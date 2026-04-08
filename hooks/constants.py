"""Constants for post-generation hook."""

CLOUD_URL = (
    "https://raw.githubusercontent.com/dotflow-io/template/master/cloud"
)

BOLD = "\033[1m"
CYAN = "\033[36m"
RESET = "\033[0m"

AWS_PLATFORMS = {
    "lambda",
    "lambda-scheduled",
    "lambda-s3-trigger",
    "lambda-sqs-trigger",
    "lambda-api-trigger",
    "ecs",
    "ecs-scheduled",
}

GCP_PLATFORMS = {
    "cloud-run",
    "cloud-run-scheduled",
}

SCHEDULED_PLATFORMS = {
    "lambda-scheduled",
    "ecs-scheduled",
    "cloud-run-scheduled",
}
