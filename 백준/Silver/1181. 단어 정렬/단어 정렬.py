import sys
input = sys.stdin.readline

N=int(input())
li=[]

for i in range(N):
    x=input().strip()
    y=len(x)
    li.append([y,x])
li=sorted(li)

for j in range(N):
    if j==0 or li[j][1] != li[j-1][1]:
        print(li[j][1])