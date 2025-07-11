
import sys
input = sys.stdin.readline


tetro_masks_str = [
    ['####'],  # flat _

    ['#',
     '#',
     '#',
     '#'],  # 90, standing |

    ['##',
     '##'], # box

    ['# ',
     '# ',
     '##'],  # tall L
    ['  #',
     '###'], # 90 cc
    ['##',
     ' #',
     ' #'],  # 180 cc
    ['###',
     '#  '], # 270 cc

    [' #',
     ' #',
     '##'],   # mirror of L
    ['###',
     '  #'],  # 90 cc
    ['##',
     '# ',
     '# '],   # 180 cc
    ['#  ',
     '###'],  # 270 cc

    ['# ',
     '##',
     ' #'],    # zigzag
    [' ##',
     '## '],   # 90 cc

    [' #',
     '##',
     '# '],    # mirror of above
    ['## ',
     ' ##'],   # 90 cc

    ['###',
     ' # '],  # T
    ['# ',
     '##',
     '# '],   # 90 cc
    [' # ',
     '###'],  # 180 cc
    [' #',
     '##',
     ' #'],   # 270 cc
]



def solve(board:list[list[int]])->int:
    '''
        use 3 nested loop instead of 4.
        mask y, x loop is replaced with offset loop.

    '''
    N,M = len(board), len(board[0])
    max_ms = 0

    for mi in range(len(tetro_masks_str)):
        m = tetro_masks_str[mi]
        mh, mw = len(m), len(m[0])

        # convert to tetro_masks to tetro_mask_offsets
        offsets = []
        for y in range(mh):
            for x in range(mw):
                if m[y][x]=='#': offsets.append((y,x))
        # assert len(offsets) == 4

        for y0 in range(N+1-mh):
            for x0 in range(M+1-mw):
                ms = 0
                for dy,dx in offsets:
                    ms += board[y0 + dy][x0 + dx]
                max_ms = max(max_ms, ms)
    return max_ms



N,M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    assert len(board[-1]) == M

print(solve(board))

