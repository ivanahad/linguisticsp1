#!/usr/bin/env python3
# Utility methods to check if a line is an ingredient
# and to exctract it's quantiy, unit and name.


def is_not_an_ingredient(line):
    line = line.strip()
    if len(line) < 4 or len(line) > 100:
        return True
    return False




