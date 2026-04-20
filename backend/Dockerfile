# ---- Build Stage ----
FROM python:3.12-slim AS builder

WORKDIR /build

# System-Abhängigkeiten für WeasyPrint (PDF)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .


# ---- Runtime Stage ----
FROM python:3.12-slim AS runtime

# Kein Root im Container
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# System-Libs für WeasyPrint kopieren
COPY --from=builder /usr/lib /usr/lib

# Installierte Python-Pakete kopieren
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin

# App-Code
COPY app/ ./app/

# Kein Root
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:8000/api/health').raise_for_status()"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
