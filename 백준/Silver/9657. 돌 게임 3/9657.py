'''
9657번
돌 게임 3 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	16032	7104	6109	46.407%

문제
돌 게임은 두 명이서 즐기는 재밌는 게임이다.

탁자 위에 돌 N개가 있다.
상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개, 3개 또는 4개 가져갈 수 있다.
마지막 돌을 가져가는 사람이 게임을 이기게 된다.

두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오.
게임은 상근이가 먼저 시작한다.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1000)

출력
상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.



'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve_dp(N:int)->str:
    '''
    Arg:
        N: number of stones
    Rule
        two player match, player S and C
        each player takes either 1, 3, or 4 stone(s) at his turn
        the player who takes last stone wins
        player S goes first
    Returns
        winner name initial ('S' or 'C')
    '''
    sz = max(4, N)

    dp = [' ']*(sz+1)
    # dp[k]:
    # k 개의 돌이 놓여 있을 때 상근부터 게임을 시작하여 최적 play 했을 경우의 최종 승자
    # '?': 정할 수 없는 경우
    # 'S': 상근 승 확정
    # 'C': 창영 승 확정
    #
    dp[1] = 'S'  # S:1 개 가져가면 됨
    dp[2] = 'C'  # S1, C1. 다른 선택지 없음.
    dp[3] = 'S'  # S3
    dp[4] = 'S'  # S4
    if N <= 4:
        return dp[N]

    '''
        dp[5]의 경우:
        상근 먼저 시작하는데, 한번에 게임을 끝낼 수 없음. (5개 집을 수 없음)
        1, 3, 4 개를 집으면 이후 상태는 dp[4], dp[2], dp[1] 의 상태처럼 되는데 turn이 바뀐다.
        dp[4], dp[2], dp[1] 중에서 C가 이기는 dp[2]가 되도록 선택하면 dp[5]도 S의 승이다.
        즉, dp[k] 에 대해서, dp[k-1], dp[k-3], dp[k-4] 중 C가 이기는 게 하나라도 있다면
        그것을 선택하면 S의 승 확정.
    '''
    for k in range(5, N+1):
        if 'C' in ( dp[k-1], dp[k-3], dp[k-4] ):
            dp[k] = 'S'
        else:
            dp[k] = 'C'
        # log("dp: %s", dp[1:k+1])
    return dp[N]


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().rstrip())
    w = solve_dp(N)
    print('SK' if w=='S' else 'CY')


'''
예제 입력 1
6
예제 출력 1
SK

run=(python3 9657.py)
echo '6' | $run


'''

