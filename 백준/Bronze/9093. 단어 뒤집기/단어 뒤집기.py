import sys
input = sys.stdin.readline

t=int(input())
li=[]
li_2=[]

for i in range(t):
    li=input().split()
    # print(li)
    for j in range(len(li)):
        li[j]=li[j][::-1]
        # print(li[j][::-1],end=' ')
    for k in range(len(li)):
         print(li[k],end=' ')

# 방법2
# import sys
# N = int(sys.stdin.readline())

# for _ in range(N):
#     test_list = list(sys.stdin.readline().split())
#     result = ""
#     for test_str in test_list:
#         result += test_str[-1::-1]+' '
#     print(result)

# 스택 사용
# import sys

# input = lambda : sys.stdin.readline().rstrip()

# T = int(input())
# for _ in range(T):
#     sentence = input().split()
#     stack = []
#     for word in sentence:
#         convert = ''
#         for ch in word:
#             stack.append(ch)
#         # 리스트는 빈 상태일 때, false로 되고 리스트에 요소가 남아 있다면 true로 변경됨
#         # false 값이 반환되면 while문을 벗어나감
#         while stack: 
#             print(stack.pop(), end="")
#         print(" ", end="")
#     print()
