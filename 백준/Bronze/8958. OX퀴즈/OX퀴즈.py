import sys
input = sys.stdin.readline

li=[]
cnt=0
sum=0

N=int(input())
for i in range(N):
    li.append(input().strip())
# print(li)
# print(li[0:4])
for j in range(N):
    cnt=0
    sum=0
    for k in range(0,len(li[j])):
        string=li[j]
        # print(string[0:2])
        if string[k] == 'O':
            cnt+=1
            sum+=cnt
            # print(cnt)
            if string[k-1:k] and k>0 == 'OO':
                print('good',string[k-1:k+1])
                cnt+=1
                sum+=1
        else:
            cnt=0
    print(sum)