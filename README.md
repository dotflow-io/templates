# Dotflow Template

Official project template for [dotflow](https://github.com/dotflow-io/dotflow) — the lightweight Python library for execution pipelines.

## Cloud deployment

Deploy your dotflow pipelines to any major cloud provider. Choose a target platform during project creation and get all the infrastructure files you need — fully configured and ready to deploy.

## CLI

| Command | Description |
|---------|-------------|
| `dotflow init` | Scaffold a new project (interactive) |
| `dotflow cloud list` | Show available deployment platforms |
| `dotflow cloud generate --platform <name>` | Generate deployment files for an existing project |
| `dotflow deploy --platform <name> --project <name>` | Deploy to AWS (Lambda, ECS) |

---

### Available platforms

| Value | Icon | Platform | Deploy method | Guide |
|---|---|---|---|---|
| `none` | 🚫 | — | — | — |
| `docker` | <img alt="Docker" src="https://cdn.simpleicons.org/docker" width="18" /> | Docker | `docker compose up` | [Guide](cloud/docker/README.md) |
| `lambda` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> | AWS Lambda | `dotflow deploy` | [Guide](cloud/lambda/README.md) |
| `lambda-scheduled` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS Lambda + EventBridge | `dotflow deploy --schedule` | [Guide](cloud/lambda-scheduled/README.md) |
| `lambda-s3-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon S3" src="https://api.iconify.design/logos:aws-s3.svg" width="18" /> | AWS Lambda + S3 Trigger | `sam deploy` | [Guide](cloud/lambda-s3-trigger/README.md) |
| `lambda-sqs-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon SQS" src="https://api.iconify.design/logos:aws-sqs.svg" width="18" /> | AWS Lambda + SQS Trigger | `sam deploy` | [Guide](cloud/lambda-sqs-trigger/README.md) |
| `lambda-api-trigger` | <img alt="AWS Lambda" src="https://www.vectorlogo.zone/logos/amazon_awslambda/amazon_awslambda-icon.svg" width="18" /> <img alt="Amazon API Gateway" src="https://api.iconify.design/logos:aws-api-gateway.svg" width="18" /> | AWS Lambda + API Gateway | `sam deploy` | [Guide](cloud/lambda-api-trigger/README.md) |
| `ecs` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> | AWS ECS (Fargate) | `dotflow deploy` | [Guide](cloud/ecs/README.md) |
| `ecs-scheduled` | <img alt="Amazon ECS" src="https://www.vectorlogo.zone/logos/amazon_ecs/amazon_ecs-icon.svg" width="18" /> <img alt="Amazon EventBridge" src="https://api.iconify.design/logos:aws-eventbridge.svg" width="18" /> | AWS ECS + EventBridge | CloudFormation | [Guide](cloud/ecs-scheduled/README.md) |
| `cloud-run` | <img alt="Google Cloud" src="https://cdn.simpleicons.org/googlecloud" width="18" /> | Google Cloud Run | `gcloud run deploy` | [Guide](cloud/cloud-run/README.md) |
| `cloud-run-scheduled` | <img alt="Google Cloud Run" src="https://cdn.simpleicons.org/googlecloud" width="18" /> <img alt="Cloud Scheduler" src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" width="18" /> | Cloud Run + Scheduler | `gcloud` | [Guide](cloud/cloud-run-scheduled/README.md) |
| `kubernetes` | <img alt="Kubernetes" src="https://cdn.simpleicons.org/kubernetes" width="18" /> | Kubernetes | `kubectl apply` | [Guide](cloud/kubernetes/README.md) |
| `azure-functions` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Functions | :soon: | — |
| `azure-container` | <img alt="Microsoft Azure" src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" width="18" /> | Azure Container Apps | :soon: | — |
| `heroku` | <img alt="Heroku" src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" width="18" /> | Heroku | :soon: | — |
| `fly-io` | <img alt="Fly.io" src="https://cdn.simpleicons.org/flydotio" width="18" /> | Fly.io | :soon: | — |
| `railway` | <img alt="Railway" src="https://cdn.simpleicons.org/railway" width="18" /> | Railway | :soon: | — |
| `render` | <img alt="Render" src="https://cdn.simpleicons.org/render" width="18" /> | Render | :soon: | — |
| `digital-ocean` | <img alt="DigitalOcean" src="https://cdn.simpleicons.org/digitalocean" width="18" /> | DigitalOcean App Platform | :soon: | — |
