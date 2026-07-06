# syntax=docker/dockerfile:1

FROM python:3.13-slim

WORKDIR /app

# Install uv (fast dependency manager)
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml uv.lock ./
COPY src ./src

# Install dependencies
RUN uv sync --frozen

# Install project in editable mode
RUN uv pip install -e .

# Default working directory for mounted volumes
WORKDIR /data

# CLI entrypoint
ENTRYPOINT ["file-organizer"]