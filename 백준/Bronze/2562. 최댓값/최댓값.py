import sys
input = sys.stdin.readline

max=0
li=[]

for i in range(9):
    num=int(input())
    if max<=num:   
        max=num
        li.append(max)
    else:
        li.append(num)
print(max)
print(li.index(max)+1)