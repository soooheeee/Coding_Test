import sys
input = sys.stdin.readline

chess=[1,1,2,2,2,8]

num_list = list(map(int,input().split()))

for i in range(6):
    print(chess[i]-num_list[i],end=' ')