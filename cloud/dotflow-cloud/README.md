# Dotflow Cloud

Managed execution runtime for dotflow pipelines. Run your workflow on Dotflow Cloud without managing infrastructure.

## Workflow entrypoint

Your `workflow.py` must expose a `main()` factory that returns a `DotFlow` instance:

```python
from dotflow import DotFlow

def main() -> DotFlow:
    workflow = DotFlow()
    workflow.task.add(step=[...], initial_context=...)
    return workflow
```

Dotflow Cloud runs it with the same contract used by:

```bash
dotflow start --workflow <module>.workflow:main
```

## Deploy

```bash
dotflow deploy --platform dotflow-cloud --project <project_name>
```
