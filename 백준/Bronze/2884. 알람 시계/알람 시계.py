import sys
input = sys.stdin.readline

H,M = map(int,input().split())

if M>= 45:
    m=M-45
    h=H
else:
    m=60+M-45
    if H==0:
        h=23
    else:
        h=H-1

print(h, m)