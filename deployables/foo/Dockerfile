# ───── Stage 1: Build wheels ─────
FROM python:3.12-alpine AS builder

WORKDIR /build

# Build dependencies
RUN apk add --no-cache build-base

# Build tools only
RUN pip install --upgrade pip build

# Copy only what's needed
COPY lib/log lib/log
COPY deployables/foo deployables/foo

# Build wheels into /dist
RUN python -m build lib/log --wheel -o /dist && \
    python -m build deployables/foo --wheel -o /dist

# ───── Stage 2: Minimal runtime (rootless) ─────
FROM python:3.12-alpine

# Create rootless user
RUN adduser -D -h /home/appuser appuser

# Drop privileges early
USER appuser
WORKDIR /home/appuser/app

# Copy only built wheels
COPY --from=builder /dist /home/appuser/dist

# Minimal install: --user + no pip cache + no bytecode
ENV PATH="/home/appuser/.local/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONOPTIMIZE=1

# Use pip before removing it
RUN pip install --no-cache-dir --user /home/appuser/dist/log-*.whl && \
    pip install --no-cache-dir --user /home/appuser/dist/foo-*.whl && \
    rm -rf ~/.cache ~/.local/lib/python*/site-packages/pip*

# Final entrypoint
CMD ["python", "-m", "foo.main"]
