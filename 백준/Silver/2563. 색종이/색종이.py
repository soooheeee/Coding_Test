import sys
input = sys.stdin.readline

num = int(input())
arr = [[0] * 101 for _ in range(101)] 

for _ in range(num): 
    A, B = map(int, input().split())
    for i in range(A, A+10):
        for j in range(B, B+10):
            arr[i][j] = 1

ret = 0
for i in arr: 
    ret += sum(i)

print(ret) 