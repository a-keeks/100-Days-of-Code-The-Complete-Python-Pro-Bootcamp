#calculate the average student height from a List of heights.

students_heights = input("Enter the heights of students seperated by a comma: ")
students_heights = [int(x) for x in students_heights.split(',')] #Each string (x) of list into integer
total = 0    #starting height is 0
for height in students_heights:    #for each height in the list ...
    total += height    #... we will go through and add them one-by-one to our starting total of zero

#Total height

print("Total height of the students = " + str(total)) #Print total height of all students in list

#Number of students in list

n = (len(students_heights)) #How many strings in list

print("The number of students = " + str(n)) #Print number of students

#Average height of students

avg_height = total/n #Formula for finding avg height

print("Average height of the students = " + str(avg_height)) #print avg student height