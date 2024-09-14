#!/usr/bin/python3
""" Defines tests for the city model """

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import time

class TestCity(unittest.TestCase):
    """Test cases for the City model"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City(name="San Francisco")
        self.city.save()

    def test_instance(self):
        """Test that City is an instance of City and BaseModel"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_initial_attributes(self):
        """Test initial attributes of City"""
        self.assertEqual(self.city.name, "San Francisco")

    def test_default_attributes(self):
        """Test default attributes of City"""
        city = City()
        self.assertEqual(city.name, "")

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.city.updated_at
        time.sleep(1)  # Ensure the update happens after the save call
        self.city.save()
        self.assertGreater(self.city.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], 'San Francisco')
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    def test_str_method(self):
        """Test the __str__ method"""
        city_str = str(self.city)
        self.assertIn('[City]', city_str)
        self.assertIn(f'({self.city.id})', city_str)
        self.assertIn(f"'{self.city.name}'", city_str)

if __name__ == '__main__':
    unittest.main()
