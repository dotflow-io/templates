# Docker

**Files:** `Dockerfile`, `docker-compose.yml`

## Prerequisites

- Docker

## Deploy

```bash
docker compose build
docker compose up
```

## Important

- Do not rename `workflow.py` or the `main()` function — the `Dockerfile` runs `dotflow start --workflow <module>.workflow:main`
- The `docker-compose.yml` uses the `project_name` as container name
