from helpers import alphabet_possition, rotate_character

def encrypt(text, encryption_key):

    lenght_of_key = len(encryption_key)

    message = ""

    non_alpha_index_minus = 0

    for index, char in enumerate(text):
        
        if char.isalpha():

            rotation = alphabet_possition(encryption_key[(index-non_alpha_index_minus) % lenght_of_key])
     
            character = rotate_character(char, rotation)
     
            message += character
  
        if not char.isalpha():

            message += char
     
            non_alpha_index_minus += 1
            
    return message

def main():

    message = input("Type a message:")

    encryption_key = input("Enter encryption key word:")

    return print(encrypt(message, encryption_key))

if __name__ == "__main__":

    main()
