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
          'centimeter',
          'chunk',
          'slice',
          'chunk',
          'bag',
          'box',
          'dash',
          'can',
          'drop',
          'scoop',
          'fillet',
          'pack',
          'package',
          'tube',
          'handful',
          'pinch',
          'bunch']

dicoUnits = ['grams',
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
        if (unit.lower() == 'fluid ounce' or unit.lower() == 'fluid ounces' or
            unit.lower() == 'fl oz' or unit.lower() == 'fl ounce' or unit.lower() == 'fl ounces'):
            return 'fluid ounce'
        elif (unit.lower() == 'ounce' or unit.lower() == 'ounces' or unit.lower() == 'oz' or unit.lower() == 'oz.'):
            return 'ounce'
        elif(unit.lower() == 'lb' or unit.lower()=='lbs' or unit.lower() == 'pound' or unit.lower()=='pounds'): #pounds en gram
            return 'pound'
        elif(unit.lower() == 'inch' or unit.lower()=='inches'):#inches in centimeters
            return 'inch'
        elif(unit.lower()=='cup' or or unit.lower()=='c' or unit.lower() == 'cups' or unit.lower() == 'c.'):
            return 'cup'
        elif(unit.lower()=='tablespoon' or unit.lower()=='tablespoons' or unit.lower() == 'tbsp' or unit.lower() == 'tbsp.'):
            return 'tablespoon'
        elif (unit.lower() == 'teaspoon' or unit.lower() == 'teaspoons' or unit.lower() == 't' or unit.lower() == 'tsp' or unit.lower() == 'tsp.'
              or unit.lower() == 't.' or unit.lower() == 'tb' or unit.lower() == 'tb.'):
            return 'teaspoon'
        elif (unit.lower() == 'g.' or unit.lower()=='g'):
            return 'gram'
        else:
            return unit
# returns the new quantity after conversion
# inutile?
def convertQuantity(unit):
    if unit in dicoUnits:
        if (unit.lower() == 'fluid ounce' or unit.lower() == 'fluid ounces'):
            return 0.0295735
        elif (unit.lower() == 'ounce' or unit.lower() == 'ounces'):
            return 28.3495
        elif(unit.lower() == 'pound' or unit.lower()=='pounds'): #pounds en gram
            return 453.592
        elif(unit.lower() == 'inch' or unit.lower()=='inches'):#inches in centimeters
            return 2.54
        elif(unit.lower()=='cup' or unit.lower() == 'cups'):
            return 236.59
        elif(unit.lower()=='tablespoon' or unit.lower()=='tablespoons'):
            return 15
        elif (unit.lower() == 'teaspoon' or unit.lower() == 'teaspoons'):
            return 5
    return 1


#returns the standard unit after conversion. If it is already a standard unit, return same unit.
def convertName(unit):
    if unit in dicoUnits:
        if(unit.lower() == 'ounce' or unit.lower()=='ounces' or unit.lower()=='kilograms' or unit.lower()=='kilogram'
           or unit.lower() == 'g'):
            return 'grams'
        elif(unit.lower() == 'fluid ounce' or unit.lower()=='fluid ounces'):
            return 'liters'
        elif (unit.lower() == 'pound' or unit.lower()=='pounds'
              or unit.lower() == 'cup' or unit.lower() == 'cups'
              or unit.lower() == 'tablespoons' or unit.lower()=='tablespoon'
              or unit.lower() == 'teaspoon' or unit.lower() == 'teaspoons'):
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


#methode convertissant les vulgar fractions?
#1-2 quantity?
#parfois quantity = '3.'
#15-ounce
#500g = quantity
#retirer "of"
#1 1/2 - 2
#methode qui retire le point à la fin de la unit?
