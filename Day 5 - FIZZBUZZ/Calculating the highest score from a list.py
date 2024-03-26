# calculating the highest score from a List of scores.

student_scores = input("Input list of students scores: ") #input list of strings
student_scores = student_scores.split(',') # split list into strings at comma
student_scores = [int(x) for x in student_scores] # turn each str into integers

highest_score = student_scores[0] #starting with first score in list
for score in student_scores: # for each score in list ....
    if score > highest_score: #... we will check each score against the first in the list...
        highest_score = score # if it is heigher than the "heighest number", it will become our new highest number
else:
    None # if it is lower than our "highest number", our "highest number" will stay the same
    
print("The highest score in the class is: " + str(highest_score)) # once the loop has finished going through the list, it will print the final highest number