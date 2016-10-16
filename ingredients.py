#!/usr/bin/env python3
# Utility methods to check if a line is an ingredient
# and to exctract it's quantiy, unit and name.
import regex
import unit


def line_to_ingredient(line):
    formatted_line = format_line(line)
    ingredient = regex.simple_regex(formatted_line)
    if not ingredient:
        return None
    add_standardized_metric(ingredient)
    return ingredient


def line_to_ingredient_strong(line):
    formatted_line = format_line(line)
    ingredient = regex.advanced_regex(formatted_line)
    if not ingredient:
        return None
    if "unit" in ingredient.keys():
        add_standardized_metric(ingredient)
    return ingredient


def format_line(line):
    new_line = line.strip()
    new_line = remove_parenthesis(new_line)
    new_line = remove_spaces(new_line)
    return new_line


def remove_parenthesis(line):
    in_parenthesis = False
    new_line = ""
    for c in line:
        if c == "(":
            in_parenthesis = True
        if not in_parenthesis:
            new_line = new_line + c
        if c == ")":
            in_parenthesis = False
    return new_line


def remove_spaces(line):
    new_line = ""
    in_spaces = False
    for c in line:
        if c != " ":
            in_spaces = False
        if not in_spaces:
            new_line = new_line + c
        if c == " ":
            in_spaces = True
    return new_line


def add_standardized_metric(ingredient):
    (metric_u, metric_q) = unit.get_unit_qty(ingredient.get("unit", None), ingredient.get("quantity", None))
    if metric_u:
        ingredient["metric_u"] = metric_u
    if metric_q:
        ingredient["metric_q"] = metric_q
