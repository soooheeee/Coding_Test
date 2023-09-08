import sys
input = sys.stdin.readline

observ = {}
cnt = 0
for _ in range(int(input())):
    cow, dir = map(int, input().split())
    if cow in observ.keys():
        if observ[cow] == dir:
            continue
        else:
            observ[cow] = dir
            cnt += 1
    else:
        observ[cow] = dir
print(cnt)