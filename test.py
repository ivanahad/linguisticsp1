#!/usr/bin/env python3

import unittest
import unit

class TestUnitMethods(unittest.TestCase):
    def test_isInDico(self):
        element1 = 'inch'
        self.assertTrue(unit.isInDico(element1))

    def test_convertName(self):
        element = 'inch'
        element1 = 'lb'
        element2 = "fluid ounce"
        element3 = "gram"
        self.assertEqual(unit.convertName(element), 'centimeters')
        self.assertEqual(unit.convertName(element1), 'grams')
        self.assertEqual(unit.convertName(element2), 'liters')
        self.assertEqual(unit.convertName(element3), 'gram')

    def test_convertQuantity(self):
        element = 'inch'
        element1 = 'lb'
        self.assertEqual(unit.convertQuantity(element), 2.54)
        self.assertEqual(unit.convertQuantity(element1), 453.592)