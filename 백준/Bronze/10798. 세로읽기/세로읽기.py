import sys
input=sys.stdin.readline

# words = [input() for i in range(5)]
# 아래 코드랑 일치함
words=[]
for i in range(5):
    a = input().strip()
    words.append(a)

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')