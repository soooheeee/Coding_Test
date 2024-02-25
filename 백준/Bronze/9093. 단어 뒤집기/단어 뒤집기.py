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