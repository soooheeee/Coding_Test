# [Bronze I] 수 정렬하기 3 - 10989 

[문제 링크](https://www.acmicpc.net/problem/10989) 

### 성능 요약

메모리: 31120 KB, 시간: 8872 ms

### 분류

정렬

### 제출 일자

2024년 2월 16일 11:10:33

### 문제 설명

<p>N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.</p>

### 참고한 블로그 
https://yoonsang-it.tistory.com/49

https://wikidocs.net/21057

https://jeonyeohun.tistory.com/103

https://kill-xxx.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0

https://velog.io/@sj9802/print%EB%AC%B8-%EB%8C%80%EC%8B%A0-sys.stdout.write-%EC%9D%84-%EC%93%B0%EC%9E%90

https://skawnj.github.io/python-jeongryeolsorting-yeogsun-jeongryeol-jejariin-place-jeongryeol-gujohwa-jeongryeol.html

https://116116.tistory.com/47#google_vignette

### 문제 풀면서

계수 정렬 알고리즘의 장점은 정렬할 때, 비교 연산을 하지 않아도 된다는 점이다. 따라서 매우 큰 입력 데이터에 대해서도 빠르게 정렬을 수행할 수 있다.
그러나, 숫자의 범위가 클 경우에는 많은 메모리를 필요로 하며, 숫자의 범위가 입력 데이터의 개수보다 훨씬 크면 비효율적일 수 있다.

계수 정렬은 입력 데이터의 크기가 매우 클 수 있으나, 숫자의 범위가 제한되어 있어서 출현 횟수를 세어 정렬 수행할 수 있다.
각 숫자를 비교하는 것보다 효율(입력 데이터의 개수가 많을 때 더욱 그러함)
