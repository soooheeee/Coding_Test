import sys
input = sys.stdin.readline

li=[]
sorted_li=[]

N= int(input())
for i in range(N):
    li.append(list(map(int,input().split())))
# print(li)


sorted_li=sorted(li)
for j in range(N):
    print(sorted_li[j][0] ,sorted_li[j][1])


#방법 2, A,B 변수를 두고 풀기

# import sys
# n = int(sys.stdin.readline())
# list = []
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     list.append([a, b])
# list.sort()
# for i in list:
#     print(i[0], i[1])
