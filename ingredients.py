#!/usr/bin/env python3
# Utility methods to check if a line is an ingredient
# and to exctract it's quantiy, unit and name.
import regex
import unit


def line_to_ingredient_safe(line):
    formatted_line = format_line(line)
    ingredient = regex.simple_regex(formatted_line)
    if not ingredient:
        return None
    check_metric(ingredient)
    add_standardized_metric(ingredient)
    return ingredient


def line_to_ingredient_unsafe(line):
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
    metric_u = unit.get_conversion_metric(ingredient.get("unit", None))
    if metric_u:
        ingredient["metric_u"] = metric_u
        metric_q = unit.get_converted_qty(ingredient["unit"], ingredient["quantity"])
        ingredient["metric_q"] = metric_q


def check_metric(ingredient):
    metric = ingredient.get("unit", None)
    if metric and is_not_a_metric(ingredient):
        not_a_metric(ingredient)


def is_not_a_metric(ingredient):
    metric = unit.convert_name_unit(ingredient["unit"])
    if metric:
        ingredient["unit"] = metric
        return False
    return True


def not_a_metric(ingredient):
    ingredient["ingredient"] = ingredient.pop("unit") + " " + ingredient["ingredient"]
