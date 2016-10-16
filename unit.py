#!/usr/bin/env python3

#represente toutes les unites

#takes a unit as an argument and converts it
dicoUnits = ['grams', 'gram', 'kilo', 'kilos', 'kilogram', 'kilograms' 'slices','pound', 'pounds', 'lb', 'tbsp', 'tablespoon', 'tablespoons' 'tsp', 'teaspoon','teaspoons', 'cup', 'cups',
             'inch', 'inches', 'piece', 'pieces' 'slice', 'slices' 'ounce', 'ounces', 'fluid ounce', 'fluid ounces', 'fl ounce', 'fl ounces', 'fl oz'
             'oz', 'chunk', 'chunks', 'bag', 'bags', 'box', 'boxes', 'dash', 'can', 'drop', 'drops', 'scoop', 'scoops', 'fillet', 'fillets', 'liter', 'liters', 'C', 'T', 't']

#returns the new quantity after conversion
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
    else:
        return 1

#returns the standard unit after conversion. If it is already a standard unit, return same unit.
#ajouter T, C, et t
def convertName(unit):
    if unit in dicoUnits:
        if(unit.lower() == 'ounce' or unit.lower()=='ounces' or unit.lower()=='oz' or unit.lower()=='kilograms' or unit.lower()=='kilogram'):
            return 'grams'
        elif(unit.lower() == 'fluid ounce' or unit.lower()=='fluid ounces' or unit.lower()=='fl oz' or unit.lower()=='fl ounce' or unit.lower()=='fl ounces'):
            return 'liters'
        elif (unit.lower() == 'lb' or unit.lower()=='lbs' or unit.lower() == 'pound' or unit.lower()=='pounds'):
            return 'grams'
        elif (unit.lower() == 'inch' or unit.lower()=='inches'):
            return 'centimeters'
        else:
            return unit
    else:
        return None

#tells if a word is indeed a unit. Used to test if a line of ingredient contains a unit.
def isInDico(unit):
    for element in dicoUnits:
        if unit.lower() in element.lower():
            return True
    return False