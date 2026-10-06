# Stage-1 Dockerfile for AnticipatedD/G4LA13_Gala4_Localizing_Code-Graph
FROM python:3.12-slim

# Environment settings
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install dependencies (minimal for Stage-1)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy service code
WORKDIR /app
COPY app.py /app/

# Expose port (harness sets PORT)
EXPOSE 8080

# Run the service
CMD ["python", "app.py"]
