import sys
input = sys.stdin.readline

n = int(input())
dic = {}
li = {}

for i in range(n):
    k,v = input().split()
    dic[k] = v
    if v == 'leave':
        del dic[k]


reversed_li = sorted(dic.items(),reverse=True)
dic = dict(reversed_li)
# print(reversed_li)

for k in dic.keys():
    print(k)