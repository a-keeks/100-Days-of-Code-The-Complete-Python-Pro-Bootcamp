rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_image =[rock, paper, scissors]
game_image_name = ["Rock", "Paper", "Scissors"]

print("Welcome to the Rock, Paper, Scissors World Championships!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(f"You Chose:", game_image_name[user_choice])
print(game_image[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer Chose:", game_image_name[computer_choice])
print(game_image[computer_choice])

if user_choice < 0 or user_choice >= 3:
    print("Invalid choice! You Lose!")
elif computer_choice == 0 and user_choice == 2:
    print("Rock beats Scissors! You LOSE!") 
elif computer_choice == 2 and user_choice == 1:
    print("Scissors beats Paper! You LOSE!")
elif computer_choice == 1 and user_choice == 0:
    print("Paper beats Rock! You LOSE!")
elif user_choice == 0 and computer_choice == 2:
    print("Rock beats Scissors! You WIN!") 
elif user_choice == 2 and computer_choice == 1:
    print("Scissors beats Paper! You WIN!")
elif user_choice == 1 and computer_choice == 0:
    print("Paper beats Rock! You WIN!")
elif user_choice == computer_choice:
    print("It's a draw!")