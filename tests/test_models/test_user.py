#!/usr/bin/python3
"""Defines tests for the User Model"""

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import time

class TestUser(unittest.TestCase):
    """Test cases for the User model"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User(email="user@example.com", password="securepassword")
        self.user.save()

    def test_instance(self):
        """Test that User is an instance of User and BaseModel"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_initial_attributes(self):
        """Test initial attributes of User"""
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "securepassword")

    def test_default_attributes(self):
        """Test default attributes of User"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.user.updated_at
        time.sleep(1)  # Ensure the update happens after the save call
        self.user.save()
        self.assertGreater(self.user.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'user@example.com')
        self.assertEqual(user_dict['password'], 'securepassword')
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_str_method(self):
        """Test the __str__ method"""
        user_str = str(self.user)
        self.assertIn('[User]', user_str)
        self.assertIn(f'({self.user.id})', user_str)
        self.assertIn(f"'{self.user.email}'", user_str)
        self.assertIn(f"'{self.user.password}'", user_str)

if __name__ == '__main__':
    unittest.main()
