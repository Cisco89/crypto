from helpers import alphabet_possition, rotate_character

def encrypt(string, rotation_amount):

    new_string = ""

    for char in string:

        if char.isalpha():

            new_string += rotate_character(char, rotation_amount)

        if not char.isalpha():

            new_string += char

    return new_string

def main():

    message = input("Type a message:")

    rotation = int(input("Rotate by:"))

    return print(encrypt(message, rotation))

if __name__ == "__main__":

    main()
