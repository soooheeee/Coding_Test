import sys
input = sys.stdin.readline

sum = 0

total_price = int(input())

for _ in range (int(input())):
    price,count = map(int,input().split())
    sum+=price*count
if sum==total_price:
    print("Yes")
else:
    print("No")