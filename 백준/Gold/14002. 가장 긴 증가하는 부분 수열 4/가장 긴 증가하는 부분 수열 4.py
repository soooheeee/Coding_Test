import sys
input = sys.stdin.readline

n = int(input())

arr = [1] * n
li = list(map(int, input().split()))

# LIS 길이를 계산
for i in range(1, n):
    for j in range(i):
        if li[j] < li[i]:
            arr[i] = max(arr[i], arr[j] + 1)

# LIS 길이 출력
max_len = max(arr)
print(max_len)

# LIS 수열 추적
result = []
length = max_len
for i in range(n - 1, -1, -1):
    if arr[i] == length:
        result.append(li[i])
        length -= 1

# 수열을 뒤집어서 출력
result.reverse()
print(' '.join(map(str, result)))
