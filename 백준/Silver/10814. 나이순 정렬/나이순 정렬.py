import sys
input = sys.stdin.readline

N = int(input())
user = []
for _ in range(N):
    age, name = input().split()
    user.append([int(age),name])

for i in sorted(user,key=lambda x : x[0]):   # age를 기준으로 정렬한다 -> x[0] , 만일 name 기준이라면, x[1]
    print(i[0],i[1])