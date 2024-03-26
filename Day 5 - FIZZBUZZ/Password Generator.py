import string
import random

letters = string.ascii_letters
letters = list((letters))

numbers = string.digits
numbers = list((numbers))

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = random.choices(letters, k = nr_letters) + random.choices(symbols, k = nr_symbols) + random.choices(numbers, k = nr_numbers)

password_choice = random.sample(password, len(password))

print(f"Your new password is: {''.join(password_choice)}")