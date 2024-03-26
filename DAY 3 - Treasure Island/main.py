# Check if a number is even

num = int(input("Input the number you want to check: \n"))

if num % 2 == 0:
    print(f"The number {num} is even!"),
else:
    print(f"The number {num} is odd!")

#Leap year

year = int(input("What year would you like to check? "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"The year {year} is a leap year!")

        else:
            print(f"The year {year} is not a leap year!")
    else:
        print(f"The year {year} is a leap year!")
else: 
    print(f"The year {year} is not a leap year!")