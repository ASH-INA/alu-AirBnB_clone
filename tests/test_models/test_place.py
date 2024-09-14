#!/usr/bin/python3
""" Defines tests for the Place model"""

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import time

class TestPlace(unittest.TestCase):
    """Test cases for the Place model"""

    def setUp(self):
        """Set up for the tests"""
        self.place = Place(name="Beach House")
        self.place.save()

    def test_instance(self):
        """Test that Place is an instance of Place and BaseModel"""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_initial_attributes(self):
        """Test initial attributes of Place"""
        self.assertEqual(self.place.name, "Beach House")

    def test_default_attributes(self):
        """Test default attributes of Place"""
        place = Place()
        self.assertEqual(place.name, "")

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.place.updated_at
        time.sleep(1)  # Ensure the update happens after the save call
        self.place.save()
        self.assertGreater(self.place.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], 'Beach House')
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)

    def test_str_method(self):
        """Test the __str__ method"""
        place_str = str(self.place)
        self.assertIn('[Place]', place_str)
        self.assertIn(f'({self.place.id})', place_str)
        self.assertIn(f"'{self.place.name}'", place_str)

if __name__ == '__main__':
    unittest.main()
