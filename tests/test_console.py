#!/usr/bin/python3
"""Testing the console module"""

from datetime import datetime
from os import remove, getenv, system
import unittest
from console import HBNBCommand
from io import StringIO
from subprocess import getoutput
from unittest.mock import patch
from models import storage

all = storage.all


class TestHBNBCommand(unittest.TestCase):
    """Testing the HBNBCommand class"""

    def check_message(self, command, expected="** class name missing **"):
        """tests that an expected error message is printed

        Args:
            command (string): the command to be executed
            expected (string): the error message expected"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            self.assertEqual(f.getvalue().rstrip(), expected)

    def setUp(self):
        """create test objects for all tests"""
        self.cli = HBNBCommand()

    def tearDown(self):
        """deletes the objects file"""
        try:
            remove('file.json')
        except FileNotFoundError:
            pass

    # create
    def test_create_no_class(self):
        """tests create with no class name"""
        self.check_message('create')

    def test_create_invalid_class(self):
        """tests create with invalid class name"""
        self.check_message('create InvalidClass',
                           "** class doesn't exist **")

    def test_create_valid_class(self):
        """tests create with valid class"""
        with patch('uuid.uuid4', return_value='Cayenne'):
            self.check_message('create City', 'Cayenne')

    def test_create_with_params(self):
        """tests the create method with params

        Usage create <class name> <params 1> <params 2> ...
        params syntax: <key>=<value>"""
        with patch('uuid.uuid4', return_value='GraceParsons'):
            self.check_message(
                'create User first_name="Grace" last_name="Parsons"',
                'GraceParsons')
        with patch('uuid.uuid4', return_value='DarrellYoung'):
            self.check_message(
                'create User name="Darrell_Young" age=29',
                'DarrellYoung')

        self.assertEqual(all()["User.GraceParsons"].first_name, "Grace")
        self.assertEqual(all()["User.GraceParsons"].last_name, "Parsons")
        self.assertEqual(all()["User.DarrellYoung"].name, "Darrell Young")
        self.assertEqual(all()["User.DarrellYoung"].age, 29)
        self.assertIs(type(all()["User.GraceParsons"].first_name), str)
        self.assertIs(type(all()["User.DarrellYoung"].age), int)
        self.assertIs(type(all()["User.DarrellYoung"].name), str)

    @unittest.skipIf(not getenv('HBNB_MYSQL_DB'), 'not testing database')
    def test_create_in_database(self):
        """tests if an object is created in database"""

        get_count = 'echo "SELECT COUNT(*) FROM states;"'
        initial = getoutput(f'{get_count} | sudo mysql -p -u root hbnb_dev_db')

        command = 'echo \'create State name="California"\''
        user = f"HBNB_MYSQL_USER={getenv('HBNB_MYSQL_USER')}"
        pwd = f"HBNB_MYSQL_PWD={getenv('HBNB_MYSQL_PWD')}"
        host = f"HBNB_MYSQL_HOST={getenv('HBNB_MYSQL_HOST')}"
        db = f"HBNB_MYSQL_DB={getenv('HBNB_MYSQL_DB')}"
        s_type = "HBNB_TYPE_STORAGE=db"

        system(f'{command} | {user} {pwd} {host} {db} {s_type} ./console.py')

        final = getoutput(f'{get_count} | sudo mysql -p -u root hbnb_dev_db')

        self.assertGreater(
            int(final.split("\n")[1]), int(initial.split("\n")[1])
        )
