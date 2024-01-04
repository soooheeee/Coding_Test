import sys
input = sys.stdin.readline

a,b = map(str, input().split())
a=list(reversed(a))
b=list(reversed(b))
for i in range(1,len(a)):
    a[0]=a[0]+a[i]
    b[0]=b[0]+b[i]
if a[0] > b[0]:
    print(a[0])
if a[0] < b[0]:
    print(b[0])