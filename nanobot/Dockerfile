FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

WORKDIR /app
ENV UV_PYTHON=3.14.2

COPY --from=workspace pyproject.toml uv.lock /app/
COPY --from=workspace mcp /app/mcp
COPY . /app/nanobot

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-workspace --package nanobot

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --package nanobot

FROM python:3.14.2-slim AS runtime

WORKDIR /app
COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv
COPY --from=builder /app /app

WORKDIR /app/nanobot
ENV PATH="/app/.venv/bin:/usr/local/bin:$PATH"
ENV PYTHONPATH="/app/nanobot"

EXPOSE 18790
CMD ["python", "entrypoint.py"]
