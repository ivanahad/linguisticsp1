#!/usr/bin/env python3
# Utility methods to check if a line is an ingredient
# and to exctract it's quantiy, unit and name.
import regex
import unit


def line_to_ingredient(line):
    ingredient = regex.simpleregex(line.strip())
    if not ingredient:
        return None
    add_standardized_metric(ingredient)
    return ingredient


def add_standardized_metric(ingredient):
    metric_u = unit.convertName(ingredient["unit"])
    if metric_u:
        ingredient["metric_u"] = metric_u
        qty = unit.convert_fraction(ingredient["quantity"])
        metric_q = qty * unit.convertQuantity(ingredient["unit"])
        ingredient['metric_q'] = metric_q
