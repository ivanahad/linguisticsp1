#!/usr/bin/env python3
import re


simple = r"-?(?P<quantity>\d+(\/\d+)?) (?P<unit>\w+\.?) (?P<element>.+)"  # quantity - unit - element
only_element = r'-?(?P<element>.+)'  # element
or_regex = r"|"


def match(line, pattern):
    p = re.compile(pattern)
    return p.match(line)


def simple_regex(line):
    result = match(line, simple)
    return {"ingredient": result.group("element"), "quantity": result.group("quantity"),
            "unit": result.group("unit")} if result else None


def only_element_regex(line):
    result = match(line, only_element)
    return {"ingredient": result.group("element")} if result else None


def advanced_regex(line):
    result = simple_regex(line)
    return result if result else only_element_regex(line)

