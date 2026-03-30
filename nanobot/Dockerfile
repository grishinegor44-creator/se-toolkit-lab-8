FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app/nanobot

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev || uv sync --no-dev

COPY . .

RUN uv sync --frozen --no-dev || uv sync --no-dev


FROM python:3.12-slim AS runtime

WORKDIR /app/nanobot

ENV PATH="/app/nanobot/.venv/bin:${PATH}"
ENV PYTHONUNBUFFERED=1

COPY --from=builder /app/nanobot /app/nanobot
COPY --from=builder /uv /uv
COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv

CMD ["python", "/app/nanobot/entrypoint.py"]
