import random
import pandas

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {student:random.randint(0, 100) for student in names}

# # passed_students = {student: score for (student, score) in students_scores.items() if score > 65}

# print(students_scores)
# print(passed_students)

####################################################################
# sentence = input("Write down a sentence: ")

# result = {word:len(word)for word in sentence.split()}

# print(result)

####################################################################
# weather_c = eval(input())

# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

# print(weather_f)

####################################################################

Student_dict = {"Student": ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"],
                "Score": [33, 99, 93, 67, 76, 59]
                }

students_data_frame = pandas.DataFrame(Student_dict)

#Dataframe to dict
# {new_key:new_value for (index,row)in df.iterrows()} 

#Loop through each row of a data frame
for (index, row) in students_data_frame.iterrows():
    if row.Student == "Beth":
        print(row.score)