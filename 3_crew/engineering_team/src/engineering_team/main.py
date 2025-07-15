#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
Build a Python module that implements a simple to-do list manager.
The class should allow adding a task (with a description and optional due date), marking a task as completed, listing all tasks, and deleting a task by its ID.
Tasks should be kept in memory (no database needed).
Each task has:
An auto-incrementing integer ID
A description (string)
An optional due date (string or None)
A boolean completed status (default: False)

The API of the class should expose at least these methods:
add_task(description: str, due_date: Optional[str] = None) -> int — adds a task, returns its ID.
complete_task(task_id: int) -> bool — marks task completed, returns True if successful.
list_tasks() -> List[Dict] — returns a list of all tasks as dicts.
delete_task(task_id: int) -> bool — deletes the task, returns True if successful.
Make sure the class can handle invalid task IDs gracefully.
"""
module_name = "todo_list.py"
class_name = "TodoList"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()