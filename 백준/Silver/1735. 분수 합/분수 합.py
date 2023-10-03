import sys
input = sys.stdin.readline
import math


a,b =map(int,input().split())
c,d=map(int,input().split())

if b!=d:
    max=math.gcd(b*d,(a*d)+(b*c))
    bunmo=b*d//max
    bunza=((a*d)+(b*c))//max
    print(bunza,bunmo)
else:
    max=math.gcd(b,(a+c))
    bunmo=b//max
    bunza=(a+c)//max
    print(bunza,bunmo)