# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

direction = input('You arrive at a cross road. Where do you want to go? Type "left" or "right"\n') #Left or Right?

if direction == "left" or "Left":
    print("You come to a lake.")
    island = input('There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if island == "wait" or "Wait":
        print("You arive at the island unharmed.")
        door = input('You come across 3 doors, one red, one yellow and one blue. Which colour do you choose? Type "red", "yellow" or "blue"\n')
        if door == "yellow" or "Yellow":
            print("The door opens and you are greeted by a great big Tresure Chest.\nYou Win!")
        elif door == "red" or "Red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue" or "Blue":
            print("Eaten by beasts.\nGame Over!")
        else:
            print("Game Over!")
    elif island == "swim":
        print("You are attacked by piranha.\nGame Over!")
    else:
        print("You are attacked by piranha.\nGame Over!")
else:
    print("You fall into a hole.\nGame Over!")