from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls')

def get_random_account():
    """Gets data from random account"""
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    #print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def check_follower_count(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game(): 
    print(logo)
    score = 0
    continue_game = True
    account_a = get_random_account()
    account_b = get_random_account()

    while continue_game:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        is_correct = check_follower_count(guess, a_followers, b_followers)

        clear()
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")

        else:
            continue_game = False
            print(f"Sorry that's wrong! Final score: {score}")
            

game()