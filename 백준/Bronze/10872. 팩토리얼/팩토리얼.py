import sys
input = sys.stdin.readline

fact = 1
n = int(input())

for i in range(1,n+1):
    fact *= i
print(fact) 