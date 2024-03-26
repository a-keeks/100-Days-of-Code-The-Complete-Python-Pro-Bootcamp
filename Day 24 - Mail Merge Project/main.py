with open(r"C:\Users\akila\OneDrive\Desktop\my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode = "a") as file: # mode: "r" read only, "w" replace text in txt file with something new, "a" to add to text in txt file
#     file.write("\nHow'd you like them apples?")

# with open("new_file.txt", mode = "w") as file: # if there is no file with this name, write mode will create it
#     file.write("New text")


