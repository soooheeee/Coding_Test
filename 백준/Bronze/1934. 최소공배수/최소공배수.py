import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    if (A < B):
        Min = A
        Max = B
    else:
        Min = B
        Max = A

    while (Max % Min != 0):
        temp = Max % Min
        Max = Min
        Min = temp

    answer = Min * (A // Min) * (B // Min)
    print(answer)