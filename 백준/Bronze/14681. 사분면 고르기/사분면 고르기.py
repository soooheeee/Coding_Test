import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

if 0<=x:
    if 0<=y:
        print("1")
    else:
        print("4")

elif x<0:
    if 0<=y:
        print("2")
    else:
        print("3")