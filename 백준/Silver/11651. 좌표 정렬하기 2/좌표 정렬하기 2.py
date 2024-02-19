import sys
input = sys.stdin.readline

N=int(input())

li=[]
for i in range(N):
    x,y = map(int,input().split())
    li.append([y,x])

sorted_li=sorted(li)

for y,x in sorted_li:
    print(x,y)
