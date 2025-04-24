# 제출용

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

# input
board = []
for y in range(9):
    a = list(map(int, input().split()))
    assert len(a) == 9
    board.append(a)

def print_board(to = sys.stdout):
    [ print(*a, file=to) for a in board ]

# print_board(sys.stderr)

# 0 의 위치 정보 수집.
# zeros[] 는 (y, x, level) 의 튜플.
#   (y,x) 는 0 이 위치한 좌표
#   level 은 난이도. 난이도는 가로, 세로, 구역 내에 포함된 0 의 개수.
zeros = []

def prepare():
    for y in range(9):
        for x in range(9):
            if board[y][x]: continue
            zeros.append((y, x, 0)) # level 사용하지 않도록 개선

def is_allowed(y_, x_, num):
    if num in board[y_]: # 가로 체크
        return False
    for y in range(9): # 세로 체크
        if board[y][x_] == num:
            return False
    ya, xa = y_//3*3, x_//3*3   # aligned y, x
    for y in range(ya, ya + 3): # 구역 체크
        for x in range(xa, xa + 3):
            if board[y][x] == num:
                return False
    return True


def solve_step2(n_solved:int) -> bool:
    if n_solved >= len(zeros):
        # log("~~ finished ~~")
        return True

    y_,x_,lvl = zeros[n_solved] # target y, x and level
    # log("step %d: (%d,%d) level %d", n_solved, y_, x_, lvl)

    # 모든 숫자를 순서대로 체크
    for num in range(1, 10):
        if not is_allowed(y_, x_, num): continue
        # log("step %d:     (%d,%d) <= %d", n_solved, y_, x_, e)
        board[y_][x_] = num
        success = solve_step2(n_solved + 1)
        if success:
            return True
        board[y_][x_] = 0 # rollback

    return False

prepare()

if solve_step2(0):
    print_board()
