{%- set scheduled_clouds = ["dotflow-cloud", "lambda-scheduled", "ecs-scheduled", "cloud-run-scheduled", "alibaba-fc-scheduled", "github-actions"] -%}
{%- set scheduler = "none" if cookiecutter.cloud in scheduled_clouds else cookiecutter.scheduler -%}
{%- set needs_internal_start = cookiecutter.cloud in ["lambda", "lambda-scheduled", "lambda-s3-trigger", "lambda-sqs-trigger", "lambda-api-trigger", "alibaba-fc", "alibaba-fc-scheduled"] -%}
{% if cookiecutter.checkpoint == "yes" -%}
from uuid import uuid4
{% endif -%}
from dotflow import Config, DotFlow
{% if cookiecutter.storage == "file" -%}
from dotflow.providers import StorageFile
{% elif cookiecutter.storage == "s3" -%}
from dotflow.providers import StorageS3
{% elif cookiecutter.storage == "gcs" -%}
from dotflow.providers import StorageGCS
{% endif -%}
{% if scheduler == "cron" -%}
from dotflow.providers import SchedulerCron
{% endif %}
from {{ cookiecutter.module_name }}.actions import step_one, step_two

{% if cookiecutter.storage == "default" and scheduler == "none" -%}
config = Config()
{% elif cookiecutter.storage == "default" and scheduler == "cron" -%}
config = Config(
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% elif cookiecutter.storage == "file" and scheduler == "none" -%}
config = Config(storage=StorageFile())
{% elif cookiecutter.storage == "file" and scheduler == "cron" -%}
config = Config(
    storage=StorageFile(),
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% elif cookiecutter.storage == "s3" and scheduler == "none" -%}
config = Config(
    storage=StorageS3(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        region="us-east-1",
    )
)
{% elif cookiecutter.storage == "s3" and scheduler == "cron" -%}
config = Config(
    storage=StorageS3(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        region="us-east-1",
    ),
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% elif cookiecutter.storage == "gcs" and scheduler == "none" -%}
config = Config(
    storage=StorageGCS(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        project="my-gcp-project",
    )
)
{% elif cookiecutter.storage == "gcs" and scheduler == "cron" -%}
config = Config(
    storage=StorageGCS(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        project="my-gcp-project",
    ),
    scheduler=SchedulerCron(cron="*/5 * * * *"),
)
{% endif %}

def main() -> DotFlow:
{%- if cookiecutter.checkpoint == "yes" %}
    workflow = DotFlow(config=config, workflow_id=uuid4())
{%- else %}
    workflow = DotFlow(config=config)
{%- endif %}

    workflow.task.add(step=step_one)
    workflow.task.add(step=step_two)
{% if needs_internal_start %}
{%- if cookiecutter.checkpoint == "yes" %}
    workflow.start(mode="{{ cookiecutter.execution_mode }}", resume=True)
{%- else %}
    workflow.start(mode="{{ cookiecutter.execution_mode }}")
{%- endif %}
{% endif %}
    return workflow
