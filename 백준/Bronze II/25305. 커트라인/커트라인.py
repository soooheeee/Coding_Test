import sys
input = sys.stdin.readline

N,k =map(int,input().split())
li=list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if i<j:
            if li[i]<li[j]:
                li[i],li[j] = li[j],li[i]
print(li[k-1])

#방법 2, 내장 함수

# import sys
# input = sys.stdin.readline

# N,k =map(int,input().split())
# li=list(map(int,input().split()))

# sorted_li=sorted(li,reverse=True)
# # print(sorted_li)
# print(sorted_li[k-1])
