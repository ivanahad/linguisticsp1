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

dicoUnits2 = ['grams',
             'gram',
             'g',
             'kilo',
             'kilos',
             'kilogram',
             'kilograms',
             'slices',
             'pound',
             'pounds',
             'lb',
             'lbs',
             'tbsp',
             'tbsp.',
             'tbs',
             'tbs.',
             'tablespoon',
             'tablespoons',
             'tsp',
             'tsp.',
             'ts',
             'ts.',
             'teaspoon',
             'teaspoons',
             'cup',
             'cups',
             'inch',
             'inches',
             'piece',
             'pieces',
             'slice',
             'slices',
             'ounce',
             'ounces',
             'fluid ounce',
             'fluid ounces',
             'fl ounce',
             'fl ounces',
             'fl oz',
             'oz',
             'oz.',
             'chunk',
             'chunks',
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
             'liter',
             'liters',
             'C',
             'c',
             'c.',
             'C.',
             'T.',
             't.',
             'T',
             't',
             'tb',
             'Tb',
             'tb.',
             'Tb.',
             'TB',
             'TB.',
             'pack',
             'package',
             'tube',
             'handful',
             'pinch',
             'bunch']


# standardizes the name of the unit. Ex : t., tsp, 't', 'teaspoons' = teaspoon.
# d'abord verifier si dans dictionnaire avant d'utiliser cette methode
def convert_name_unit(unit):
        if (unit.lower() in fluid_ounce):
            return 'fluid ounce'
        elif (unit.lower() in ounce):
            return 'ounce'
        elif(unit.lower() in pound): #pounds en gram
            return 'pound'
        elif(unit.lower() in cup):
            return 'cup'
        elif(unit == 'T' or unit.lower() in tablespoon):
            return 'tablespoon'
        elif (unit.lower() in teaspoon):
            return 'teaspoon'
        elif (unit.lower() in gram):
            return 'gram'
        else:
            return unit

# fraction is a string. Returns the float value of a string of the form "X/Y"
def convert_fraction(fraction):
    if '/' in fraction:
        operands = fraction.split("/")
        return int(operands[0]) / int(operands[1])
    return int(fraction)

# returns a tuple with the standardized unit and the according quantity
def get_unit_qty(unit, qty):
    standardized = convertName(unit)
    new_quantity = None
    if qty:
        quantity = remove_fraction_quantity(qty)
        new_quantity = int(quantity) * convertQuantity(unit)

    return (standardized, new_quantity)


# if the quantity is of the form "X Z/Y", returns the equivalent float
def remove_fraction_quantity(quantity):
    operands = quantity.split(" ")
    if len(operands) == 2:
        operandone = convert_fraction(operands[0])
        operandtwo = convert_fraction(operands[1])
        new_quantity = operandone + operandtwo
        return new_quantity
    return quantity
