# mini-agent

A minimal Python agent project skeleton managed with [uv](https://docs.astral.sh/uv/).

## Requirements

- Python 3.12+
- uv

## Quick start

```bash
uv sync
uv run mini-agent
uv run pytest
```

The entry point is `src/mini_agent/__init__.py` and currently prints `Hello from mini-agent!`.
`tests/test_smoke.py` verifies that output.

## Project layout

```text
.
├── pyproject.toml
├── .python-version
├── src/mini_agent/__init__.py
└── tests/test_smoke.py
```

## Status

Early skeleton (W1D1). Agent functionality will be added incrementally.
