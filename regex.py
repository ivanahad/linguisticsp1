#!/usr/bin/env python3
import re


#classic = r"-(?P<quantity>\d+(\\d+)?) (?P<unit>\w+) (?P<element>.+)"

classic = r"-?(?P<quantity>\d+(\/\d+)?) (?P<unit>\w+\.?) (?P<element>.+)"

def simpleregex(line):
    p = re.compile(classic)
    match = p.match(line)
    if not match:
        return None
    result = match.group()
    return {"ingredient": match.group("element"), "quantity": match.group("quantity"), "unit": match.group("unit"),
            "line": line}

