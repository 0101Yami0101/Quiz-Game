class quizbrain:
    def __init__(self, question_list):
        self.questionNumber = 0
        self.questionList = question_list
        self.score = 0

    def still_have_questions(self):
        if self.questionNumber < len(self.questionList):
            return True
        else:
            return False

    def next_question(self):
        #currentQuestion becomes a question object from the list of question objs created
        currentQuestion = self.questionList[self.questionNumber]  #Picks the question from the list of questions that is passed according to question number
        self.questionNumber += 1
        user_answer = input(f"Q: {self.questionNumber}. {currentQuestion.question} (TRue or False): ")
        self.check_answer(user_answer, currentQuestion.answer)  #Check_answer() method runs with next_question() method

    def check_answer(self, userGuess, correctAnswer):
        if userGuess.lower() == correctAnswer.lower():
            print("YAy you got it")
            self.score += 1
        else:
            print(f"YOu are wrong ")
        print(f"The correct answer was {correctAnswer}")
        print(f"YOur Current Score is {self.score} / {self.questionNumber} \n \n")