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
```

Additionally, these commands might be useful:

```bash
# install deps to a package
uv add <external-package> --package bar
# install dev dependency in monorepo
uv add --group dev <external-package>
```
