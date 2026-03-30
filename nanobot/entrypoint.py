from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"
RESOLVED_CONFIG_PATH = ROOT / "config.resolved.json"
WORKSPACE_PATH = ROOT / "workspace"

PLACEHOLDER_RE = re.compile(r"\$\{([^}:]+)(?::-[^}]*)?\}")


def env(*names: str, default: str | None = None) -> str | None:
    for name in names:
        value = os.environ.get(name)
        if value is not None and value != "":
            return value
    return default


def require_env(*names: str) -> str:
    value = env(*names)
    if value is None:
        raise RuntimeError(f"Missing required environment variable(s): {', '.join(names)}")
    return value


def as_port(value: str | None) -> int | str | None:
    if value is None:
        return None
    return int(value) if value.isdigit() else value


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_placeholders(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: resolve_placeholders(v) for k, v in value.items()}
    if isinstance(value, list):
        return [resolve_placeholders(v) for v in value]
    if isinstance(value, str):
        def repl(match: re.Match[str]) -> str:
            var_name = match.group(1)
            return os.environ.get(var_name, "")
        return PLACEHOLDER_RE.sub(repl, value)
    return value


def walk_nodes(node: Any):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from walk_nodes(value)
    elif isinstance(node, list):
        for item in node:
            yield from walk_nodes(item)


def patch_provider_like(config: dict[str, Any], llm_api_key: str, llm_api_base_url: str, llm_api_model: str) -> None:
    for node in walk_nodes(config):
        if not isinstance(node, dict):
            continue

        keys = set(node.keys())
        looks_like_provider = bool(keys & {"apiKey", "apiBase", "baseUrl", "model"})

        if not looks_like_provider:
            continue

        if "apiKey" in node:
            node["apiKey"] = llm_api_key
        if "apiBase" in node:
            node["apiBase"] = llm_api_base_url
        if "baseUrl" in node:
            node["baseUrl"] = llm_api_base_url
        if "model" in node:
            node["model"] = llm_api_model


def patch_sections_by_name(node: Any, section_names: set[str], replacements: dict[str, Any]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in section_names and isinstance(value, dict):
                for field, replacement in replacements.items():
                    if replacement is not None and field in value:
                        value[field] = replacement
            patch_sections_by_name(value, section_names, replacements)
    elif isinstance(node, list):
        for item in node:
            patch_sections_by_name(item, section_names, replacements)


def patch_mcp_servers(config: dict[str, Any], backend_url: str, backend_api_key: str) -> None:
    candidate_keys = ("mcpServers", "mcp_servers", "mcp")

    aliases = {
        "BACKEND_URL": backend_url,
        "LMS_BACKEND_URL": backend_url,
        "NANOBOT_LMS_BACKEND_URL": backend_url,
        "BACKEND_API_KEY": backend_api_key,
        "LMS_API_KEY": backend_api_key,
        "NANOBOT_LMS_API_KEY": backend_api_key,
    }

    for key in candidate_keys:
        container = config.get(key)
        if not isinstance(container, dict):
            continue

        for server in container.values():
            if not isinstance(server, dict):
                continue

            env_block = server.get("env")
            if not isinstance(env_block, dict):
                env_block = {}
                server["env"] = env_block

            env_block.update(aliases)


def main() -> None:
    llm_api_key = require_env("LLM_API_KEY")
    llm_api_base_url = require_env("LLM_API_BASE_URL")
    llm_api_model = require_env("LLM_API_MODEL")

    backend_url = require_env("NANOBOT_LMS_BACKEND_URL")
    backend_api_key = require_env("NANOBOT_LMS_API_KEY")

    gateway_host = require_env("NANOBOT_GATEWAY_CONTAINER_ADDRESS")
    gateway_port = as_port(require_env("NANOBOT_GATEWAY_CONTAINER_PORT"))

    webchat_host = env("NANOBOT_WEBCHAT_CONTAINER_ADDRESS")
    webchat_port = as_port(env("NANOBOT_WEBCHAT_CONTAINER_PORT"))
    access_key = env("NANOBOT_ACCESS_KEY")

    os.environ["LLM_API_KEY"] = llm_api_key
    os.environ["LLM_API_BASE_URL"] = llm_api_base_url
    os.environ["LLM_API_MODEL"] = llm_api_model
    os.environ["NANOBOT_LMS_BACKEND_URL"] = backend_url
    os.environ["NANOBOT_LMS_API_KEY"] = backend_api_key
    os.environ["BACKEND_URL"] = backend_url
    os.environ["BACKEND_API_KEY"] = backend_api_key

    config = load_json(CONFIG_PATH)
    config = resolve_placeholders(config)

    if not isinstance(config, dict):
        raise RuntimeError("config.json must contain a JSON object at the top level")

    patch_provider_like(config, llm_api_key, llm_api_base_url, llm_api_model)

    patch_sections_by_name(
        config,
        {"gateway"},
        {
            "host": gateway_host,
            "address": gateway_host,
            "port": gateway_port,
        },
    )

    patch_sections_by_name(
        config,
        {"webchat"},
        {
            "host": webchat_host,
            "address": webchat_host,
            "port": webchat_port,
            "access_key": access_key,
            "accessKey": access_key,
        },
    )

    patch_mcp_servers(config, backend_url, backend_api_key)

    save_json(RESOLVED_CONFIG_PATH, config)

    os.execvp(
        "nanobot",
        [
            "nanobot",
            "gateway",
            "--config",
            str(RESOLVED_CONFIG_PATH),
            "--workspace",
            str(WORKSPACE_PATH),
        ],
    )


if __name__ == "__main__":
    main()
