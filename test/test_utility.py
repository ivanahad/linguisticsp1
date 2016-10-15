#!/usr/bin/env python3
import unittest
import utility
import filecmp
import os


class TestUtility(unittest.TestCase):
    def test_ingredients_to_yaml(self):
        unique_ingredient = [{"ingredient": "apple", "quantity": "1/2"}]

        output_file = "./assets/output1.yaml"
        expected_output_file = "./assets/ingredients_to_yaml_1.yaml"

        utility.ingredients_to_yaml(unique_ingredient, output_file)

        self.assertTrue(filecmp.cmp(output_file, expected_output_file))

        # remove files
        os.remove(output_file)

        multiple_ingredients = [
            {"ingredient": "apple", "quantity": "1/2"},
            {"ingredient": "strawberries", "metric_q": 236.59, "metric_u": "grams", "quantity": 1, "unit": "cup"},
            {"ingredient": "watermelon", "metric_q": 591.47, "metric_u": "grams", "quantity": "2 1/2", "unit":"cup"}]

        output_file = "./assets/output2.yaml"
        expected_output_file = "./assets/ingredients_to_yaml_2.yaml"

        utility.ingredients_to_yaml(multiple_ingredients, output_file)

        self.assertTrue(filecmp.cmp(output_file, expected_output_file))

        # remove files
        os.remove(output_file)
