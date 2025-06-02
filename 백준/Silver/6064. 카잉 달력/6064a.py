'''
다른 답변

https://www.acmicpc.net/source/94793071

M*N 까지 가지 않고 lcm 까지만 루프를 도는 것이 시간 단축의 핵심이다.

'''

import sys; input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_year(M, N, x, y):
    max_year = lcm(M, N)
    for k in range(x, max_year + 1, M):
        if (k - 1) % N + 1 == y:
            return k
    return -1

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(find_year(M, N, x, y))
