numbers = [1,2,3]

new_list = [n + 1 for n in numbers]

print(new_list)

####################################################################

name = "Akila"

name_list = [letter for letter in name]

print(name_list)

###################################################################

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_list = [name.upper() for name in names if len(name) >= 5]

print(new_list)
####################################################################
#Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)

####################################################################
#Filter even numbers
list_of_strings = input("List of Numbers: ").split(",")

numbers = [int(x) for x in list_of_strings]

even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)

####################################################################
#Reading files and complining into lists
with open("file1.txt") as file_1:
    list_1 = file_1.readlines()

with open("file2.txt") as file_2:
    list_2 = file_2.readlines()

overlap = [ int(n) for n in list_1 if n in list_2]

print(overlap)