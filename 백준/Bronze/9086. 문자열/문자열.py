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

#### 문자열의 가장 끝은 -1 사용하기
n=int(input())
for i in range(n):
	X=list(input())
	print(X[0]+X[-1])
