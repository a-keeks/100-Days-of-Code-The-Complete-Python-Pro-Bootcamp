from borders import frame
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0 
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"\nQ{self.question_number}. {current_question.category}")
        print()
        user_answer = input(f"{current_question.text} (True/ False): ")
        self.check_answer(user_answer, current_question.answer, current_question)
        current_score = f"{self.score} / {self.question_number}"
        current_score= f"\033[1mCurrent Score: {current_score} \033[0m".rjust(130)
        print(current_score)

    def check_answer(self, user_answer, correct_answer, current_question):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1            
            print(f"You got it right!")
        else:
            print("That's wrong!")
        print()
        print(f"{current_question.text} is: {correct_answer}!")
        


