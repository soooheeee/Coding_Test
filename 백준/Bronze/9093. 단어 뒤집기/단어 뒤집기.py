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
