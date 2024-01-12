import sys
input=sys.stdin.readline

N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
ret = 0

for i,n in enumerate(N):
    ret += (int(b)**i)*(ary.index(n))
print(ret)