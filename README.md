# UV POC

```bash
# create a virtual environment, update deps
uv venv
uv sync

# run commands in the virtual environment
uv run python deployables/foo/foo/main.py
uv run pytest
uv run mypy
uv run bandit -c pyproject.toml -r .
uv run ruff format
uv run ruff check --fix

# install deps
uv add <external package> --package bar

# create lock file
uv lock
```
