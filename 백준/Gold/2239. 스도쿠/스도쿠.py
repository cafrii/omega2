import sys
input = sys.stdin.readline

board:list[list[int]] = []
for _ in range(9):
    board.append([ int(x) for x in input().strip() ])
    assert len(board[-1]) == 9

zeros = []
for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            zeros.append((y, x))
# print(len(zeros))

def print_board(to=sys.stdout):
    for y in range(9):
        print(*board[y], sep='', file=to)

def is_allowed(r, c, num) -> bool:
    if num in board[r]:
        return False
    for y in range(9):
        if board[y][c] == num: return False
    ya,xa = r//3*3, c//3*3
    for y in range(ya, ya+3):
        for x in range(xa, xa+3):
            if board[y][x] == num: return False
    return True


def step(index:int):
    # solve zero in zeros[index] location
    if index >= len(zeros): # all zeros are filled
        return True

    r,c = zeros[index] # target location (row, col)

    for i in range(1, 10): # candidates
        if not is_allowed(r, c, i): continue
        board[r][c] = i
        if step(index+1):
            return True
        board[r][c] = 0 # recover and try next i

if step(0):
    print_board()
