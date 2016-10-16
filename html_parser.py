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
        if self.in_ingredient_box:
            ingredient = ingredients.line_to_ingredient_strong(data)
        else:
            ingredient = ingredients.line_to_ingredient(data)
        if ingredient:
            self.list_ingredients.append(ingredient)
        self.check_if_in_ingredient_box(data)

    def check_if_in_ingredient_box(self, data):
        if len(data) < 25:
            if "ingredient" in data.lower():
                self.in_ingredient_box = True
            if "instruction" in data.lower() or "direction" in data.lower():
                self.in_ingredient_box = False
                self.finish = True
        return self.in_ingredient_box


def parse_whole_file(file_to_parse):
    ingredients_parser = IngredientsHTMLParser()
    for line in file_to_parse:
        ingredients_parser.feed(line)
        if ingredients_parser.finish:
            break
    return ingredients_parser.list_ingredients

