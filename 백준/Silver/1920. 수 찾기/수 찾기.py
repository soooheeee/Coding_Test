import sys
input = sys.stdin.readline

n = int(input())
n_li = set(map(int,input().split()))

m = int(input())
m_li = list(map(int,input().split()))


for num in m_li:
    if num in n_li:
        print('1')
    else:
        print('0')