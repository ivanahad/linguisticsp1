#!/usr/bin/env python3

# represente toutes les unites

# takes a unit as an argument and converts it
dicoUnits = ['grams',
             'gram',
             'kilo',
             'kilos',
             'kilogram',
             'kilograms',
             'slices',
             'pound',
             'pounds',
             'lb',
             'tbsp',
             'tablespoon',
             'tablespoons',
             'tsp',
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
             'chunk',
             'chunks',
             'bag',
             'bags',
             'box',
             'boxes',
             'dash',
             'can',
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
             'T',
             't']


# returns the new quantity after conversion
def convertQuantity(unit):
    if unit in dicoUnits:
        if (unit.lower() == 'fluid ounce' or unit.lower() == 'fluid ounces' or
            unit.lower() == 'fl oz' or unit.lower() == 'fl ounce' or unit.lower() == 'fl ounces'):
            return 0.0295735
        elif (unit.lower() == 'ounce' or unit.lower() == 'ounces' or unit.lower() == 'oz'):
            return 28.3495
        elif(unit.lower() == 'lb' or unit.lower()=='lbs' or unit.lower() == 'pound' or unit.lower()=='pounds'): #pounds en gram
            return 453.592
        elif(unit.lower() == 'inch' or unit.lower()=='inches'):#inches in centimeters
            return 2.54
        elif(unit.lower()=='cup' or unit.lower()=='C' or unit.lower()=='c' or unit.lower() == 'cups'):
            return 236.59
        elif(unit.lower()=='tablespoon' or unit.lower()=='tablespoons' or unit.lower()=='T' or unit.lower() == 'tbsp' or unit.lower() == 'tbsp.'):
            return 15
        elif (unit.lower() == 'teaspoon' or unit.lower() == 'teaspoons' or unit.lower() == 't' or unit.lower() == 'tsp' or unit.lower() == 'tsp.'):
            return 5
    return 1


#returns the standard unit after conversion. If it is already a standard unit, return same unit.
def convertName(unit):
    if unit in dicoUnits:
        if(unit.lower() == 'ounce' or unit.lower()=='ounces' or unit.lower()=='oz' or unit.lower()=='kilograms' or unit.lower()=='kilogram'):
            return 'grams'
        elif(unit.lower() == 'fluid ounce' or unit.lower()=='fluid ounces' or unit.lower()=='fl oz' or unit.lower()=='fl ounce' or unit.lower()=='fl ounces'):
            return 'liters'
        elif (unit.lower() == 'lb' or unit.lower()=='lbs' or unit.lower() == 'pound' or unit.lower()=='pounds'
              or unit.lower() == 'cup' or unit.lower() == 'cups' or unit.lower()=='C' or unit.lower()=='c'
              or unit.lower() == 'tablespoons' or unit.lower()=='tablespoon' or unit.lower()=='T' or unit.lower() == 'tbsp' or unit.lower() == 'tbsp.'
              or unit.lower() == 'teaspoon' or unit.lower() == 'teaspoons' or unit.lower() == 't' or unit.lower() == 'tsp' or unit.lower() == 'tsp.'):
            return 'grams'
        elif (unit.lower() == 'inch' or unit.lower()=='inches'):
            return 'centimeters'
        else:
            return unit
    else:
        return None


# tells if a word is indeed a unit. Used to test if a line of ingredient contains a unit.
def isInDico(unit):
    for element in dicoUnits:
        if unit.lower() in element.lower():
            return True
    return False


# fraction is a string
def convert_fraction(fraction):
    if '/' in fraction:
        operands = fraction.split("/")
        return int(operands[0]) / int(operands[1])
    return int(fraction)


def get_unit_qty(unit, qty):
    standardized = convertName(unit)
    new_quantity = None
    if qty:
        quantity = convert_fraction(qty)
        new_quantity = quantity * convertQuantity(unit)

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