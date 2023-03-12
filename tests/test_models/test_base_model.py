#!/usr/bin/python3
"""
Module for BaseModel class test cases
"""
import unittest
import time
from datetime import datetime

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """unittest for the BaseModel class"""
    def setUp(self):
        """sets up test methods"""
        pass

    def tearDown(self):
        """tears down test methods"""
        pass

    def test_docstring_BaseModel(self):
        """checks if docstrings are present"""
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)


if __name__ == '__main__':
    unittest.main()
