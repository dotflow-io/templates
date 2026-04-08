# GitHub Actions

Run your dotflow pipeline on a schedule or manually using GitHub Actions as the runtime.

## Generated files

| File | Description |
|------|-------------|
| `.github/workflows/dotflow.yml` | Workflow with cron schedule and manual trigger |

## How it works

The workflow runs directly on a GitHub Actions runner — no Docker, no cloud provider, no deploy. Push your code and the pipeline runs on the configured schedule.

## Setup

1. Generate the project:

```bash
dotflow init
# Select cloud: github-actions
```

2. Push to GitHub:

```bash
git init && git add . && git commit -m "initial"
gh repo create my_pipeline --push --source .
```

3. The pipeline runs automatically on the configured schedule, or trigger manually from the **Actions** tab.

## View logs

Go to your repository > **Actions** tab > select the workflow run.

## Important

- The cron expression uses **UTC timezone**
- GitHub Actions cron has a minimum interval of 5 minutes and may be delayed during high load
- The `workflow_dispatch` event allows manual trigger from the GitHub UI
- No secrets or credentials needed unless your pipeline uses external services (S3, databases, etc.)
