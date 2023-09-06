method B :
a,b = int(input()),input()
print(*[a*int(p) for p in b][::-1], a*int(b))

[::-1] 인덱스를 주면 전체 문자열을 역순으로 출력하는 것(리스트, 튜플에서도 사용가능함)
ex> 1=['a','b','c','d','e']
print(1[::-1}]) #['e','d','c','b','a']

t=['a','b','c','d','e']
print(t[::-1}]) #['e','d','c','b','a']

