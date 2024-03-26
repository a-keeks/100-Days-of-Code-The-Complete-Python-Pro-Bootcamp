import pandas

nato_alphabet = pandas.read_csv(r"NATO-alphabet-start\nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()} 

word = input("What word would you like to spell using the NATO alphabet?: ").upper()

letters_list = [alphabet_dict[letter] for letter in word]

print(letters_list)

# Prints as list of letter:code
# for letter in letters_list:
#     code = alphabet_dict[letter]
#     print(f"{letter}: {code}")