import unittest
from unittest.mock import patch
from io import StringIO
from task_tracker import main

class TestCLIIntegration(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['1', 'Title', 'Description', '2024-05-24', '2024-05-31', 'completed', '1', '100.0', '7', ''])
    def test_main_menu_integration(self, mock_input, mock_stdout):
        main()
        # Write assertions to verify the output printed to stdout

if __name__ == '__main__':
    unittest.main()
