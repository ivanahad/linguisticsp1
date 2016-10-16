#!/usr/bin/env python3
# Parse an html to extract ingredients.
from html import parser
import ingredients


class IngredientsHTMLParser(parser.HTMLParser):
    def __init__(self):
        self.list_ingredients = []
        self.in_ingredient_box = False
        self.finish = False
        super().__init__()

    def handle_data(self, data):
        self.check_if_outside_ingredient_box(data)

        ingredient = self.get_ingredient(data)

        if not self.discard_ingredient(ingredient):
            self.list_ingredients.append(ingredient)

        self.check_if_in_ingredient_box(data)

    def get_ingredient(self, data):
        if self.in_ingredient_box:
            return ingredients.line_to_ingredient_unsafe(data)
        return ingredients.line_to_ingredient_safe(data)

    def check_if_in_ingredient_box(self, data):
        if len(data) < 25:
            if "ingredient" in data.lower():
                self.in_ingredient_box = True

    def check_if_outside_ingredient_box(self, data):
        if len(data) < 25:
            if "instruction" in data.lower() or "direction" in data.lower() or "procedure" in data.lower():
                self.in_ingredient_box = False
                self.finish = True

    @staticmethod
    def discard_ingredient(ingredient):
        if not ingredient:
            return True
        if len(ingredient["ingredient"]) < 3:
            return True
        return False


def parse_whole_file(file_to_parse):
    ingredients_parser = IngredientsHTMLParser()
    for line in file_to_parse:
        ingredients_parser.feed(line)
        if ingredients_parser.finish:
            break
    return ingredients_parser.list_ingredients

