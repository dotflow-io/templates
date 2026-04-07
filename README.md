# dotflow template

This repository is a **Cookiecutter template** for generating a **dotflow** workflow project, with optional **cloud deployment scaffolding**.

## Prerequisites

- Python **>= 3.9**
- `cookiecutter` installed (via `pipx` or `pip`)

## Generate a project

```bash
cookiecutter https://github.com/dotflow-io/template.git
```

You'll be prompted for these options:

| Option | Description |
|------|-----------|
| `project_name` | Generated project name (e.g. `my_pipeline`) |
| `module_name` | Python module name (derived from `project_name`, with `-` replaced by `_`) |
| `storage` | Storage backend (`default`, `file`, `s3`, `gcs`) |
| `scheduler` | Scheduling (`none`, `cron`) |
| `execution_mode` | Execution (`sequential`, `parallel`, `background`) |
| `retry` | Enable retry (`no`, `yes`) |
| `checkpoint` | Enable checkpointing (`no`, `yes`) |
| `cloud` | Adds deployment files (`none`, `docker`, `lambda`, `lambda-scheduled`, `lambda-s3-trigger`, `lambda-sqs-trigger`, `lambda-api-trigger`, `ecs`, `ecs-scheduled`, `cloud-run`, `cloud-run-scheduled`, `kubernetes`) |
| `schedule_expression` | Cron or rate expression for scheduled platforms (e.g. `rate(6 hours)`, `cron(0 12 * * ? *)`) |

## Cloud templates

When the `cloud` option is set to a value other than `none`, the post-generation hook copies the corresponding infrastructure files (e.g. `Dockerfile`, `docker-compose.yml`, `handler.py`) into the generated project root.

You can also generate cloud files separately using the CLI:

```bash
dotflow cloud generate --platform lambda
dotflow cloud list
```

### Available platforms

| Value | Icon | Platform | Available |
|---|---|---|---|
| `none` | 🚫 | — | — |
| `docker` | <img alt="Docker" src="https://cdn.simpleicons.org/docker" width="18" /> | Docker | :white_check_mark: |
| `lambda` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> | AWS Lambda | :white_check_mark: |
| `lambda-scheduled` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS Lambda + EventBridge Schedule | :white_check_mark: |
| `lambda-s3-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon S3" src="https://api.iconify.design/logos:aws-s3.svg" width="18" /> | AWS Lambda + S3 Trigger | :white_check_mark: |
| `lambda-sqs-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon SQS" src="https://api.iconify.design/logos:aws-sqs.svg" width="18" /> | AWS Lambda + SQS Trigger | :white_check_mark: |
| `lambda-api-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon API Gateway" src="https://api.iconify.design/logos:aws-api-gateway.svg" width="18" /> | AWS Lambda + API Gateway | :white_check_mark: |
| `ecs` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> | AWS ECS (Fargate) | :white_check_mark: |
| `ecs-scheduled` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS ECS + EventBridge Schedule | :white_check_mark: |
| `cloud-run` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Run | :white_check_mark: |
| `cloud-run-scheduled` | <img alt="Google Cloud Run" src="https://cdn.simpleicons.org/googlecloud" width="18" /> <img alt="Cloud Scheduler" src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" width="18" /> | Cloud Run + Cloud Scheduler | :white_check_mark: |
| `kubernetes` | <img alt="Kubernetes" src="https://cdn.simpleicons.org/kubernetes" width="18" /> | Kubernetes | :soon: |
| `azure-functions` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Functions | :soon: |
| `azure-container` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Container Apps | :soon: |
| `heroku` | <img alt="Heroku" src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" width="18" /> | Heroku | :soon: |
| `fly-io` | <img alt="Fly.io" src="https://cdn.simpleicons.org/flydotio" width="18" /> | Fly.io | :soon: |
| `railway` | <img alt="Railway" src="https://cdn.simpleicons.org/railway" width="18" /> | Railway | :soon: |
| `render` | <img alt="Render" src="https://cdn.simpleicons.org/render" width="18" /> | Render | :soon: |
| `digital-ocean` | <img alt="DigitalOcean" src="https://cdn.simpleicons.org/digitalocean" width="18" /> | DigitalOcean App Platform | :soon: |

### Platform details

- **`docker`** — `Dockerfile` and `docker-compose.yml`
- **`lambda`** — Container-based Lambda handler template
- **`lambda-scheduled`** — SAM template with EventBridge cron/rate trigger
- **`lambda-s3-trigger`** — SAM template triggered by S3 file upload
- **`lambda-sqs-trigger`** — SAM template triggered by SQS messages
- **`lambda-api-trigger`** — SAM template triggered by HTTP POST via API Gateway
- **`ecs`** — Task definition template for ECS Fargate (often paired with Amazon ECR)
- **`ecs-scheduled`** — CloudFormation with EventBridge scheduled Fargate task
- **`cloud-run`** — Includes `cloudbuild.yaml`
- **`cloud-run-scheduled`** — Includes `cloudbuild.yaml` + `scheduler.yaml` for Cloud Scheduler
- **`kubernetes`** — Deployment + service manifests
- **`azure-functions`** — `function.json` + `host.json`
- **`azure-container`** — `container-app.yaml`
- **`heroku`** — `Procfile` + `heroku.yml`
- **`fly-io`** — `fly.toml`
- **`railway`** — `railway.json`
- **`render`** — `render.yaml`
- **`digital-ocean`** — `app.yaml`

## Next steps (inside the generated project)

Enter the generated folder and run:

```bash
pip install -e ".[dev]"
python -m <your_module_name>.workflow
```

Run tests:

```bash
pytest
```

## Template structure

- `cookiecutter.json`: defines the prompt questions/options.
- `{{cookiecutter.project_name}}/`: generated Python project skeleton.
- `hooks/post_gen_project.py`: hook that downloads `cloud/` files based on the selected `cloud` option.
- `cloud/`: catalog of platforms and available files (see `cloud/registry.json`).
