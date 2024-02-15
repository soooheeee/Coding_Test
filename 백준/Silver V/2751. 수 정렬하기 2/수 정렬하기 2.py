import sys
input = sys.stdin.readline

li=[]
sorted_li=[]
N=int(input())

for _ in range(N):
    li.append(int(input().strip()))
sorted_li=sorted(li)

for k in range(N):
     print(sorted_li[k])