# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY src/ src/
# COPY tests/ tests/

# CMD ["pytest", "-v"]

# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY tests ./tests

# ---------- Stage 2: Runtime ----------
FROM python:3.11-slim

# Create non-root user (MANDATORY for marks)
RUN useradd -m appuser
RUN mkdir -p /app/data && chown -R appuser:appuser /app/data

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src

USER appuser

ENV PYTHONPATH=/app

# CMD ["python", "-m", "src"]
CMD ["python", "src/app.py"]
