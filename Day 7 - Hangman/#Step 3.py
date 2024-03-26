#Step 3
import random 
	
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word) #number of letters in chosen word

print(f"Pssst the solution is {chosen_word}")

letter = 0
display = [] #empty list
for letter in chosen_word: # loop through each letter in chosen word
        display.append("_") #adds "_" for every letter in chosen word to empty list

while chosen_word != "".join(display): #while chosen =/= the word in our display, reapeat the loop
        guess = input("Guess a letter: ").lower()
        for position in range(word_length): #loops through each letter of word, random word with unknown length do range is len(word)
                letter = chosen_word[position] #each item in word string is a letter
                if letter == guess: #if the letter matches ...
                        display[position] = letter #... the display list will replace the blanck space with the guessed letter 
        print(display)                
        if chosen_word == "".join(display): #when the display matches the word chosen stop the loop and finish game
                print(f"Congratulations! The word was {chosen_word}.\nYou Won!" )
        