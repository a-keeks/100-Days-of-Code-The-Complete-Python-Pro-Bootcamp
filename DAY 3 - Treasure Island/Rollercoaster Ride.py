#Rollercoaster Ride

height = int(input("How tall are you? "))
age = int(input("How old are you? "))
int_price_1 = 5
int_price_2 = 7
int_price_3 = 12

if height > 120:
    if age < 12:
        print(f"That will be £{int_price_1}!")
    elif 12<=age<18:
        print(f"That will be £{int_price_2}!")
    elif age >= 18:
        print(f"That will be £{int_price_3}!")
    
else:
    print("You are too short to ride this ride!")

