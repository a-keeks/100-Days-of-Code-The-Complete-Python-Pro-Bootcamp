# randomisation

import random

a = random.randint(1, 99)

b = random.randint(1, 99)

c = a*b

print(f"The product of {a} and {b} is {c}")

# Heads or Tails?

import random
print("Lets toss a coin!")

coin_face = random.randint(0, 1)

if coin_face == 0:
    print("Heads!")

else:
    print("Tails!")

# Random Name Picker

import random 

names_string = input("List the names you want to pick from: ")
names = names_string.split(", ")

print(random.choice(names) + " is going to buy the meal today!")
