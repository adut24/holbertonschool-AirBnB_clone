#!/usr/bin/python3
"""Unittest module for Amenity"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """class testing the Amenity class"""

    def test_instance(self):
        """test the creation of an instance"""
        a = Amenity()
        self.assertEqual(a.name, '')
        a.name = 'Betty'
        self.assertEqual(a.name, 'Betty')
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'updated_at'))
        self.assertTrue(issubclass(a.__class__, BaseModel))


if __name__ == '__main__':
    unittest.main()
