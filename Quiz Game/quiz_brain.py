class QuizBrain:
    def __init__(self, questionlist):
        self.question_number = 0
        self.question_list = questionlist
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q. {self.question_number} {current_question.text} (TRUE/FALSE): ").title()

        self.check_answer(u_answer, current_question.answer)

    def still_has_questions(self):
        if len(self.question_list) <= self.question_number:
            return False
        else:
            return True
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("YOU GOT IT RIGHT!\n" \
            f"The correct answer was: {correct_answer}\n" \
            f"Your current score is: {self.score}/{self.question_number}\n")

        else:
            print("You got it wrong :(\n" \
            f"The correct answer was: {correct_answer}\n" \
            f"Your current score is: {self.score}/{self.question_number}\n")
