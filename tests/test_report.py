import unittest
from report import generate_report

class TestReportGeneration(unittest.TestCase):
    def test_generate_report(self):
        tasks = [
            (1, "Task 1", "Description 1", "2024-05-01", "2024-05-05", "pending", 1, 100.0),
            (2, "Task 2", "Description 2", "2024-05-02", "2024-05-06", "in-progress", 2, 200.0)
        ]
        output_file = "test_report.xlsx"
        generate_report(tasks, output_file)
        # Write assertions to verify the output file exists and has correct content

if __name__ == '__main__':
    unittest.main()
