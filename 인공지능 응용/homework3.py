import sys
input =sys.stdin.readline

li=[]

# def _call_(score):
#     print(name, homework,quiz,exam,score)

# def ComputerScore():
#     score=0.2*homework + 0.2*quiz + 0.6*exam
#     return score
# def setScore(x, y, z):
#     homework=x
#     quiz=y
#     exam=z
#     return homework, quiz, exam

# name = input()
# homework = int(input())
# quiz = int(input())
# exam = int(input())

# score=ComputerScore()
# _call_(score)
# homework=setScore(100,60,80)
# _call_()




def _call_(score):
    li.append(score)
    print(name, homework,quiz,exam,score)

def ComputerScore():
    score=0.2*homework + 0.2*quiz + 0.6*exam
    return score
def setScore(x, y, z):
    homework=x
    quiz=y
    exam=z
    return homework, quiz, exam

li = input().split()

class Member:
    