
import sys
input = sys.stdin.readline

li = [0] * 30

for _ in range(28):
    n = int(input())
    li[n - 1] = n

for idx in range(30):
    if li[idx] == 0:
        print(idx + 1, end=' ')