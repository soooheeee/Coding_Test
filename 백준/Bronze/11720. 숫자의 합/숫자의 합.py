import sys
input = sys.stdin.readline

num = input().strip()
numbers = list(map(int,input().strip()))

print(sum(numbers))
