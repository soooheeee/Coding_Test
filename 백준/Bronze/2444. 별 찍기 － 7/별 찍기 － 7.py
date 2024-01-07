n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1): # n부터 1까지 1씩 감소하면서 반복
    print(' '*(n-i) + '*'*(2*i-1))