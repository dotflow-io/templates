# {{ cookiecutter.project_name }}

A workflow built with [dotflow](https://github.com/dotflow-io/dotflow).

## Configuration

| Option | Value |
|--------|-------|
| Storage | {{ cookiecutter.storage }} |
| Scheduler | {{ cookiecutter.scheduler }} |
| Execution mode | {{ cookiecutter.execution_mode }} |
| Retry | {{ cookiecutter.retry }} |
| Checkpoint | {{ cookiecutter.checkpoint }} |

## Getting Started

```bash
pip install -e ".[dev]"
python -m {{ cookiecutter.module_name }}.workflow
```

## Running Tests

```bash
pytest
```
