

import sys
input = sys.stdin.readline


def solve_bruteforce(board:list[str])->int:
    '''
    '''
    def check(y0:int, x0:int, ltop_is_b:bool)->int:
        # return the number of cells to be repainted.
        # if left-top is black, then (r+c) even position should be black.
        count = 0
        col = ['B','W'] if ltop_is_b else ['W','B']
        for r in range(8):
            for c in range(8):
                y, x = y0+r, x0+c
                if board[y][x] != col[(r+c) % 2]:
                    count += 1
        return count

    R,C = len(board),len(board[0])
    min_count = R*C
    # res = []

    for y in range(0, R+1-8):
        for x in range(0, C+1-8):
            min_count = min(min_count, check(y, x, True), check(y, x, False))
            # res.extend([ check(y, x, True), check(y, x, False) ])

    # print(res)
    return min_count


N,M = map(int, input().split())  # row, column

board:list[str] = []
for r in range(N):
    board.append(input().strip())
    assert len(board[-1]) == M
    # assume strings are composed of only W and B

print(solve_bruteforce(board))
