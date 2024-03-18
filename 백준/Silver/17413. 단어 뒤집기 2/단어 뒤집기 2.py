import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1 
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))

#스택 사용하기

# from collections import deque
# a = input()+'\n' # 사용자로부터 문자열을 입력받음
# flag = False # flag 변수 초기화
# stack = deque() # deque() 함수를 사용하여 스택(Stack)을 생성
# result = '' # 결과값을 저장할 변수 초기화

# for i in a: 
#     if not flag: 
#         if i == '\n' or i == ' ': # 공백이나 개행 문자인 경우
#             while stack: 
#                 result += stack.pop() 
#             result += " " 

#         else: # "<"와 ">" 사이에 있는 문자열이 아닌 경우
#             if i == "<": 
#                 while stack: # 이 부분이 중요합니다.
#                     result += stack.pop() 
#                 flag = True 

#             stack.append(i) # 스택(Stack)에 데이터를 추가

#     else: # flag가 True인 경우
#         flag = True # flag를 True로 유지
#         stack.append(i) 
#         if i == ">": 
#             while  stack: 
#                 result += stack.popleft() # 스택(Stack)에서 데이터를 popleft()하여 결과값에 추가
#             flag = False 

# print(result) # 결과값을 출력
