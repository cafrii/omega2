'''
9660번
돌 게임 6 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	6651	3463	3188	53.124%

문제
돌 게임은 두 명이서 즐기는 재밌는 게임이다.

탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며,
돌은 1개, 3개 또는 4개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.

두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오.
게임은 상근이가 먼저 시작한다.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 1,000,000,000,000)

출력
상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력한다.

------

dp 메모리를 할당하는 것은 불가능.
반면 round queue 방식으로 해도 직접 1부터 dp로 진행하면 무조건 timeout.
결국 규칙을 찾아서 수식으로 계산하는 방법 뿐이다.


'''



import sys
from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve_dp_timeout(N:int)->str:
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
    dp = deque()

    # dp[k]:
    # k 개의 돌이 놓여 있을 때 상근부터 게임을 시작하여 최적 play 했을 경우의 최종 승자
    # '?': 정할 수 없는 경우
    # 'S': 상근 승 확정
    # 'C': 창영 승 확정
    #
    dp.append('?')
    dp.append('S')  # S:1 개 가져가면 됨
    dp.append('C')  # S1, C1. 다른 선택지 없음.
    dp.append('S')  # S3
    dp.append('S')  # S4
    if N <= 4:
        return dp[N - len(dp)]

    ans = ['S','C','S','S']

    for k in range(5, N+1):
        if 'C' in ( dp[-1], dp[-3], dp[-4] ):
            w = 'S'
        else:
            w = 'C'
        dp.append(w)
        dp.popleft()

        ans.append(w)
        log("  %s", ''.join(ans)) # 적당한 수 몇 개에 대해서 로그 출력을 해 보면 규칙을 알 수 있음.
    return dp[-1]



if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().rstrip())
    # w = solve_dp(N)
    # w = solve_dp_mod(N)
    w = 'CSCSSSS'[N%7]
    print('SK' if w=='S' else 'CY')






'''

run=(python3 9660.py)

echo '1000000000' | time $run
# 시간 안끝남!!

echo '10000000' | time $run
# -> $run  1.03s user 0.01s system 99% cpu 1.043 total
# 1/100 로 줄여야 겨우 1초..

0123456 7890123 4567890
CSCSSSS CSCSSSS CSCSSSS

'''

