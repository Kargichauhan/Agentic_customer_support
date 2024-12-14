import unittest
from workflow.workflow_manager import WorkflowManager

class TestWorkflowManager(unittest.TestCase):
    def test_add_node(self):
        manager = WorkflowManager()
        manager.add_node("node1", {"name": "Start"})
        self.assertIn("node1", manager.get_workflow())
