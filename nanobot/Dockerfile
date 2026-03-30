FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS builder

WORKDIR /app
ENV UV_PYTHON=3.14.2

COPY --from=workspace / /workspace
COPY . /app/nanobot

WORKDIR /app/nanobot

RUN cp -R /workspace/mcp /app/mcp || true
RUN cp -R /workspace/nanobot-websocket-channel /app/nanobot-websocket-channel || true

RUN uv sync --no-dev

FROM python:3.14.2-slim AS runtime

WORKDIR /app

COPY --from=builder /app/nanobot /app/nanobot
COPY --from=builder /app/mcp /app/mcp
COPY --from=builder /app/nanobot-websocket-channel /app/nanobot-websocket-channel

WORKDIR /app/nanobot

ENV PATH="/app/nanobot/.venv/bin:$PATH"
ENV PYTHONPATH="/app/nanobot"

EXPOSE 18790

CMD ["python", "main.py"]
