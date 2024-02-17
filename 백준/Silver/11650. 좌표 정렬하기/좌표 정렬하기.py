import sys
input = sys.stdin.readline

li=[]
sorted_li=[]

N= int(input())
for i in range(N):
    li.append(list(map(int,input().split())))
# print(li)


sorted_li=sorted(li)
for j in range(N):
    print(sorted_li[j][0] ,sorted_li[j][1])