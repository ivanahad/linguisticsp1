#!/usr/bin/env python3
# Extract ingredients from an html recipe page and output it into a yaml file.
# Usage: - ./digest.py path/to/input.html path/to/output.yaml
import sys
from os import listdir
from os.path import isfile, join
import yaml

ingredients = {}
quantities = {}
units = {}
empty_files = 0


def main(args):
    input_dir = args[1]
    files = get_files(input_dir)
    compute_statistics(files)
    print("Number of ingredients : " + str(len(ingredients)))
    print("Number of units : " + str(len(units)))
    print("Number of quantities : " + str(len(quantities)))
    print("Number of empty files : " + str(empty_files))


def get_files(dir_path):
    files = [dir_path+f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    return files


def compute_statistics(files):
    for file in files:
        with open(file, "r") as f:
            data = yaml.load(f)
            add_stat_from_data(data)


def add_stat_from_data(data):
    if not data:
        empty_files += 1
        return
    for ingredient in data:
        add_ingredient(ingredient)
        add_unit(ingredient)
        add_quantity(ingredient)


def add_ingredient(ingredient):
    element = ingredient["ingredient"]
    if element in ingredients:
        ingredients[element] += 1
    else:
        ingredients[element] = 1


def add_unit(ingredient):
    unit = ingredient.get("unit")
    if unit:
        if unit in units:
            units[unit] += 1
        else:
            units[unit] = 1


def add_quantity(ingredient):
    qty = ingredient.get("quantity")
    if qty:
        if qty in quantities:
            quantities[qty] += 1
        else:
            quantities[qty] = 1


arguments = sys.argv
main(arguments)
