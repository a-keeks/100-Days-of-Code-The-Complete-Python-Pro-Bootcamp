print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza would you like? ") #S, M, or L
add_pepperoni = input("Do you want pepperoni? ") #Y or N
extra_cheese = input("Do you want extra cheese? ") #Y or N

bill = 0
if size == "S": #Small pizza is $15, medium is £20, large is £25
    bill += 15
elif size == "M": 
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total comes to £{bill}.")