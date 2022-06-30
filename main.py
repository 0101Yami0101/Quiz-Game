from data import question_data
from questionModel import Question
from quiz_brain import quizbrain

question_bank = []  #question list
for q in question_data: #q = loop through dictionaries in the list
    question_text = q['text']
    answer = q['answer']
    new_question = Question(question_text,answer) #New obj of Question class
    question_bank.append(new_question)

quiz = quizbrain(question_bank)
while quiz.still_have_questions():  #loop will run till the list of questions are finished
    quiz.next_question()

print("You have completed the quiz..")
print(f"Your final score is {quiz.score}/{quiz.questionNumber}")