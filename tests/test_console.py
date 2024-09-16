#!/usr/bin/python3
# Defines unittests for console.py.

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand class."""

    def setUp(self):
        """Set up the test environment."""
        self.cmd = HBNBCommand()
        self.mock_storage_all = patch('models.storage.all', return_value={})
        self.mock_storage_save = patch('models.storage.save')
        self.mock_storage_new = patch('models.storage.new')
        self.mock_storage_reload = patch('models.storage.reload')

        self.mock_storage_all.start()
        self.mock_storage_save.start()
        self.mock_storage_new.start()
        self.mock_storage_reload.start()

    def tearDown(self):
        """Tear down the test environment."""
        self.mock_storage_all.stop()
        self.mock_storage_save.stop()
        self.mock_storage_new.stop()
        self.mock_storage_reload.stop()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test the create command."""
        with patch('builtins.eval', return_value=BaseModel):
            self.cmd.onecmd('create BaseModel')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)  # Ensure an ID is printed

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test the show command."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'show BaseModel {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[BaseModel] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test the destroy command."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'destroy BaseModel {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        storage.all.assert_not_called()  # Ensure no extra calls

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test the all command."""
        instance = BaseModel()
        storage.all = MagicMock(return_value={f"BaseModel.{instance.id}": instance})
        self.cmd.onecmd('all BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[BaseModel] ({instance.id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test the count command."""
        instance = BaseModel()
        storage.all = MagicMock(return_value={f"BaseModel.{instance.id}": instance})
        self.cmd.onecmd('count BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test the update command."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'update BaseModel {instance_id} name "New Name"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.name, "New Name")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_dict(self, mock_stdout):
        """Test the update command with dictionary."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'update BaseModel {instance_id} {{"name": "New Name"}}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.name, "New Name")

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_command(self, mock_stdout):
        """Test handling of an invalid command."""
        self.cmd.onecmd('invalid_command')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "*** Unknown syntax: invalid_command")

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line(self, mock_stdout):
        """Test handling of an empty line."""
        self.cmd.onecmd('')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # No output should be produced

    # Tests for specific models

    def test_show_instance_not_found(self):
        """Test 'show' command when instance is not found."""
        self.cmd.onecmd('show User 12345')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_destroy_instance_not_found(self):
        """Test 'destroy' command when instance is not found."""
        self.cmd.onecmd('destroy User 12345')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '** no instance found **')

    def test_count_no_instances(self):
        """Test 'count' command when no instances exist."""
        storage.all = MagicMock(return_value={})
        self.cmd.onecmd('count User')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '0')

    def test_update_non_existent_instance(self):
        """Test 'update' command with a non-existent instance."""
        self.cmd.onecmd('update User 12345 name "Updated Name"')
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '** no instance found **')


if __name__ == '__main__':
    unittest.main()
