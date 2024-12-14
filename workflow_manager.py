import json

class WorkflowManager:
    def __init__(self):
        self.workflow = {}

    def load_workflow(self, file_path):
        """Loads workflow data from a JSON file."""
        with open(file_path, 'r') as f:
            self.workflow = json.load(f)

    def get_workflow(self):
        """Returns the current workflow."""
        return self.workflow

    def add_node(self, node_id, details):
        """Adds a new node to the workflow."""
        self.workflow[node_id] = details

    def connect_nodes(self, from_node, to_node):
        """Connects two nodes in the workflow."""
        if from_node in self.workflow:
            self.workflow[from_node]['connections'].append(to_node)
