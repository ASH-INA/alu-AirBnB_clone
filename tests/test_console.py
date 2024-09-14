#!/usr/bin/python3
"""Defines unittests for console.py."""

import unittest
from unittest.mock import patch, MagicMock
import io
import sys
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand interpreter"""

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()
        self.console.prompt = ""

    def test_do_create(self):
        """Test the do_create command"""
        with patch('models.file_storage.FileStorage') as MockStorage:
            mock_storage = MockStorage.return_value
            mock_storage.all = MagicMock(return_value={})
            mock_storage.save = MagicMock()

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.console.onecmd('create User')
                output = fake_out.getvalue().strip()
                self.assertTrue(output)  # Check if ID is printed

    def test_do_show(self):
        """Test the do_show command"""
        with patch('models.file_storage.FileStorage') as MockStorage:
            mock_storage = MockStorage.return_value
            mock_storage.all = MagicMock(return_value={
                'User.1234': MagicMock(id='1234', to_dict=lambda: {'id': '1234'})
            })

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.console.onecmd('show User 1234')
                output = fake_out.getvalue().strip()
                self.assertIn('User', output)
                self.assertIn('1234', output)

    def test_do_destroy(self):
        """Test the do_destroy command"""
        with patch('models.file_storage.FileStorage') as MockStorage:
            mock_storage = MockStorage.return_value
            mock_storage.all = MagicMock(return_value={
                'User.1234': MagicMock(id='1234', to_dict=lambda: {'id': '1234'})
            })
            mock_storage.delete = MagicMock()

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.console.onecmd('destroy User 1234')
                mock_storage.delete.assert_called_once()
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** instance deleted **')

    def test_do_all(self):
        """Test the do_all command"""
        with patch('models.file_storage.FileStorage') as MockStorage:
            mock_storage = MockStorage.return_value
            mock_storage.all = MagicMock(return_value={
                'User.1234': MagicMock(id='1234', to_dict=lambda: {'id': '1234'}),
                'State.5678': MagicMock(id='5678', to_dict=lambda: {'id': '5678'})
            })

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.console.onecmd('all User')
                output = fake_out.getvalue().strip()
                self.assertIn('1234', output)

    def test_do_update(self):
        """Test the do_update command"""
        with patch('models.file_storage.FileStorage') as MockStorage:
            mock_storage = MockStorage.return_value
            mock_storage.all = MagicMock(return_value={
                'User.1234': MagicMock(id='1234', to_dict=lambda: {'id': '1234'})
            })
            mock_storage.save = MagicMock()

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.console.onecmd('update User 1234 email "user@example.com"')
                mock_storage.save.assert_called_once()
                output = fake_out.getvalue().strip()
                self.assertEqual(output, '** instance updated **')

    def test_do_quit(self):
        """Test the do_quit command"""
        self.assertTrue(self.console.onecmd('quit'))

    def test_do_EOF(self):
        """Test the do_EOF command"""
        self.assertTrue(self.console.onecmd('EOF'))

if __name__ == '__main__':
    unittest.main()
