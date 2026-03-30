FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

WORKDIR /app
COPY --from=workspace / /workspace
COPY . /app/nanobot

WORKDIR /app/nanobot
RUN cp -R /workspace/mcp /app/mcp || true

ENV UV_PYTHON=3.14.2
RUN uv sync --no-dev --frozen || uv sync --no-dev


FROM python:3.14.2-slim AS runtime

WORKDIR /app/nanobot

ENV PATH="/app/nanobot/.venv/bin:${PATH}"
ENV PYTHONUNBUFFERED=1

COPY --from=builder /app/nanobot /app/nanobot

CMD ["python", "/app/nanobot/entrypoint.py"]
