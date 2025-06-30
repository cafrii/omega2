import sys

def solve(N:int)->list[str]:
    # find k?
    assert N%3 == 0
    m = N//3 # 2**k, 즉, 1, 2, 4, 8, 16, ..

    # 삼각 트리의 맨 밑변의 길이:
    width = N*2 - 1

    # 스케치를 위한 보드. N x width
    board = [ [0]*width for h in range(N) ]

    def duplicate_slow(dsty, dstx, height):
        srcy,srcx = 0,0
        for sy in range(0, height):
            dy = dsty + (srcy + sy)
            for sx in range(0, height*2-1):
                dx = dstx + (srcx + sx)
                board[dy][dx] = board[sy][sx]

    def duplicate(dsty, dstx, height):
        for sy in range(0, height):
            dy = dsty + sy
            width = height*2 - 1
            board[dy][dstx:dstx+width] = board[sy][:width]

    for k in range(0, 11):
        # k   : 0, 1, 2, 3, .., 10
        n = (2**k) * 3
        # 2**k: 1, 2, 4, 8, .., 1024
        # n   : 3, 6,12,24, .., 3072
        if n > N: break

        if k == 0: # 단위 삼각 트리. N=3
            board[0][0:5] = [1,1,1,1,1]
            board[1][1] = board[1][3] = 1
            board[2][2] = 1
        # elif k == 1: # n=6
        #     duplicate(3, 3, 3)
        #     duplicate(0, 6, 3)
        # elif k == 2: # n=12
        #     duplicate(6, 6, 6)
        #     duplicate(0, 12, 6)
        # elif k == 3: # n=24
        #     duplicate(12, 12, 12)
        #     duplicate(0, 24, 12)
        # elif k == 4: # n=48
        #     duplicate(24, 24, 24)
        #     duplicate(0, 48, 24)
        else:
            # 이전에 그려진 삼각트리들을 복제
            half_n = n // 2
            duplicate(half_n, half_n, half_n)
            duplicate(0, n, half_n)

    result:list[str] = []
    for h in range(N-1, -1, -1):
        # result.append(''.join(('*' if x else ' ') for x in board[h]).rstrip())
        result.append(''.join(('*' if x else ' ') for x in board[h]))

    return result


N = int(input().strip())
res = solve(N)
for ln in res:
    if ln:
        print(ln)
