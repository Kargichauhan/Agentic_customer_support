from workflow.workflow_manager import WorkflowManager
from workflow.visualization import WorkflowVisualizer

if __name__ == "__main__":
    # Initialize the workflow manager
    manager = WorkflowManager()

    # Load initial workflow data
    manager.load_workflow("data/workflow_data.json")

    # Generate and save workflow visualization
    visualizer = WorkflowVisualizer(manager.get_workflow())
    visualizer.save_graph("output/workflow_diagram.png")
