# FIZZBUZZ

target = 100 # What number do we want to go up to?

for number in range(1 ,target + 1): # For every number from 1 till the last number we are checking, go through each number checking the following conditions:
    if number % 3 == 0 and number % 5 == 0: # If the number is divisable by 3 AND 5 print fizzbuzz
        print("FIZZBUZZ")
    elif number % 3 == 0: # If the number is divisible by 3 print fizz
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ") # if the number if divisible by 5 print buzz
    else:
        print(number) # If none of the conditions are satisfied just pritn the nubmer as is
