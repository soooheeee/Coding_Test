import sys
input = sys.stdin.readline
# 입력을 받아 숫자로 변환하고 리스트에 추가
N = int(input())
li = []

for _ in range(N):
    li.append(int(input().strip()))

# 버블 정렬 알고리즘 구현
for i in range(N):
    for j in range(0, N-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

# 정렬된 리스트 출력
for num in li:
    print(num)


#방법 2, 내장 함수 사용하기
    
# import sys

# N = int(input())
# li = []

# for _ in range(N):
#     li.append(int(input().strip()))

# li.sort()

# for num in li:
#     print(num)

