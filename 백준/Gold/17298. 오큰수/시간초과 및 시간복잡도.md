[내가 짠 코드]
import sys
input = sys.stdin.readline

n=int(input())

NGE = list(map(int,input().split()))

for j in range(n):
    for k in range(j+1,n):
        if NGE[j] < NGE[k]:
            print(NGE[k],end=' ')
            break
        elif k+1==n and NGE[j] >= NGE[k]:
            print(-1,end=' ')
            break
print(-1)


