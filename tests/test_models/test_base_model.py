#!/usr/bin/python3
# Unittests for the base model.

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)

if __name__ == "__main__":
    unittest.main()
