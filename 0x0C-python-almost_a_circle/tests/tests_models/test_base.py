#!/usr/bin/python3
"""
Module test_base.py

This module will be described below
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """in this class the methods of the base class will be tested"""

    def setUp(self):
        """this method will run before each test methods
            this method will set up resources before each test
        """
        self.bs = Base()
        self.rt = Rectangle(1, 2, 3, 4)
        self.sq = Square(5)

    def tearDown(self):
        """this method will run after each test method
            this method will clean up resources after each test
        """
        del self.bs
        del self.rt
        del self.sq

    def test_init(self):
        """this method will test the init method of the Base class
        For Example: bs = self.bs() #we create instace 
                    print(bs.id) #must print 1
                    bl = self.bs(34) must print 34
        """
        bs = self.bs
        self.assertEqual(bs.id, 1)
        bs.id = 43
        self.assertEqual(bs.id, 43)
