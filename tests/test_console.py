#!/usr/bin/python3
"""Unittest module for the console"""
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
import io


class TestCommand(unittest.TestCase):
    """Tests for the console"""

    def setUp(self):
        """Function used to empty file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage()
        FileStorage().save()

    def test_with_help(self):
        """test the help command"""
        self.assertEqual(HBNBCommand().prompt, '(hbnb) ')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help")
        output = '\nDocumented commands (type help <topic>):\n'
        output += '========================================\n'
        output += 'EOF  all  count  create  destroy  help  quit  show  update'
        output += '\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
        output = 'Create an instance, print its id and save it\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
        output = 'Show string representation of an instance\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        output = 'Destroy an instance with its id\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
        output = 'Print the string representation of all instances\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
        output = 'Adding or updating attribute of an instance\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        output = 'Ctrl + D to exit the program\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        output = 'Quit command to exit the program\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help help")
        output = 'List available commands with "help" or detailed help with'
        output += ' "help cmd".\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help count")
        output = 'Count the number of instances of a class\n\n'
        self.assertEqual(f.getvalue(), output)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help hello")
        output = '*** No help on hello\n'
        self.assertEqual(f.getvalue(), output)

    def test_create(self):
        """test the create command"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
        opt = '** class name missing **\n'
        self.assertEqual(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create NotClass")
        opt = "** class doesn't exist **\n"
        self.assertEqual(f.getvalue(), opt)
        self.setUp()

    def test_create_default(self):
        """test the create function via default"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        opt = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        self.assertRegex(f.getvalue(), opt)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("NotClass.create()")
        opt = "** class doesn't exist **\n"
        self.assertEqual(f.getvalue(), opt)


if __name__ == '__main__':
    unittest.main()
