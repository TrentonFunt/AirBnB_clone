#!/usr/bin/python3
"""Unittest for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test the console"""

    def setUp(self):
        """Setup method"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Teardown method"""
        pass

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual('', f.getvalue().strip())

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual('', f.getvalue().strip())

    def test_emptyline(self):
        """Test emptyline method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd(""))
            self.assertEqual('', f.getvalue().strip())

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            self.assertEqual(
                '** class name missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            self.assertEqual(
                '** instance id missing **', f.getvalue().strip())

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            self.assertEqual('** class name missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual('** class name missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual('** class name missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual('** instance id missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 123"))
            self.assertEqual('** attribute name missing **',
                             f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 123 name"))
            self.assertEqual('** value missing **', f.getvalue().strip())

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("count FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_show_errors(self):
        """Test show errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("show BaseModel"))
            self.assertEqual(f.getvalue().strip(),
                             str(storage.all()["BaseModel." + uid]))

    def test_create_errors(self):
        """Test create errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create Unknown"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_update_errors(self):
        """Test update errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            self.assertEqual('** class name missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual('** instance id missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel " + uid))
            self.assertEqual('** attribute name missing **',
                             f.getvalue().strip())

    def test_destroy_errors(self):
        """Test destroy errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            self.assertEqual('** class name missing **', f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_all_errors(self):
        """Test all errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_count_errors(self):
        """Test count errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("count FakeClass"))
            self.assertEqual('** class doesn\'t exist **',
                             f.getvalue().strip())

    def test_show_by_id(self):
        """Test show command with ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_destroy_by_id(self):
        """Test destroy command with ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_by_id(self):
        """Test update command with ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(
                "update BaseModel 12345 name"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_by_id_dict(self):
        """Test update command with ID and dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(
                "update BaseModel 12345 {'name': 'test'}"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_show_obj(self):
        """Test show with object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel"))
            self.assertEqual('** instance id missing **', f.getvalue().strip())

    def test_create_obj(self):
        """Test create with object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create BaseModel"))
            self.assertEqual(
                '** instance id missing **', f.getvalue().strip())

    def test_destroy_obj(self):
        """Test destroy with object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            self.assertEqual(
                '** instance id missing **', f.getvalue().strip())

    def test_all_obj(self):
        """Test all with object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all BaseModel"))
            self.assertEqual('', f.getvalue().strip())

    def test_update_obj(self):
        """Test update with object"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            self.assertEqual('** instance id missing **', f.getvalue().strip())

    def test_show_error(self):
        """Test show with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_destroy_error(self):
        """Test destroy with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_error(self):
        """Test update with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(
                "update BaseModel 12345 name"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_error2(self):
        """Test update with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 12345 {}"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_show_error2(self):
        """Test show with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_show_error3(self):
        """Test show with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_destroy_error2(self):
        """Test destroy with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_destroy_error3(self):
        """Test destroy with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_destroy_error4(self):
        """Test destroy with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 12345"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_error3(self):
        """Test update with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(
                "update BaseModel 12345 name"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_error4(self):
        """Test update with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 12345 {}"))
            self.assertEqual('** no instance found **', f.getvalue().strip())

    def test_update_error5(self):
        """Test update with error"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(
                "update BaseModel 12345 {'name': 'test'}"))
            self.assertEqual('** no instance found **', f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
