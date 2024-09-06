import sys
input = sys.stdin.readline

cnt = 0
ret = 1

n = int(input())

for i in range(n, 1, -1):
    ret *= i

str_ret = str(ret)
str_ret = str_ret[::-1]

for j in str_ret:
    if j == '0':
        cnt += 1
    else:
        break

print(cnt)
