########################## BlackJack Project ###########################

import random
from art import logo
import os
def clear():
    os.system('cls')

def deal_card():
    """Returns random card form the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares to see if either user or computer has a blackjact and if not which one has the highest score"""
    if user_score > 21 and computer_score > 21:
        return "You both went over 21, You both Lose"
    elif user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. You Lose!"
    elif user_score == 0:
        return "You have a Blackjack. You Win!"
    elif user_score > 21:
        return "You went over 21, You Lose!"
    elif computer_score > 21:
        return "Computer has gone over 21, You Win!"
    elif user_score > computer_score:
        return "You have the highest score, You Win!"
    elif computer_score > user_score:
        return "The computer has the highest score, You Lose!"
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score = {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_playing = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if continue_playing == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
