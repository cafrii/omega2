'''

제출용

'''

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



'''

예제 입력 1
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
예제 출력 1
19

run=(python3 14500.py)

echo '5 5\n1 2 3 4 5\n5 4 3 2 1\n2 3 4 5 6\n6 5 4 3 2\n1 2 1 2 1' | $run
-> 19

예제 입력 2
4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
예제 출력 2
20
예제 입력 3
4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
예제 출력 3
7

run=(python3 14500.py)

echo '5 5\n1 2 3 4 5\n5 4 3 2 1\n2 3 4 5 6\n6 5 4 3 2\n1 2 1 2 1' | $run
echo '4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5\n1 2 3 4 5' | $run
echo '4 10\n1 2 1 2 1 2 1 2 1 2\n2 1 2 1 2 1 2 1 2 1\n1 2 1 2 1 2 1 2 1 2\n2 1 2 1 2 1 2 1 2 1' | $run
->
19
20
7



(python3 <<EOF
import time
from random import seed,randint
# seed(time.time())
seed(43)
N,M = 500,500
# N,M = 10,10
print(N,M)
for y in range(N):
    print(' '.join([ str(randint(1,999)) for x in range(M) ]))
EOF
) | time $run


성능 비교. seed 43, 500x500

plain
$run  3.19s user 0.02s system 97% cpu 3.301 total

fast
$run  1.18s user 0.01s system 93% cpu 1.268 total

'''

