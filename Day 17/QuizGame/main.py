from questions import *
from data import *

from QuizBrain import *

question_bank = []
for questions in question_data:
    question_text=questions["text"]
    question_answer=questions["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.new_question()