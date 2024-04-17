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

## 이진 탐색을 재귀로 구현

import sys
input = sys.stdin.readline

def binary_search(n_li, x, start, end):
    if start > end:
        return False
    mid = ( start + end ) //2
    if n_li[mid] == x:
        return True
    elif n_li[mid] > x:
        return binary_search(n_li, x, start, mid-1)
    else:
        return binary_search(n_li, x, mid+1, end)

n = int(input())
n_li = sorted(map(int,input().split()))

m = int(input())
m_li = list(map(int,input().split()))

for m in m_li:
    if binary_search( n_li, m, 0, n-1):
        print(1)
    else:
        print(0)
