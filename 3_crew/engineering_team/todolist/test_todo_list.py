import unittest
from todo_list import TodoList

class TestTodoList(unittest.TestCase):

    def test_add_task(self):
        todo = TodoList()
        task_id = todo.add_task('Task 1')
        self.assertEqual(task_id, 0)

    def test_complete_task(self):
        todo = TodoList()
        task_id = todo.add_task('Task 1')
        self.assertEqual(todo.complete_task(task_id), True)

    def test_list_tasks(self):
        todo = TodoList()
        todo.add_task('Task 1')
        tasks = todo.list_tasks()
        self.assertEqual(len(tasks), 1)

    def test_delete_task(self):
        todo = TodoList()
        task_id = todo.add_task('Task 1')
        self.assertEqual(todo.delete_task(task_id), True)

if __name__ == '__main__':
    unittest.main()