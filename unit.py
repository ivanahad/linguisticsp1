#!/usr/bin/env python3

# represente toutes les unites

# stocker les valeurs plurielles aussi?
solid = {'gram' : 1,
         'kilogram' : 1000,
         'ounce' : 28.3495,
         'tablespoon' : 15,
         'teaspoon': 5,
         'pound' : 453.592,
         'cup' : 236.59
        }

liquid = {
        'liter' : 1,
        'fluid ounce' : 0.0295735,
        'milliliter' : 0.001
         }

others = ['inch',
          'inches',
          'centimeter',
          'chunk',
          'slice',
          'slices',
          'chunk',
          'chunks',
          'piece',
          'pieces',
          'bag',
          'bags',
          'box',
          'boxes',
          'dash',
          'can',
          'cans',
          'drop',
          'drops',
          'scoop',
          'scoops',
          'fillet',
          'fillets',
          'pack',
          'packs',
          'package',
          'packages',
          'tube',
          'tubes',
          'handful',
          'pinch',
          'bunch']

tablespoon = ['tablespoon', 'tablespoons', 'tbsp', 'tbsp.', 'tbs', 'tbs.', 'T', 'tb.', 'tb', 'tbl', 'tbl.']
teaspoon = ['tsp', 'tsp.', 'ts', 'ts.', 'teaspoon', 'teaspoons']
pound = ['pound', 'pounds', 'lb', 'lbs', 'lb.', 'lbs.']
gram = ['gram', 'grams', 'g.', 'g']
kilogram = ['kilogram', 'kilograms', 'kilo', 'kilos', 'kilo.', 'kg.', 'kg']
ounce = ['ounce', 'ounces', "oz", "oz."]
fluid_ounce = ['fluid ounce', 'fluid ounces', 'fl ounce','fl ounces','fl oz', 'fl. ounce', 'fl. oz', 'fl ounces']
cup = ['cup', 'cups', 'C', 'c', 'c.']


# standardizes the name of the unit. Ex : t., tsp, 't', 'teaspoons' = teaspoon.
# d'abord verifier si dans dictionnaire avant d'utiliser cette methode
def convert_name_unit(unit):
        if unit.lower() in fluid_ounce:
            return 'fluid ounce'
        elif unit.lower() in ounce:
            return 'ounce'
        elif unit.lower() in pound:
            return 'pound'
        elif unit.lower() in cup:
            return 'cup'
        elif unit == 'T' or unit.lower() in tablespoon:
            return 'tablespoon'
        elif unit.lower() in teaspoon:
            return 'teaspoon'
        elif unit.lower() in gram:
            return 'gram'
        elif unit.lower() in others:
            return unit
        else:
            return None


def get_conversion_rate(unit):
    result = solid.get(unit, None)
    if not result:
        result = liquid.get(unit, None)
    return result


def get_conversion_metric(unit):
    if unit in solid.keys():
        return "gram"
    elif unit in liquid.keys():
        return "liter"
    return None


def is_a_unit(unit):
    if unit in solid.keys():
        return True
    elif unit in liquid.keys():
        return True
    elif unit in others:
        return True
    return False


# fraction is a string. Returns the float value of a string of the form "X/Y"
def convert_fraction(fraction):
    if '/' in fraction:
        operands = fraction.split("/")
        return int(operands[0]) / int(operands[1])
    return int(fraction)


# returns a tuple with the standardized unit and the according quantity
def get_converted_qty(unit, qty):
    quantity = remove_fraction_quantity(qty)
    conversion_rate = get_conversion_rate(unit)
    new_quantity = float(quantity) * conversion_rate
    return new_quantity


# if the quantity is of the form "X Z/Y", returns the equivalent float
def remove_fraction_quantity(quantity):
    operands = quantity.split(" ")
    if len(operands) == 2:
        operandone = convert_fraction(operands[0])
        operandtwo = convert_fraction(operands[1])
        new_quantity = operandone + operandtwo
        return new_quantity
    return convert_fraction(quantity)
