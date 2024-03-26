########################### Number Guessing Game ###########################

import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100.")
difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard: ")
n_guess = []
number = random.randrange(101)

if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5
print(f"You have {guesses} attempts remianing to guess the number.")  

while guesses > 0:
    guess = int(input("Make a guess: "))
    while guess != number:
        if guess not in n_guess:
            if guess > number:
                print("Too high.")
            elif guess < number:
                print("Too low.")
            guesses -= 1
            if guesses == 1:
                    print(f"You have 1 attempt remaining to guess the number.")
                    break
            if guesses == 0:
                print("You ran out of lives. You Lose!")
                break

            print(f"You have {guesses} attempts remaining to guess the number.")
            break    
        else:   
            print(f"You've already tried '{guess}'. Try Again!")
            break

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break