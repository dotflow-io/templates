from dotflow import Config, DotFlow
from dotflow.providers import StorageFile

from {{ cookiecutter.module_name }}.actions import step_one, step_two


config = Config(storage=StorageFile())


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
