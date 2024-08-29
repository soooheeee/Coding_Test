import sys
input = sys.stdin.readline

s = input().rstrip()

for char in s:
    if '0' <= char <= '9':  # 숫자인 경우 그대로 출력
        print(char, end='')
    elif 'a' <= char <= 'z':  # 소문자 처리
        if ord(char) + 13 > ord('z'):
            print(chr(ord(char) + 13 - 26), end='')
        else:
            print(chr(ord(char) + 13), end='')
    elif 'A' <= char <= 'Z':  # 대문자 처리
        if ord(char) + 13 > ord('Z'):
            print(chr(ord(char) + 13 - 26), end='')
        else:
            print(chr(ord(char) + 13), end='')
    else:
        print(char, end='')  # 알파벳이 아닌 경우 그대로 출력