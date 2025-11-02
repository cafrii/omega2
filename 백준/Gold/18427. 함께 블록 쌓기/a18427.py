'''
18427번
함께 블록 쌓기, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	3793	1729	1292	44.126%

문제
1번부터 N번까지의 학생들은 각각 블록들을 가지고 있다.
학생마다 최대 M개의 블록을 가지고 있을 수 있으며, 한 명의 학생이 가지고 있는 모든 블록들의 높이는 서로 다르다.
이 때 1번부터 N번까지의 학생들이 가진 블록을 차례대로 사용하여 바닥에서부터 쌓아올려 하나의 탑을 만들고자 한다.

단, 어떤 학생의 블록은 사용하지 않아도 되며 한 학생당 최대 1개의 블록만을 사용할 수 있다.

1번부터 N번까지의 학생들이 가지고 있는 블록들에 대한 정보가 주어졌을 때,
높이가 정확히 H인 탑을 만들 수 있는 경우의 수를 계산하는 프로그램을 작성하시오.

예를 들어 N=3, M=3, H=5일 때, 각 학생마다 가지고 있는 블록들의 높이가 다음과 같다고 가정하자.

1번 학생: 2, 3, 5
2번 학생: 3, 5
3번 학생: 1, 2, 3

이 때, 탑의 높이가 정확히 5가 되도록 블록을 쌓는 경우로는 다음의 6가지가 존재한다.
(블록을 사용하지 않는 경우는 X로 표시하였다.)

입력
첫째 줄에 자연수 N, M, H가 공백을 기준으로 구분되어 주어진다.
(1 ≤ N ≤ 50, 1 ≤ M ≤ 10, 1 ≤ H ≤ 1,000)
둘째 줄부터 N개의 줄에 걸쳐서 각 학생이 가진 블록들의 높이가 공백을 기준으로 구분되어 주어진다.

단, 모든 블록의 높이는 1,000 이하의 자연수이며 한 명의 학생이 가지고 있는 모든 블록들의 높이는 서로 다르게 주어진다.

출력
첫째 줄에 높이가 H인 탑을 만드는 경우의 수를 10,007로 나눈 나머지를 출력한다.

----

6:18~

dp[k][j]
1번 학생부터 k번 학생까지만을 고려하여 탑의 높이를 j로 만드는 경우의 수
인덱스 순서 변경함.
그리고 직전 학생의 정보만 참고하니, 굳이 2차원 dp 테이블일 필요 없음.

검증 완료.

'''

import sys
log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    input = sys.stdin.readline
    N,M,H = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        assert len(A[-1]) <= M
    return N,M,H,A

def solve(N:int, M:int, H:int, A:list[list[int]])->int:
    '''
    '''
    MOD = 10_007

    dp = [0]*(H+1)
    dp[0] = 1  # 높이 0을 만드는 경우는 1가지

    for k in range(1, N+1):
        dpx = dp[:]  # copy
        # 학생 k가 가지고 있는 블럭의 높이는 A[k-1]
        # log("k %d, A: %s", k, A[k-1])

        for a in A[k-1]:
            for h in range(a, H+1):
                dpx[h] = (dpx[h] + dp[h-a]) % MOD
            # log("  a %d, dp %s", a, dpx)
        dp = dpx
        # log("k %d, dp %s", k, dp)

    return dp[H]


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
3 3 5
2 3 5
3 5
1 2 3
예제 출력 1
6
----
run=(python3 a18427.py)

echo '3 3 5\n2 3 5\n3 5\n1 2 3' | $run
# 6

echo '2 3 5\n1 10\n3 4 9' | $run
# 1
# 블럭 하나의 크기가 H 보다 더 클 수도 있음.



'''

import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    # seed(time.time())
    seed(37)
    N = int(os.getenv('_N', '5'))
    M = 10
    H = 1000
    A = []
    max_h = max(M, H//10) # 개별 블럭의 최대 높이를 너무 크지 않도록 줄임. 그래야 worst case에 가까워짐
    for n in range(N):
        m = randint(1, M) # 이 학생이 가지고 있는 블럭의 수
        x = list(range(1,max_h+1))
        shuffle(x)
        A.append(x[:m])
    return N,M,H,A

def test():
    N,M,H,A = gen_worstcase_input()
    print(N,M,H)
    print('\n'.join( ' '.join(map(str, x)) for x in A ))

'''
# worst case simulation
_N=10 python3 -c "from a18427 import test; test()" | time $run
# 0

_N=100 python3 -c "from a18427 import test; test()" | time $run
# 6122
# $run  0.05s user 0.01s system 92% cpu 0.065 total

'''