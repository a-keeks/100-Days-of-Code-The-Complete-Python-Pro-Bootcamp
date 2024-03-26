# program that tests the compatibility between two people.

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

T = name1.count("t") + name2.count("t")

R = name1.count("r") + name2.count("r")

U = name1.count("u") + name2.count("u")

E = name1.count("e") + name2.count("e")

true = T+R+U+E

L = name1.count("l") + name2.count("l")

O = name1.count("o") + name2.count("o")

V = name1.count("v") + name2.count("v")

E = name1.count("e") + name2.count("e")

love = L+O+V+E

Love_Score = true*10 + love

if Love_Score < 10 or Love_Score > 90:
   print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif (40<= Love_Score <= 50):
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")





