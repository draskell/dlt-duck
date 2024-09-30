# DLT Test Project

This is a simple personal project to experiment with the ergonomics of the Astral projects [Ruff](https://github.com/astral-sh/ruff) and [UV](https://github.com/astral-sh/uv) and the functionality of [DLT](https://github.com/dlt-hub/dlt) and [Duck DB](https://github.com/duckdb/duckdb). I'm using Oakland CrimeWatch data as a sample API for DLT integration and a Duck DB warehouse as the data destination. 

I'm using VS Code, so subsequent instructions will assume that IDE.

# Install/Setup

Using UV to manage Python packages. 

1. Install UV: https://docs.astral.sh/uv/getting-started/installation/
1. Install Ruff extension for VS Code: https://github.com/astral-sh/ruff-vscode
1. Install project dependencies: `uv sync`
1. Get a Socrata App Token for API requests: https://dev.socrata.com/docs/app-tokens
1. Make a `~/.env` with the `OAKLAND_APP_TOKEN` environment set to the Token from step 1.

# Use

Run the pipeline with: `uv run integration/pipeline.py`

## UV Notes

UV is under active development, to update and get new features: `uv self update`

Activating the virtual environment created by UV is the same as any virtaulenv: `source .venv/bin/activate`. I alias this to `vact`. UV will also activate the virtual env when using `run`, for example: `uv run integration/pipeline.py`.

## Ruff Notes

Update VS Code to format on save in `.venv/settings.json`:

```
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    },
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

## Duck DB

Connect to the DuckDB database file created by the pipeline: `duckdb dlt_pipeline.duckdb`
