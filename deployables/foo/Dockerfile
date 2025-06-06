# Stage 1: Build wheels as root
FROM python:3.12-slim AS builder

WORKDIR /build

# Copy only what's needed
COPY lib/log lib/log
COPY deployables/foo deployables/foo

# Install build tools (system-wide is fine for build stage)
RUN pip install --upgrade pip build

# Build wheels into /dist
RUN python -m build lib/log --wheel -o /dist && \
    python -m build deployables/foo --wheel -o /dist

# Stage 2: Minimal runtime image as non-root
FROM python:3.12-slim

# Create and switch to a non-root user
RUN useradd -m appuser
USER appuser

WORKDIR /home/appuser/app

# Copy built wheels from the builder stage
COPY --from=builder /dist /home/appuser/dist

# Install the wheels in the correct order (to ~/.local)
ENV PATH="/home/appuser/.local/bin:$PATH"
RUN pip install --no-cache-dir --user /home/appuser/dist/log-*.whl && \
    pip install --no-cache-dir --user /home/appuser/dist/foo-*.whl

# Entry point
CMD ["python", "-m", "foo.main"]
