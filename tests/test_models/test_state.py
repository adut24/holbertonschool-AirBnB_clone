#!/usr/bin/python3
"""Unittest module for State"""
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """class testing the State class"""

    def test_init(self):
        """test the creation of an instance"""
        a = State()
        self.assertEqual(a.name, '')
        a.name = 'Betty'
        self.assertEqual(a.name, 'Betty')
        self.assertTrue(issubclass(a.__class__, BaseModel))
