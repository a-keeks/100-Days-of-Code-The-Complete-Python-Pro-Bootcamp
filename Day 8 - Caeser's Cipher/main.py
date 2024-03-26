# Functions

#Simple fuction
def greet():
    print("Hello")
    print("I hope you are well")
    print("It's a nice day today")

#Functions that allow for inputs

name = input("What is your name? ")
location = input("Where do you live? ")
def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How are you doing?")
    print(f"What is it like in {location}?")
greet_with_name(name, location)

# Cans of paint for a wall

import math 
test_h = int(input("What is the height of the wall? ")) # Height of wall (m)
test_w = int(input("What is the width of the wall? ")) # Width of wall (m)
coverage = 5

def paint_calc(height, weight, cover):
    """Calculates number of paint cans needed to paint a wall with a given width and height"""
    paint_cans = (height * weight )/ cover
    paint_cans = math.ceil(paint_cans)
    print(f"You'll need {paint_cans} cans of paint for a wall of height {test_h}m and width {test_w}m")

paint_calc(height = test_h, weight = test_w, cover = coverage)

# Check if a number is prime

n = int(input("What number do you want to check? ")) # Check this number

def prime_checker(number=n):
    """Checks if any given number is prime"""
    if n == 1:
        print(f"{str(n)} is not a prime number")
    if n == 2 or n == 3:
        print(f"{str(n)} is a prime number")
    if 3 < n <= 5:
        if n % 2 == 0 or n % 3 == 0:
            print(f"{str(n)} is not a prime number")
        else:
            print(f"{str(n)} is a prime number")
    for i in range(5,n):
        if (n + 1)%6 == 0 or (n - 1)%6 == 0:       
            if n % i == 0 or n %(i+2) == 0:
                print(f"{str(n)} is not a prime number")
            else:
                print(f"{str(n)} is a prime number")
        else:
            print(f"{str(n)} is not a prime number")
        break 
    

prime_checker(number=n)
