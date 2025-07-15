from typing import Optional, Dict, List

class TodoList:
    """
    A simple in-memory to-do list manager which allows for adding, deleting,
    completing, and listing tasks. Tasks are stored internally with an auto-incrementing
    ID to uniquely identify each task.
    """
    
    def __init__(self):
        """
        Initializes the TodoList.
        """
        self.tasks = {}
        self.current_id = 0
        
    def add_task(self, description: str, due_date: Optional[str] = None) -> int:
        """
        Adds a new task to the to-do list.
        
        :param description: The description of the task.
        :param due_date: The optional due date of the task as a string.
        :return: The auto-generated unique ID for the new task.
        """
        task_id = self.current_id
        self.tasks[task_id] = {
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.current_id += 1
        return task_id
        
    def complete_task(self, task_id: int) -> bool:
        """
        Marks a specified task as completed.
        
        :param task_id: The ID of the task to mark as completed.
        :return: True if the operation was successful, otherwise False.
        """
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            return True
        return False
        
    def list_tasks(self) -> List[Dict]:
        """
        Lists all tasks in the to-do list.
        
        :return: A list of dicts, each representing a task.
        """
        return [{'id': task_id, **task_info} for task_id, task_info in self.tasks.items()]
        
    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task from the to-do list by its ID.
        
        :param task_id: The ID of the task to be deleted.
        :return: True if the task was deleted, otherwise False.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False