programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])

#Add new item to dictionary
programming_dictionary["Loop"] = "The action of doing something over and orver again."
print(programming_dictionary)

#Empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in the dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

####################################################################################################################

#Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin", 
}

#Nesting a List in a Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting a Dictionary in a Dictionary

travel_log = {
    "France" : {"cities visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}, 
    "Germany" : {"cities visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 8}
}

#dictionary with cities visited and total visits and keys within a travel-log dictionary
# {key: value} --> the outer-most dictionary is our travel-log where our keys are the countries visited and the values are dictionaries which tell us the cities visted and how the number of times visited

#Nesting a Dictionary in a List

travel_log = [
    {"countries" : "France", 
    "cities visited" : ["Paris", "Lille", "Dijon"], 
    "total_visits": 12}, 
    
    {"countries" : "Germany", 
     "cities visited": ["Berlin", "Hamburg", "Stuttgart"], 
     "total_visits": 8}
]

# List name is travel-log
# each line as a key value and pair
# each group of 3 lines is a seperate dictionary. Eahc dictionary is a new country and information on the visit

# cont. in travel-log challenge
