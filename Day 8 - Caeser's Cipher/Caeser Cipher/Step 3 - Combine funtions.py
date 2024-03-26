#Caeser Cipher - Encryption

import string

alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def caesar(text, shift, direction):
    """Coverts a message into a a Caeser Cipher and vice versa"""
    cipher = "" # this will tell us our encrypted text
    if direction == "decode":
        shift *= -1 
    for letter in text: #loop through input text and ... 
        text_index = alphabet.index(letter) 
        new_index = text_index + shift # new position is the old position plus/ minus the number of times shifted
        if new_index > len(alphabet):
            new_index = len(alphabet) - new_index
        cipher_text = alphabet[new_index] # loop through and output letter with said index from alphabet
        cipher += cipher_text #add each letter to cipher str
    print(f"The {direction}d text is {cipher}.")
caesar(text, shift, direction)
    

