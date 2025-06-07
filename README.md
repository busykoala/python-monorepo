# Python Monorepo PoC

## Installation

```bash
uv sync
```

## Development

```bash
# run pytest on all packages
uv run poe test

# lint & format all packages
uv run poe lint

# run sast on all packages
uv run poe sast

# package and release a package (target)
uv run poe package --target lib/log

# run type checks
uv run poe types
```

Additionally, these commands might be useful:

```bash
# install deps to a package
uv add <external-package> --package bar
# install dev dependency in monorepo
uv add --group dev <external-package>
```

## Docker build

```bash
# build and run foo
docker build -f deployables/foo/Dockerfile -t foo-app .
docker run foo-app

# build and run bar
docker build -f deployables/bar/Dockerfile -t bar-app .
docker run bar-app
```
