#Caeser Cipher - Decryption

import string

alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'decode' to decrypt:\n")

def decrypt(text, shift):# define decode funct.
    original = "" # this will tell us our decoded text
    for letter in text:
        encoded_text_index = alphabet.index(letter)
        new_index = encoded_text_index - shift # new position is the old position minus the number of times shifted
        original_text = alphabet[new_index] # loop through and output letter with said index from alphabet
        original += original_text #add each letter to original str
    print(f"The decoded text is {original}.")
    
decrypt(text, shift)
