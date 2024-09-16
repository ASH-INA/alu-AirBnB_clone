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

    # Count Tests

    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_count(self, mock_stdout):
        """Test BaseModel count command."""
        instance = BaseModel()
        storage.all = MagicMock(return_value={f"BaseModel.{instance.id}": instance})
        self.cmd.onecmd('count BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_User_count(self, mock_stdout):
        """Test User count command."""
        instance = User()
        storage.all = MagicMock(return_value={f"User.{instance.id}": instance})
        self.cmd.onecmd('count User')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_State_count(self, mock_stdout):
        """Test State count command."""
        instance = State()
        storage.all = MagicMock(return_value={f"State.{instance.id}": instance})
        self.cmd.onecmd('count State')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_City_count(self, mock_stdout):
        """Test City count command."""
        instance = City()
        storage.all = MagicMock(return_value={f"City.{instance.id}": instance})
        self.cmd.onecmd('count City')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_Amenity_count(self, mock_stdout):
        """Test Amenity count command."""
        instance = Amenity()
        storage.all = MagicMock(return_value={f"Amenity.{instance.id}": instance})
        self.cmd.onecmd('count Amenity')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_Place_count(self, mock_stdout):
        """Test Place count command."""
        instance = Place()
        storage.all = MagicMock(return_value={f"Place.{instance.id}": instance})
        self.cmd.onecmd('count Place')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    @patch('sys.stdout', new_callable=StringIO)
    def test_Review_count(self, mock_stdout):
        """Test Review count command."""
        instance = Review()
        storage.all = MagicMock(return_value={f"Review.{instance.id}": instance})
        self.cmd.onecmd('count Review')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Show Tests

    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_show(self, mock_stdout):
        """Test BaseModel show command."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'show BaseModel {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[BaseModel] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_User_show(self, mock_stdout):
        """Test User show command."""
        instance = User()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"User.{instance_id}": instance})
        self.cmd.onecmd(f'show User {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[User] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_State_show(self, mock_stdout):
        """Test State show command."""
        instance = State()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"State.{instance_id}": instance})
        self.cmd.onecmd(f'show State {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[State] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_City_show(self, mock_stdout):
        """Test City show command."""
        instance = City()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"City.{instance_id}": instance})
        self.cmd.onecmd(f'show City {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[City] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_Amenity_show(self, mock_stdout):
        """Test Amenity show command."""
        instance = Amenity()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Amenity.{instance_id}": instance})
        self.cmd.onecmd(f'show Amenity {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[Amenity] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_Place_show(self, mock_stdout):
        """Test Place show command."""
        instance = Place()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Place.{instance_id}": instance})
        self.cmd.onecmd(f'show Place {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[Place] ({instance_id}", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_Review_show(self, mock_stdout):
        """Test Review show command."""
        instance = Review()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Review.{instance_id}": instance})
        self.cmd.onecmd(f'show Review {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[Review] ({instance_id}", output)

    # Destroy Tests

    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_destroy(self, mock_stdout):
        """Test BaseModel destroy command."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'destroy BaseModel {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"BaseModel.{instance_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_User_destroy(self, mock_stdout):
        """Test User destroy command."""
        instance = User()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"User.{instance_id}": instance})
        self.cmd.onecmd(f'destroy User {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"User.{instance_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_City_destroy(self, mock_stdout):
        """Test City destroy command."""
        instance = City()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"City.{instance_id}": instance})
        self.cmd.onecmd(f'destroy City {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"City.{instance_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_State_destroy(self, mock_stdout):
        """Test State destroy command."""
        instance = State()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"State.{instance_id}": instance})
        self.cmd.onecmd(f'destroy State {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"State.{instance_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_Place_destroy(self, mock_stdout):
        """Test Place destroy command."""
        instance = Place()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Place.{instance_id}": instance})
        self.cmd.onecmd(f'destroy Place {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"Place.{instance_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_Amenity_destroy(self, mock_stdout):
        """Test Amenity destroy command."""
        instance = Amenity()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Amenity.{instance_id}": instance})
        self.cmd.onecmd(f'destroy Amenity {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"Amenity.{instance_id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_Review_destroy(self, mock_stdout):
        """Test Review destroy command."""
        instance = Review()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Review.{instance_id}": instance})
        self.cmd.onecmd(f'destroy Review {instance_id}')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Destroy command should not print anything
        self.assertNotIn(f"Review.{instance_id}", storage.all())

    # Update Tests

    @patch('sys.stdout', new_callable=StringIO)
    def test_BaseModel_update(self, mock_stdout):
        """Test BaseModel update command."""
        instance = BaseModel()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"BaseModel.{instance_id}": instance})
        self.cmd.onecmd(f'update BaseModel {instance_id} name "Updated Name"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.name, "Updated Name")

    @patch('sys.stdout', new_callable=StringIO)
    def test_User_update(self, mock_stdout):
        """Test User update command."""
        instance = User()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"User.{instance_id}": instance})
        self.cmd.onecmd(f'update User {instance_id} last_name "Doe"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.last_name, "Doe")

    @patch('sys.stdout', new_callable=StringIO)
    def test_State_update(self, mock_stdout):
        """Test State update command."""
        instance = State()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"State.{instance_id}": instance})
        self.cmd.onecmd(f'update State {instance_id} name "Updated State"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.name, "Updated State")

    @patch('sys.stdout', new_callable=StringIO)
    def test_City_update(self, mock_stdout):
        """Test City update command."""
        instance = City()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"City.{instance_id}": instance})
        self.cmd.onecmd(f'update City {instance_id} name "Updated City"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.name, "Updated City")

    @patch('sys.stdout', new_callable=StringIO)
    def test_Place_update(self, mock_stdout):
        """Test Place update command."""
        instance = Place()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Place.{instance_id}": instance})
        self.cmd.onecmd(f'update Place {instance_id} description "Updated Description"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.description, "Updated Description")

    @patch('sys.stdout', new_callable=StringIO)
    def test_Amenity_update(self, mock_stdout):
        """Test Amenity update command."""
        instance = Amenity()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Amenity.{instance_id}": instance})
        self.cmd.onecmd(f'update Amenity {instance_id} name "Updated Amenity"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.name, "Updated Amenity")

    @patch('sys.stdout', new_callable=StringIO)
    def test_Review_update(self, mock_stdout):
        """Test Review update command."""
        instance = Review()
        instance_id = instance.id
        storage.all = MagicMock(return_value={f"Review.{instance_id}": instance})
        self.cmd.onecmd(f'update Review {instance_id} text "Updated Review Text"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')  # Update command should not print anything
        self.assertEqual(instance.text, "Updated Review Text")

if __name__ == '__main__':
    unittest.main()
