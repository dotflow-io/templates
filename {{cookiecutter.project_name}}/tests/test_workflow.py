import unittest

from dotflow.core.dotflow import DotFlow
from dotflow.core.types.status import TypeStatus

from {{ cookiecutter.module_name }}.actions import step_one, step_two


class TestWorkflow(unittest.TestCase):
    def test_workflow_completes(self):
        workflow = DotFlow()
        workflow.task.add(step=step_one)
        workflow.task.add(step=step_two)
        workflow.start()

        tasks = workflow.result_task()
        self.assertEqual(len(tasks), 2)
        for task in tasks:
            self.assertEqual(task.status, TypeStatus.COMPLETED)

    def test_step_one_output(self):
        workflow = DotFlow()
        workflow.task.add(step=step_one)
        workflow.start()

        storage = workflow.result_storage()
        self.assertEqual(storage[0], {"message": "hello from dotflow"})
