import sys
input = sys.stdin.readline

s = input()
li=[]

for i in range(len(s)-1):
    li.append(s[i:-1])
li.sort()
for j in range(len(s)-1):
    print(li[j])
