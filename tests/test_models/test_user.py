#!/usr/bin/python3
"""Testing for User"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testuser(unittest.TestCase):

    def test_pep8_conformance_user(self):
        """Testing that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_User(self):
        """
        Testing attributes of Class Use
        """
        my_user = User()
        my_user.first_name = 'Chiemerie'
        my_user.last_name = 'Obi'
        my_user.email = 'Obiwinner94@gmail.com'
        self.assertEqual(my_user.first_name, 'Chiemerie')
        self.assertEqual(my_user.last_name, 'Obi')
        self.assertEqual(my_user.email, 'obiwinner94@gmail.com')
