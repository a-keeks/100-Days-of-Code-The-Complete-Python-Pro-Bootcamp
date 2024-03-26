# ENCRYPTION/ DECRYTION AS IF LOOP

import string
	
alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

cipher = ""
for letter in text:
    text_index = alphabet.index(letter)
    if direction == "encode":
        new_index = text_index + shift
    if direction == "decode":
        new_index = text_index - shift
    cipher_text = alphabet[new_index] 
    cipher += cipher_text
print(cipher)