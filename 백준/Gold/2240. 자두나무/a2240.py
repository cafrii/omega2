'''
2240번
자두나무 성공, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	23964	9360	6644	39.571%

문제
자두는 자두를 좋아한다. 그래서 집에 자두나무를 심어두고, 여기서 열리는 자두를 먹고는 한다.
하지만 자두는 키가 작아서 자두를 따먹지는 못하고, 자두가 떨어질 때까지 기다린 다음에 떨어지는 자두를 받아서 먹고는 한다.
자두를 잡을 때에는 자두가 허공에 있을 때 잡아야 하는데, 이는 자두가 말랑말랑하여 바닥에 떨어지면 못 먹을 정도로 뭉개지기 때문이다.

매 초마다, 두 개의 나무 중 하나의 나무에서 열매가 떨어지게 된다.
만약 열매가 떨어지는 순간, 자두가 그 나무의 아래에 서 있으면 자두는 그 열매를 받아먹을 수 있다.
두 개의 나무는 그다지 멀리 떨어져 있지 않기 때문에, 자두는 하나의 나무 아래에 서 있다가 다른 나무 아래로 빠르게(1초보다 훨씬 짧은 시간에) 움직일 수 있다.
하지만 자두는 체력이 그다지 좋지 못해서 많이 움직일 수는 없다.

자두는 T(1≤T≤1,000)초 동안 떨어지게 된다.
자두는 최대 W(1≤W≤30)번만 움직이고 싶어 한다.
매 초마다 어느 나무에서 자두가 떨어질지에 대한 정보가 주어졌을 때, 자두가 받을 수 있는 자두의 개수를 구해내는 프로그램을 작성하시오.
자두는 1번 자두나무 아래에 위치해 있다고 한다.

입력
첫째 줄에 두 정수 T, W가 주어진다. 다음 T개의 줄에는 각 순간에 자두가 떨어지는 나무의 번호가 1 또는 2로 주어진다.

출력
첫째 줄에 자두가 받을 수 있는 자두의 최대 개수를 출력한다.

--------

10/6, 10:33~

2d dp-table 이용
검증 완료


'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    T,W = map(int, input().split())
    A = []
    for _ in range(T):
        A.append(int(input().rstrip()))
    return T,W,A


def solve_0(T:int, W:int, A:list[int])->int:
    # short coding
    dp = [ [0]*(W+1) for _ in range(T+1) ]
    for t in range(1, T+1):
        for w in range(0, min(t, W)+1):
            k = (1 if A[t-1] == w%2 + 1 else 0)
            dp[t][w] = max(dp[t][w], dp[t-1][w]+k, dp[t-1][w-1]+k if w>0 else 0)
    return max(dp[T])


def solve(T:int, W:int, A:list[int])->int:
    '''
    Args:
        T: 수행 단계.  1 ~ 1000
        W: 가능한 최대 움직임 수. 1 ~ 30
    Returns:
        받을 수 있는 자두의 최대 개수
    Logic:
        위치는 1 아니면 2. 초기 위치는 1.
        1 <-> 2 변환에 움직임 1 소모.

        w -> position 대응
            w=0, pos=1
            w=1, pos=2
            w=2, pos=1
            ...
        pos = w%2 + 1

    2-d dp table
        T\W 0 1 2 3 4 .. W
        0
        1
        2
        ..
        T

    '''

    dp = [ [0]*(W+1) for _ in range(T+1) ]
    # dp[][]: 해당 상태에서 받은 자두 누적 개수

    for t in range(1, T+1):
        log("t[%d]: p %d", t,  A[t-1])
        # t=1 일때: w= 0,1
        # t=2      w= 0,1,2
        # t=3      w= 0,1,2,3
        # ...      w= 0,.....W (max)
        for w in range(0, min(t, W)+1):
            k = (1 if A[t-1] == w%2 + 1 else 0) # 이번 단계에서 획득한 자두

            # 이동하지 않은 경우.
            v1 = dp[t-1][w] + (1 if A[t-1] == w%2 + 1 else 0)

            # 이동하는 경우. w >= 1 에서만 가능
            if w > 0:
                v2 = dp[t-1][w-1] + (1 if A[t-1] == w%2 + 1 else 0)
            else:
                v2 = 0

            dp[t][w] = max(dp[t][w], v1, v2)

        log("    dp %s", dp[t])

    return max(dp[T])

if __name__ == '__main__':
    #r = solve(*get_input())
    #print(r)
    print(solve(*get_input()))


'''
예제 입력 1
7 2
2
1
1
2
2
1
1
예제 출력 1
6
----
run=(python3 a2240.py)

echo '7 2\n2\n1\n1\n2\n2\n1\n1' | $run
# 6

'''


