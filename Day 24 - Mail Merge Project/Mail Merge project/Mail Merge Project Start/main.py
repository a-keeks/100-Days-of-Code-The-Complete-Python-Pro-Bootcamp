# #TODO: Create a letter using starting_letter.txt 
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
    
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# # First we have to replace the senders name to our own

# # search_text = "Angela" #name we need to replace

# # replace_text = "Akila" #name we are replacing it with
# # with open(r"C:\Users\akila\Dropbox\100 Days of Python\2. INTERMEDIATE\Day 24\Mail Merge project\Mail Merge Project Start\Input\Letters\starting_letter.txt", "r") as file:
# #     letter = f.readlines() #opens our letter as read-only and assigns this to the name letter

# #     letter = letter.replace(search_text, replace_text) #

# # with open(r"C:\Users\akila\Dropbox\100 Days of Python\2. INTERMEDIATE\Day 24\Mail Merge project\Mail Merge Project Start\Input\Letters\starting_letter.txt", "w") as file:
# #     file.write(letter) # rewrites the whole letter with our own name

# #open name txt file as list

with open(r"C:\Users\akila\Dropbox\100 Days of Python\2. INTERMEDIATE\Day 24\Mail Merge project\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    list_of_names = [line.rstrip("\n") for line in file]


for name in list_of_names:
    file_name = f"Mail Merge Project Start\Output\letter_to_{name}.txt" #allows us to loop through the list of names and make a file name for each diff name

    replace_text = name
    search_text = "[name]" #we need to search for the name placeholder in order to replace with each name from the list above

    with open(r"C:\Users\akila\Dropbox\100 Days of Python\2. INTERMEDIATE\Day 24\Mail Merge project\Mail Merge Project Start\Input\Letters\starting_letter.txt", "r") as file:
        letter = file.read() #opens our letter as read-only and assigns this to the name letter

        letter = letter.replace(search_text, replace_text) #  replaces name placeholder with names in list


    with open(file_name, "w") as file:
        file.write(letter) # rewrites the whole letter with our new replacements


