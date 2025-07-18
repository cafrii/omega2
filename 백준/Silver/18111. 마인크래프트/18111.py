'''
18111번
마인크래프트 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	1024 MB	83018	22316	16536	24.528%

문제
팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다.
마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.

목재를 충분히 모은 lvalue는 집을 짓기로 하였다.
하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.

lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다.
우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.

1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다.
밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.
‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다.
또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다.
땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

입력
첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)

둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다.
(i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다.
땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오.
답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.

----

8:03~9:06, 은근히 시간 많이 썼음. for loop 줄이는 최적화 때문에..

'''


import sys, itertools
from collections import defaultdict

input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve(board:list[list[int]], B:int)->tuple[int,int]:
    '''
    Args:
        board:
        B: number of blocks in inventory at start.
    Returns:
        (elapsed_time, ground_level)
    '''
    N,M = len(board),len(board[0])
    num_cell = N*M

    # flatten 2d list to 1d
    board1d = list(itertools.chain.from_iterable(board))
    board1d.sort()

    # get statistics dict
    boarddict = defaultdict(int)
    for e in board1d:
        boarddict[e] += 1

    MAX_LEVEL = 256
    INF = int(1e9) # num_cell * 2 * 256 = 500000 * 256 = 128000000

    elapsed_time = [INF] * (MAX_LEVEL+1)
    lvl_min, lvl_max = min(board1d), max(board1d)

    # for level in range(256, -1, -1):
    for level in range(lvl_min, lvl_max+1):
        # 모든 셀의 높이를 level 에 맞출 때 과부족 수량 계산.
        budget = B
        elapsed = 0
        bankrupt = False

        for lv,cnt in sorted(boarddict.items(), reverse=True):
            if lv > level: # need to cut (dig out). no limit.
                extra = (lv - level) * cnt
                elapsed += extra * 2
                budget += extra
            elif lv < level:  # need to fill. but within budget!
                extra = (level - lv) * cnt
                if extra <= budget:
                    elapsed += extra
                    budget -= extra
                else: # cannot meet!
                    bankrupt = True
                    break
        elapsed_time[level] = elapsed if not bankrupt else INF
        log("[%d] %s", level, '--' if elapsed_time[level] == INF else elapsed_time[level])

    min_et,level = INF,256
    for i,et in enumerate(elapsed_time):
        if et <= min_et:
            min_et,level = et,i

    return (min_et, level)


N,M,B = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    assert len(board[-1]) == M, 'wrong M'
print(*solve(board, B))



'''

run=(python3 18111.py)

예제 입력 1
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1
예제 출력 1
2 0
맨 오른쪽 아래의 블록을 제거하면 모두 높이가 0으로 고른 상태가 된다. 따라서 블럭을 한 번 제거하는 시간 2초가 소요된다.


예제 입력 2
3 4 1
64 64 64 64
64 64 64 64
64 64 64 63
예제 출력 2
1 64

인벤토리에 블록이 하나 있기 때문에, 맨 오른쪽 아래에 블록을 하나 채우면 된다.

예제 입력 3
3 4 0
64 64 64 64
64 64 64 64
64 64 64 63
예제 출력 3
22 63

인벤토리가 비어 있기 때문에, 맨 오른쪽 아래를 제외한 모든 좌표에서 블록을 하나씩 제거해야 한다.


echo '3 4 99\n0 0 0 0\n0 0 0 0\n0 0 0 1' | $run
echo '3 4 1\n64 64 64 64\n64 64 64 64\n64 64 64 63' | $run
echo '3 4 0\n64 64 64 64\n64 64 64 64\n64 64 64 63' | $run
->
2 0
1 64
22 63


2 2 10
2 2
2 2
-> 0 2

2 3 10
5 5 5
5 6 6
-> 4 6



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 500,500
B = randint(1,int(6e7))
print(N,M,B)
for n in range(N):
    print(' '.join([ str(randint(0,256)) for _ in range(M) ]))
EOF
) | time $run

'''

