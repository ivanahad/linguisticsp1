#!/usr/bin/env python3
# Utility methods to check if a line is an ingredient
# and to exctract it's quantiy, unit and name.
import regex


def line_to_ingredient(line):
    ingredient = regex.simpleregex(line.strip())
    return ingredient




