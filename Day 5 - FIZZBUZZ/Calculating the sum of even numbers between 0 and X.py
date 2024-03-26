# Calculating the sum of even numbers
target = int(input("X = " )) # input the end value in our range and computer turns it into an integer

n = target // 2 #finding the position of our target in the 2x sequence

s_of_even = n*(n+1) # sum of a series 

print("The sum of even numbers between 1 and " + str(target) + " is " + str(s_of_even))

sum_of_even_numbers = 0 # Starting total is 0
for number in range(2, target + 1, 2): # looping through the numbers starting from 2 upto our target ...
    n += number # ... we add these to our "sum_of_even_numbers"

print(n) # Print our final total
