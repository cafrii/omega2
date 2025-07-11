'''
14500번
질문 게시판
테트로미노 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	109033	42793	27962	36.876%

문제
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다.
종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다.
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다.
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.


----

1:39~


'''

import sys
input = sys.stdin.readline

import itertools

def log(fmt, *args): print(fmt % args, file=sys.stderr)



tetro_masks = [
    [[1, 1, 1, 1]],       # flat _
    [[1], [1], [1], [1]], # 90, standing |

    [[1, 1], [1, 1]], # box

    [[1, 0], [1, 0], [1, 1]], # tall L
    [[0, 0, 1], [1, 1, 1]],   # 90 cc (counter-clockwise rotate)
    [[1, 1], [0, 1], [0, 1]], # 180 cc
    [[1, 1, 1], [1, 0, 0]],   # 270 cc

    [[0, 1], [0, 1], [1, 1]], # mirror of L
    [[1, 1, 1], [0, 0, 1]],   # 90 cc
    [[1, 1], [1, 0], [1, 0]], # 180 cc
    [[1, 0, 0], [1, 1, 1]],  # 270 cc

    [[1, 0], [1, 1], [0, 1]], # zigsaw
    [[0, 1, 1], [1, 1, 0]],   # 90 cc

    [[0, 1], [1, 1], [1, 0]], # mirror of above
    [[1, 1, 0], [0, 1, 1]],   # 90 cc

    [[1, 1, 1], [0, 1, 0]],   # T
    [[1, 0], [1, 1], [1, 0]], # 90 cc
    [[0, 1, 0], [1, 1, 1]],   # 180 cc
    [[0, 1], [1, 1], [0, 1]], # 270 cc
]



def sumproduct2d(arr1, arr2):
    # arr1 and arr2 is 2d (nested) list.
    # assert len(arr1)==len(arr2) and len(arr1[0])==len(arr2[0])
    it1 = itertools.chain(*arr1)
    it2 = itertools.chain(*arr2)
    return sum(map(lambda x, y: x*y, it1, it2))


def sumproduct2dmask(arr, yo, xo, mask):
    # arr and mask is 2d (nested) list.
    # assert len(arr)>=yo+len(mask) and len(arr[0])>=xo+len(mask[0])

    islice = itertools.islice
    chain = itertools.chain

    height,width = len(mask),len(mask[0])
    iss = [ islice(arr[y], xo, xo+width) for y in range(yo, yo+height) ]
    result = sum(map(lambda x,y: x*y, chain(*iss), chain(*mask)))
    return result


def solve_slow(board:list[list[int]])->int:
    '''
        trying to avoid using for loop.
    '''
    N,M = len(board), len(board[0])

    # # extend N,M to avoid iterable shortage (early stop)
    # # max 3 space needed, both for horizontally and vertically.
    # for a in board:
    #     a.extend([0, 0, 0])
    # board.extend([ [0]*(M+3) for y in range(3) ])

    max_ms = 0

    for mi in range(len(tetro_masks)):
        m = tetro_masks[mi]
        xh, xw = len(m)-1, len(m[0])-1

        for y in range(0, N-xh):
            for x in range(0, M-xw):
                # get masked-sum
                ms = sumproduct2dmask(board, y, x, m)
                max_ms = max(max_ms, ms)
    return max_ms




def solve_plain(board:list[list[int]])->int:
    '''
        use plain, nested for loop
    '''
    N,M = len(board), len(board[0])
    max_ms = 0

    for mi in range(len(tetro_masks)):
        m = tetro_masks[mi]
        mh, mw = len(m), len(m[0])

        for y0 in range(0, N+1-mh):
            for x0 in range(0, M+1-mw):
                ms = 0
                for y,mline in enumerate(m):
                    ms += sum([ board[y0+y][x0+k] for k in range(len(mline)) if mline[k] ])
                max_ms = max(max_ms, ms)
    return max_ms


# 숫자보다 문자열로 마스크를 표현하면 시각적으로 좀 더 명확하게 구분이 되어 오타를 줄일 수 있음.

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



def solve_fast(board:list[list[int]])->int:
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
                for i,(dy,dx) in enumerate(offsets):
                    if ms + 1000*(4-i) < max_ms: # pruning
                        break
                    ms += board[y0 + dy][x0 + dx]
                max_ms = max(max_ms, ms)
    return max_ms



N,M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    assert len(board[-1]) == M

# print(solve_slow(board))
# print(solve_plain(board))
print(solve_fast(board))



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

fast with pruning
$run  1.09s user 0.01s system 93% cpu 1.175 total

하지만.. dfs 를 능가할 수는 없음. 14500b.py 참고.

'''

