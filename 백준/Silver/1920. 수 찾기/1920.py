'''
수 찾기

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	315315	101890	66929	30.762%

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''


import sys
input = sys.stdin.readline

set1 = set()

N = int(input().strip())
for _ in map(lambda s: set1.add(int(s)), input().split()): pass

# print(set1)

M = int(input().strip())
B = list(map(int, input().split()))
for b in B:
    print(1 if b in set1 else 0)


'''
예제 입력 1
5
4 1 5 2 3
5
1 3 7 9 5

예제 출력 1
1
1
0
0
1



시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 100_000,100_000
# N,M = 10,10
print(N)
A = [ str(randint(-2**31, 2**31)) for _ in range(N) ]
print(' '.join(A))
print(M)
A = [ str(randint(-2**31, 2**31)) for _ in range(M) ]
print(' '.join(A))
EOF
) | time python3 1920.py

python3 1920.py  0.13s user 0.06s system 62% cpu 0.293 total
'''
