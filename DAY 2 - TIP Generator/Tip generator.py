#Tip generator

print("Welcome to the tip calculator!")

total = input("What was the total bill \n")
tip_percent = int(input("What percentage tip would you like to pay? 10, 12 or 15 \n"))
num_of_people = input("How many people will be splitting the bill? \n")

total_bill = float(total) * (1+tip_percent/100)

each_bill = round((total_bill / int(num_of_people)), 2)

print(f"Each person should pay: £{each_bill}")