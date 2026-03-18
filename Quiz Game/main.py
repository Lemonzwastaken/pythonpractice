from question_model import *
from data import *
from quiz_brain import *


question_bank = []
for question in question_data:
    new_question = Question(q_text=question["text"], q_answer=question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(questionlist=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Game over!!!\n\n" \
f"Your final score is: {quiz.score}/{quiz.question_number}")
