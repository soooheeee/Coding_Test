import sys
input = sys.stdin.readline

li=[]
n=int(input())

for i in range(n):
    str=input().strip()
    li.append(str)
    s=list(li[i])
    print(s[0],end='')
    print(s[len(s)-1])