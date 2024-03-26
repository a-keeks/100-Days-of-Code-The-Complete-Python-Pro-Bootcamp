#Step 1

import random
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

letter = 0

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")



