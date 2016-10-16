#!/usr/bin/env python3
import html_parser
import yaml


def extract_ingredients(input_file):
    with open(input_file, "r") as f:
        return html_parser.parse_whole_file(f)


def ingredients_to_yaml(ingredients, output_file):
    with open(output_file, "w") as f:
        yaml.dump(ingredients, f)
