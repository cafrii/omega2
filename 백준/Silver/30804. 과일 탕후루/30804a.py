'''

다른 풀이.
그런데 쉽게 이해가 되는 코드는 아니다.
수행 시간은 내 코드보다 더 빠름.

출처: https://www.acmicpc.net/source/96000657

--------

6. 핵심 아이디어
두 종류의 과일만 포함하는 가장 긴 구간을 찾기 위해
"마지막으로 과일 종류가 바뀐 위치"(s)를 기억
새로운 과일이 등장하면, 구간 시작(i)을 s로 옮기고, 집합을 새로 만듦
일반적인 슬라이딩 윈도우와 다르게,
"종류가 바뀐 마지막 위치"를 추적하여 불필요한 반복을 줄임
그래서 속도가 빠름

예: 현재 윈도우가 다음과 같다면
1 2 1 2 1 1 2 2 1 2

새로운 숫자 3이 추가될 때, 마지막 2를 제외한 모든 숫자를 다 건너뛰어야 함.
1 2 1 2 1 1 2 2 1 2
                  2 3
그래서 마지막 2를 기억하고 있는 것이 성능에 도움이 된다.

그냥 전형적인 투 포인터 방식이라면 뒤따르는 포인터를 맨 앞의 1부터 계속 scan 해 와야 하지만
먼저 나가는 포인터 진행 시에 이렇게 마지막 변경 위치를 기억해 놓아서
성능 향상을 꾀한 것이 핵심이다.

'''


N = int(input())
S = tuple(map(int, input().split()))

i = 0
s = 0
fruits = set([S[0]])
maximum = 1

for j in range(1, N):
    fruit = S[j]
    cur_fruit = S[s]
    if fruit in fruits:
        if fruit != cur_fruit:
            s = j
    else:
        if len(fruits) >= 2:
            fruits = set([cur_fruit, fruit])
            i, s = s, j
        else:
            fruits.add(fruit)
            s = j
    maximum = max(maximum, j - i + 1)

print(maximum)

