import unittest
from database import TaskDatabase

class TestTaskDatabase(unittest.TestCase):
    def setUp(self):
        self.db = TaskDatabase(':memory:')  # Use in-memory database for testing

    def test_add_task(self):
        self.db.add_task("Test Task", "Test Description", "2024-05-01", "2024-05-05", "pending", 1, 100.0)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test Task")

    def test_get_all_tasks(self):
        self.db.add_task("Task 1", "Description 1", "2024-05-01", "2024-05-05", "pending", 1, 100.0)
        self.db.add_task("Task 2", "Description 2", "2024-05-02", "2024-05-06", "in-progress", 2, 200.0)
        tasks = self.db.get_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_get_last_n_tasks(self):
        for i in range(10):
            self.db.add_task(f"Task {i+1}", f"Description {i+1}", "2024-05-01", "2024-05-05", "pending", 1, 100.0)
        tasks = self.db.get_last_n_tasks(5)
        self.assertEqual(len(tasks), 5)

    def test_filter_tasks_by_date(self):
        self.db.add_task("Task 1", "Description 1", "2024-05-01", "2024-05-05", "pending", 1, 100.0)
        self.db.add_task("Task 2", "Description 2", "2024-05-02", "2024-05-06", "in-progress", 2, 200.0)
        tasks = self.db.filter_tasks_by_date("2024-05-01", "2024-05-05")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Task 1")

    def test_update_task(self):
        self.db.add_task("Task 1", "Description 1", "2024-05-01", "2024-05-05", "pending", 1, 100.0)
        self.db.update_task(1, "Updated Task", "Updated Description", "2024-05-03", "2024-05-07", "completed", 2, 150.0)
        task = self.db.get_all_tasks()[0]
        self.assertEqual(task[1], "Updated Task")
        self.assertEqual(task[2], "Updated Description")
        self.assertEqual(task[3], "2024-05-03")
        self.assertEqual(task[4], "2024-05-07")
        self.assertEqual(task[5], "completed")
        self.assertEqual(task[6], 2)
        self.assertEqual(task[7], 150.0)

if __name__ == '__main__':
    unittest.main()
