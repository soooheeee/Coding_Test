import sys
input = sys.stdin.readline

sum=0
li=[]
li_2=[]
N= int(input())

for i in range(N):
    for j in range(N):
        if N==5*j+3*i:
            # print(j,i)
            sum=j+i
            li.append(sum)
            li_2.append(sum)
        else:
            li.append(-1)
# print(li)
if max(li) > -1:
    print(min(li_2))
else:
    print(min(li))