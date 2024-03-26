#Rollercoaster 2

height = int(input("How tall are you? "))

bill = 0

child = 5
youth = 7
adult = 12
senior = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    
    if age < 12:
       bill += child
       print(f"A child ticket is £{child}.")
    elif age <= 18:
        bill += youth
        print(f"A youth ticket is £{youth}.")
    elif age >= 55:
        bill += senior
        print(f"The ticket is on the house.")
    else:
        bill += adult
        print(f"An adult ticket is £{adult}.")
   

    photos = input("Do you want your photos printed? ")
    if photos == "Y":
         bill += 3
         

    print(f"The total will be £{bill}!")

else:
    print("Sorry, you are too short to ride this ride!")


