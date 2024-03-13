import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new=StringIO())
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue("Documented commands" in f.getvalue())

    @patch('sys.stdout', new=StringIO())
    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual("", f.getvalue().strip())

    # Add tests for each command: count, show, destroy, update, create, all

    @patch('sys.stdout', new=StringIO())
    def test_count(self):
        # Add test for count command
        pass

    @patch('sys.stdout', new=StringIO())
    def test_show(self):
        # Add test for show command
        pass

    @patch('sys.stdout', new=StringIO())
    def test_destroy(self):
        # Add test for destroy command
        pass

    @patch('sys.stdout', new=StringIO())
    def test_update(self):
        # Add test for update command
        pass

    @patch('sys.stdout', new=StringIO())
    def test_create(self):
        # Add test for create command
        pass

    @patch('sys.stdout', new=StringIO())
    def test_all(self):
        # Add test for all command
        pass


if __name__ == '__main__':
    unittest.main()
