import sys
input = sys.stdin.readline
li=[]

N=input()

for i in range(len(N)-1):
    li.append(N[i])
# print(li)

li=sorted(li,reverse=True)
for j in range(len(N)-1):
    print(li[j],end='')