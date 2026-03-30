FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

COPY --from=workspace / /workspace
COPY . /app/nanobot

WORKDIR /app/nanobot
RUN cp -R /workspace/mcp /app/mcp || true
RUN uv sync --no-dev

FROM python:3.12-slim AS runtime

WORKDIR /app/nanobot

ENV PATH="/app/nanobot/.venv/bin:${PATH}"
ENV PYTHONUNBUFFERED=1

COPY --from=builder /app /app

CMD ["python", "/app/nanobot/entrypoint.py"]
