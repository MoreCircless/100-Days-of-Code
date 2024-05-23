from data import question_data
from quiz_brain import Question
from quiz_checking import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    Question(text, answer)
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)



    


