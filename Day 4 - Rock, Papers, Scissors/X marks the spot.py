# X marks the spot

line1 = ["⬜️","️⬜️","️⬜️"] #map is going to be a 3x3 grid so we made three lies and then print them on a new line one after the other
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3] 
print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to hide your treasure? ") #User inputs coordinates
letter = position[0].lower() #letter is assigned to first character of coordinate
abc = ["a", "b", "c"] #Assigns a, b and c to each column - first column is "a", second column is "b" ....
letter_index = abc.index(letter) #.index compares the two lists
number_index = int(position[1])-1 # minus 1 from input number is positions start
map [number_index][letter_index] = "X" #Mark with X
print(f"{line1}\n{line2}\n{line3}") #Prints final map with line1, line2 &line 3 on new lines (3x3 square)