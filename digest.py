#!/usr/bin/env python3
# Extract ingredients from an html recipe page and output it into a yaml file.
# Usage: - ./digest.py path/to/input.html path/to/output.yaml

import sys
from utility import extract_ingredients


def main(args):
    input = args[1]
    output = args[2]

    extract_ingredients(input)


arguments = sys.argv
main(arguments)
