
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
        #log("[%d] %s", level, '--' if elapsed_time[level] == INF else elapsed_time[level])

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
