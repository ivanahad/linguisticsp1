#!/usr/bin/env python3
import unittest
import ingredients


class TestIngredients(unittest.TestCase):
    def test_remove_parenthesis(self):
        line = "Hello"
        output = ingredients.remove_parenthesis(line)
        output_expected = "Hello"
        self.assertEqual(output_expected, output)

        line = "3 or 4 (it depends) eggs"
        output = ingredients.remove_parenthesis(line)
        output_expected = "3 or 4  eggs"
        self.assertEqual(output_expected, output)

        line = "3 or 4 (it depends) eggs (or water) haha"
        output = ingredients.remove_parenthesis(line)
        output_expected = "3 or 4  eggs  haha"
        self.assertEqual(output_expected, output)

    def test_remove_spaces(self):
        line = "Hello"
        output = ingredients.remove_spaces(line)
        output_expected = "Hello"
        self.assertEqual(output_expected, output)

        line = "3 or 4  eggs"
        output = ingredients.remove_spaces(line)
        output_expected = "3 or 4 eggs"
        self.assertEqual(output_expected, output)

        line = "3 or 4  eggs    haha"
        output = ingredients.remove_spaces(line)
        output_expected = "3 or 4 eggs haha"
        self.assertEqual(output_expected, output)
