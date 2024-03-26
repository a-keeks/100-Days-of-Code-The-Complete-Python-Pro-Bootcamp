# Student Grades

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if 91 <= score: #Scores 91 - 100: Grade = "Outstanding"
        student_grades[student] = "Outstanding"
    elif 81 <= score: #Scores 81 - 90: Grade = "Exceeds Expectations"
       student_grades[student] = "Exceeds Expectations"
    elif 71 <= score: #Scores 71 - 80: Grade = "Acceptable"
        student_grades[student] = "Acceptable"
    elif score <= 70: #Scores 70 or lower: Grade = "Fail"
        student_grades[student] = "Fail"

print(student_grades)


