import sys
input = sys.stdin.readline

li=[]
sum=0
n=int(input())

li=list(map(int,input().split()))
max = li[0] 

for i in range (n):
    if max <=li[i]:
        max=li[i]
for j in range (n):
    change=li[j]/max*100
    sum+=change
avg=sum/n
# print(li)
# print(max)
print(avg)