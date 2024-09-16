#!/usr/bin/python3
# Defines unittests for console.py.

import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.cmd = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        self.assertTrue(self.cmd.do_quit(''))
        self.assertIn("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        self.assertTrue(self.cmd.do_EOF(''))
        self.assertIn("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        """Test help command"""
        self.cmd.onecmd('help')
        output = mock_stdout.getvalue()
        self.assertIn('create', output)
        self.assertIn('show', output)
        self.assertIn('destroy', output)
        self.assertIn('all', output)
        self.assertIn('count', output)
        self.assertIn('update', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        """Test empty line"""
        self.cmd.emptyline()
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_BaseModel(self, mock_stdout, mock_storage_all):
        """Test create BaseModel"""
        self.cmd.onecmd('create BaseModel')
        output = mock_stdout.getvalue()
        self.assertTrue(output.strip())

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_BaseModel(self, mock_stdout, mock_storage_all):
        """Test show BaseModel"""
        self.cmd.onecmd('show BaseModel 1234')
        output = mock_stdout.getvalue()
        self.assertIn('** no instance found **', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_BaseModel(self, mock_stdout, mock_storage_all):
        """Test destroy BaseModel"""
        self.cmd.onecmd('destroy BaseModel 1234')
        output = mock_stdout.getvalue()
        self.assertIn('** no instance found **', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_all_BaseModel(self, mock_stdout, mock_storage_all):
        """Test all BaseModel"""
        self.cmd.onecmd('all BaseModel')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_BaseModel(self, mock_stdout, mock_storage_all):
        """Test update BaseModel"""
        self.cmd.onecmd('update BaseModel 1234 name "New Name"')
        output = mock_stdout.getvalue()
        self.assertIn('** no instance found **', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_all(self, mock_stdout, mock_storage_all):
        """Test BaseModel.all()"""
        self.cmd.onecmd('BaseModel.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_Review_all(self, mock_stdout, mock_storage_all):
        """Test Review.all()"""
        self.cmd.onecmd('Review.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_User_all(self, mock_stdout, mock_storage_all):
        """Test User.all()"""
        self.cmd.onecmd('User.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_State_all(self, mock_stdout, mock_storage_all):
        """Test State.all()"""
        self.cmd.onecmd('State.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_City_all(self, mock_stdout, mock_storage_all):
        """Test City.all()"""
        self.cmd.onecmd('City.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_Amenity_all(self, mock_stdout, mock_storage_all):
        """Test Amenity.all()"""
        self.cmd.onecmd('Amenity.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_Place_all(self, mock_stdout, mock_storage_all):
        """Test Place.all()"""
        self.cmd.onecmd('Place.all()')
        output = mock_stdout.getvalue()
        self.assertIn('[]', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_count(self, mock_stdout, mock_storage_all):
        """Test BaseModel.count()"""
        self.cmd.onecmd('BaseModel.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_User_count(self, mock_stdout, mock_storage_all):
        """Test User.count()"""
        self.cmd.onecmd('User.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_State_count(self, mock_stdout, mock_storage_all):
        """Test State.count()"""
        self.cmd.onecmd('State.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_Place_count(self, mock_stdout, mock_storage_all):
        """Test Place.count()"""
        self.cmd.onecmd('Place.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_City_count(self, mock_stdout, mock_storage_all):
        """Test City.count()"""
        self.cmd.onecmd('City.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_Amenity_count(self, mock_stdout, mock_storage_all):
        """Test Amenity.count()"""
        self.cmd.onecmd('Amenity.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_Review_count(self, mock_stdout, mock_storage_all):
        """Test Review.count()"""
        self.cmd.onecmd('Review.count()')
        output = mock_stdout.getvalue()
        self.assertIn('0', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_show(self, mock_stdout, mock_storage_all):
        """Test BaseModel.show("id")"""
        self.cmd.onecmd('BaseModel.show("1234")')
        output = mock_stdout.getvalue()
        self.assertIn('** no instance found **', output)

    @patch('models.storage.all', return_value={})
    @patch('sys.stdout', new_callable=StringIO)
    def test_User_show(self, mock_stdout, mock_storage_all):
        """Test User.show("id")"""
        self.cmd.onecmd('User.show("1234")')
        output = mock_stdout.getvalue()
        self.assertIn('** no instance


if __name__ == "__main__":
    unittest.main()
