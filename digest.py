#!/usr/bin/env python3
# Extract ingredients from an html recipe page and output it into a yaml file.
# Usage: - ./digest.py path/to/input.html path/to/output.yaml
import sys
from utility import extract_ingredients, ingredients_to_yaml
from os import listdir
from os.path import isfile, join

RESULTS_DIR = "./result/"

def main(args):
    if len(args) == 2:
        dir_path = args[1]
        extract_from_dir(dir_path)
    elif len(args) == 3:
        input = args[1]
        output = args[2]
        extract_from_file(input, output)


def extract_from_file(input, output):
    ingredients = extract_ingredients(input)
    ingredients_to_yaml(ingredients, output)


def extract_from_dir(dir_path):
    files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    for file in files:
        output_file = RESULTS_DIR + file.replace(".html", ".yaml")
        input_file = dir_path + file
        extract_from_file(input_file, output_file)

arguments = sys.argv
main(arguments)
