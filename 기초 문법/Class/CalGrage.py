class CAIGrade:
    def __init__(self, name, homework, quiz, exam):
        self.name = name
        self.homework = homework
        self.quiz = quiz
        self.exam = exam
        self.score = 0
    def ComputeScore(self):
        self.score  = 0.2*self.homework + 0.2*self.quiz + 0.6*self.exam  
        return self.score
    def setScore(self, homework, quiz, exam):
        self.homework = homework
        self.quiz = quiz
        self.exam = exam

    def call(self):
         print(f"name:{self.name}homework:{self.homework}quiz:{self.quiz}exam:{self.exam}score:{self.ComputeScore()}")

name = input()
homework = int(input())
quiz = int(input())
exam = int(input())

calgade = CAIGrade( name ,homework, quiz, exam)
calgade.call()

homework = int(input())
quiz = int(input())
exam = int(input())

calgade.setScore(homework, quiz, exam)
calgade.call()
