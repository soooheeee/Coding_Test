import sys
input = sys.stdin.readline

a1, a2 = map(int, input().split())
c = int(input())
n = int(input())
if (a1*n + a2) <= (c*n) and a1 <= c:
    print(1)
else:
    print(0)

# a0과 a1은 음수가 될 수도 있기 때문에 a1 <= c라는 조건을 써야함