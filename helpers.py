alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

alphabet_upper = alphabet_lower.upper()

def alphabet_possition(string):

    for character in string:

        value = character.lower()

        return alphabet_lower.index(value)

def rotate_character(character, rotation):

    value = ""

    rotation = (alphabet_possition(character) + rotation) % 26

    if character.islower():

        value = alphabet_lower[rotation]
    
    if character.isupper():
    
        value = alphabet_upper[rotation]
    
    return value
