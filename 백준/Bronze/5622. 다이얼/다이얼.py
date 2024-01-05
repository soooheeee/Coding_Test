import sys
input = sys.stdin.readline

dial =['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s=input()
ret=0
for j in range(len(s)): # s길이 만큼 반복한다. 즉, WA로 입력을 받으면 길이 2만큼 반복한다.
    for i in dial: # i 요소가 다이어리 안에 들어 있다면 즉, s[j]가 W이고, i가 WXYZ일 때 참이됨
        if s[j] in i: # s문자열 중에 j번째 요소가 i에 들어 있다면
            ret+=dial.index(i)+3
print(ret)