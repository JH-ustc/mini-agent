# mini-agent

![CI](https://github.com/JH-ustc/mini-agent/actions/workflows/ci.yml/badge.svg)

A minimal Python agent project skeleton managed with [uv](https://docs.astral.sh/uv/).

## Requirements

- Python 3.12+
- uv

## Quick start

```bash
uv sync
uv run mini-agent
uv run mini-agent --version
uv run python -m mini_agent
uv run pytest
```

The entry point is `src/mini_agent/__init__.py` and currently prints `Hello from mini-agent!`.
`--version` prints the installed package version, and the `__main__.py` module makes
`python -m mini_agent` work the same way. `tests/test_smoke.py` covers both paths.

## Project layout

```text
.
├── pyproject.toml
├── .python-version
├── .github/workflows/ci.yml
├── src/mini_agent/__init__.py
├── src/mini_agent/__main__.py
└── tests/
    ├── test_cli.py
    └── test_smoke.py
```

## Status

Early skeleton (W1D1). Agent functionality will be added incrementally.
GitHub Actions runs the test suite on every push to `main` and on pull requests.
