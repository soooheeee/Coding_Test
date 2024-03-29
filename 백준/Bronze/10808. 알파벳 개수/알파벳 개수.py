import sys
input = sys.stdin.readline

ret = [0]*26
li=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

s = input()

for i in range(len(s)):
    if s[i] in li:
        n=li.index(s[i])
        ret[n]+=1
print(*ret)
        