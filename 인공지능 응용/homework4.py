# class CAIGrage:
#     def Contrutor(self):
#         print('나의 이름은')

# james = CAIGrage()
# james.Contrutor()

# 출력 : 나의 이름은

class CAIGrade:
    def __init__(self, name, homework, quiz, exam):
        self.__name = name
        self.__homework = homework
        self.__quiz = quiz
        self.__exam = exam
        self.__score = self.__compute_score()

    def __compute_score(self):
        return 0.2 * self.__homework + 0.2 * self.__quiz + 0.6 * self.__exam

    def set_score(self, homework, quiz, exam):
        self.__homework = homework
        self.__quiz = quiz
        self.__exam = exam
        self.__score = self.__compute_score()

    def __call__(self):
        return f"{self.__name}-{self.__homework}-{self.__quiz}-{self.__exam}-{self.__score}"

student1 = CAIGrade("Plato K", 100, 60, 60)
student2 = CAIGrade("Socrates H", 100, 60, 80)


print(student1())
print(student2())

