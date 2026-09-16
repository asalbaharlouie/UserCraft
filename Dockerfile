# ---- Base image: Python + uv pre-installed (maintained by Astral) ----
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

# Copy only dependency files first so Docker can cache this layer
# and avoid re-installing dependencies on every code change.
COPY pyproject.toml uv.lock ./

# Install dependencies (frozen = exactly what's in uv.lock, no surprises)
RUN uv sync --frozen --no-dev

# Now copy the actual source code
COPY . .

# Make sure the virtual environment created by uv is on PATH
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "crud:app"]
