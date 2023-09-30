import sys
input = sys.stdin.readline

li = []

N, M = map(int, input().split())

for i in range(N):
    li.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())
    li[i - 1], li[j - 1] = li[j - 1], li[i - 1]

for value in li:
    print(value, end=' ')
