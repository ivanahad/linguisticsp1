#!/usr/bin/env python3
# Extract ingredients from an html recipe page and output it into a yaml file.
# Usage: - ./digest.py path/to/input.html path/to/output.yaml

import sys
import html_parser


def main(args):
    input = args[1]
    output = args[2]

    extract_ingredients(input)


def extract_ingredients(input):
    with open(input, "r") as input_file:
        html_parser.parse_all_file(input_file)

arguments = sys.argv
main(arguments)
