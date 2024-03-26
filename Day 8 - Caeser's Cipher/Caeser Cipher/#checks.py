#checks

import string

alphabet = []
for letter in string.ascii_lowercase:
    alphabet.append(letter)

text = input("Type your message:\n").lower()

for char in text:
    if not char in alphabet:
        new_text = text.replace(char, "")
    
print(new_text)