#!/usr/bin/env python3
# Parse an html to extract ingredients.
from html import parser
import ingredients


class IngredientsHTMLParser(parser.HTMLParser):
    def handle_data(self, data):
        if not ingredients.is_not_an_ingredient(data):
            print("Data: " + data) # TODO check if is ingredient


def parse_all_file(file_to_parse):
    ingredients_parser = IngredientsHTMLParser()
    for line in file_to_parse:
        ingredients_parser.feed(line)

