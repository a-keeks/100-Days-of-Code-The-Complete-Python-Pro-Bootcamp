# from turtle import Turtle, Screen 

# timmy = Turtle() # capital T denotes that it is a class
# print(timmy)
# timmy.shape("turtle") # print(class.attribute) ## attributes are variables 
# ## timmy is originally denoted by a triangle 
# ### this changes it into the shape of a turtle

# timmy.fillcolor("yellow")
# timmy.pencolor("black")
# timmy.width(3)
# timmy.begin_fill()
# count = 1

# while True:
#     timmy.left(85)
#     timmy.forward(200)
#     timmy.right(170)
#     timmy.forward(200)
    
#     if abs(timmy.position()) < 1: # if timmy gets back to his o.g. pos, break the loop
#         break
#     elif abs(timmy.position()) >= 1: # if he hasnt reached his starting pt.
#         count +=1 ##  add 1 to loop counter
#         print(count) ### print final loop count
# timmy.end_fill()

# my_screen = Screen() # object_name = method
# ## this way every time we call the object my_screen, it will call the method "Screen"

# my_screen.exitonclick() # class.method ## methods are functions

# ## DOCUMENTATION FOR Turtle() module: https://docs.python.org/3/library/turtle.html

# Constructing a Prettytable object

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon_name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)