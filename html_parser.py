#!/usr/bin/env python3
# Parse an html to extract ingredients.
from html import parser
import ingredients


class IngredientsHTMLParser(parser.HTMLParser):
    def __init__(self):
        self.list_ingredients = []
        super().__init__()

    def handle_data(self, data):
        ingredient = ingredients.line_to_ingredient(data)
        if ingredient:
            self.list_ingredients.append(ingredient)


def parse_whole_file(file_to_parse):
    ingredients_parser = IngredientsHTMLParser()
    for line in file_to_parse:
        ingredients_parser.feed(line)
    return ingredients_parser.list_ingredients

