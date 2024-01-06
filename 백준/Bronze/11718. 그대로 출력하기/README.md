# [Bronze V] 그대로 출력하기 - 11718 

[문제 링크](https://www.acmicpc.net/problem/11718) 

### 성능 요약

메모리: 31120 KB, 시간: 48 ms

### 분류

구현, 문자열

### 제출 일자

2024년 1월 6일 23:06:13

### 문제 설명

<p>입력 받은 대로 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.</p>

### 출력 

 <p>입력받은 그대로 출력한다.</p>


# 틀린 방법 
import sys
input = sys.stdin.readline

while True :
    try : # 입력값이 계속 들어오면 그대로 프린트
        print(input())
    except EOFError: # 입력값이 안 들어오면EOF(End Of File)을 사용해서 이 상태가 되면 break를 걸어준다
        break
이렇게 코드를 치게 되면 틀린 코드라고 뜬다 
왜그런지 찾아보니 
![image](https://github.com/soooheeee/Coding_Test/assets/129060841/d5468152-cfea-4001-8af0-694e0f511b34)
![image](https://github.com/soooheeee/Coding_Test/assets/129060841/20f04078-ad11-45b4-b890-7576b08eb1e4)

https://juni-tech.tistory.com/10
