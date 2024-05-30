from question_data import question_data
from quiz_brain import QuizBrain
import os


class Question():
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer




question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

os.system("clear")
while quiz_brain.still_has_question():
    
    quiz_brain.next_question()

os.system("clear")
print(f"Quiz Completed!!!\nYour final score is {quiz_brain.score} of {quiz_brain.question_number}.")







