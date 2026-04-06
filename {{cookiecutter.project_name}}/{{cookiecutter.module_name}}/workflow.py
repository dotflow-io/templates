from dotflow import Config, DotFlow
{% if cookiecutter.storage == "file" -%}
from dotflow.providers import StorageFile
{% elif cookiecutter.storage == "s3" -%}
from dotflow.providers import StorageS3
{% elif cookiecutter.storage == "gcs" -%}
from dotflow.providers import StorageGCS
{% endif %}
from {{ cookiecutter.module_name }}.actions import step_one, step_two

{% if cookiecutter.storage == "default" -%}
config = Config()
{% elif cookiecutter.storage == "file" -%}
config = Config(storage=StorageFile())
{% elif cookiecutter.storage == "s3" -%}
config = Config(
    storage=StorageS3(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        region="us-east-1",
    )
)
{% elif cookiecutter.storage == "gcs" -%}
config = Config(
    storage=StorageGCS(
        bucket="my-dotflow-bucket",
        prefix="workflows/",
        project="my-gcp-project",
    )
)
{% endif %}

def main():
    workflow = DotFlow(config=config)

    workflow.task.add(step=step_one)
    workflow.task.add(step=step_two)
    workflow.start()

    for task in workflow.result_task():
        print(f"Task {task.task_id}: {task.status}")

    return workflow


if __name__ == "__main__":
    main()
