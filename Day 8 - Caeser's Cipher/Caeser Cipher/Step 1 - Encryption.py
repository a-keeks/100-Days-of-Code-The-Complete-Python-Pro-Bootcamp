#Caeser Cipher - Encryption

import string
	
alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt:\n")

def encrypt(text, shift):# define encrypt funct.
    cipher = "" # this will tell us our encryptded text
    for letter in text: #loop through input text and ... 
        text_index = alphabet.index(letter) #... output position of each letter in alphabet
        new_index = text_index + shift # new position is the old position plus the number of times shifted
        new_index = len(alphabet) - new_index
        cipher_text = alphabet[new_index] # loop through and output letter with said index from alphabet
        cipher += cipher_text #add each letter to cipher str
    print(f"The encoded text is {cipher}.")
encrypt(text, shift)