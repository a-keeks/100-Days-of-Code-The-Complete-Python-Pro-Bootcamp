#Caeser Cipher - Encryption

import string
from art import logo

print(logo)
alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

def caesar(start_text, shift_amount, cipher_direction):
    cipher = "" # this will tell us our encrypted text
    if cipher_direction == "decode":
            shift_amount *= -1 
    for char in start_text: #loop through input text and ... 
        if char in alphabet:
            text_index = alphabet.index(char)
            new_index = text_index + shift_amount # new position is the old position plus/ minus the number of times shifted
            cipher_text = alphabet[new_index] # loop through and output letter with said index from alphabet
            cipher += cipher_text #add each letter to cipher str
        else:
            cipher += char
    print(f"The {direction}d text is {cipher}.")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    
    restart = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if restart == "no":
        should_end = True
        print("Caeser Cipher is finished. Goodbye!")
        

