#!/usr/bin/python3
"""Defines tests for the State model"""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
import time

class TestState(unittest.TestCase):
    """Test cases for the State model"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State(name="California")
        self.state.save()

    def test_instance(self):
        """Test that State is an instance of State and BaseModel"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_initial_attributes(self):
        """Test initial attributes of State"""
        self.assertEqual(self.state.name, "California")

    def test_default_attributes(self):
        """Test default attributes of State"""
        state = State()
        self.assertEqual(state.name, "")

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.state.updated_at
        time.sleep(1)  # Ensure the update happens after the save call
        self.state.save()
        self.assertGreater(self.state.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'California')
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)

    def test_str_method(self):
        """Test the __str__ method"""
        state_str = str(self.state)
        self.assertIn('[State]', state_str)
        self.assertIn(f'({self.state.id})', state_str)
        self.assertIn(f"'{self.state.name}'", state_str)

if __name__ == '__main__':
    unittest.main()
