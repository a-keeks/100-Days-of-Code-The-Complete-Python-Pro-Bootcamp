from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from start_finish_art import start, finished
from borders import frame

question_bank = []

for question in question_data:
    question_category = question["category"]
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_category, question_text, question_answer)
    question_bank.append(new_question)


print(start)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():


    quiz.next_question()

print("")
print("You have completed the quiz.")
print("")



frame(f"Your Final Score is {quiz.score}/{quiz.question_number} ", alignment = "center", display = "center")
print("")
print(finished)