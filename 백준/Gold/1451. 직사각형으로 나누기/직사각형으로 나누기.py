import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().rstrip())))
    return N,M,A


def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    Args:
    Returns:
    '''
    # 누적합 (accumulated sum)
    asum = [ [0]*(M+1) for _ in range(N+1) ]
    # asum 에 대해서만큼은 좌상단 좌표를 (1,1)로 간주하는 것이 편하다.
    # 즉, asum[y][x] 는 (1,1) 부터 (y,x) 까지의 partial sum
    for y in range(1, N+1):
        asum_x = [0]*(M+1)
        for x in range(1, M+1):
            asum_x[x] = asum_x[x-1] + A[y-1][x-1]
            asum[y][x] = asum[y-1][x] + asum_x[x]

    maxval = -1

    # case 1: 세로 분할, 가로 배치 ||.  조건: M>=3
    for i in range(1, M-1):  # i: 첫번째 사각형의 가로길이. 1 ~ M-2
        for k in range(i+1, M): # k: 첫번째와 두번째 사각형의 길이. i+1 ~ M-1
            #   |   k   |
            #   +-i-+---+---+
            #   | 1 | 2 | 3 |
            #   +---+---+---+
            #
            # 각 사각형 내부합
            s1 = asum[N][i] - asum[0][i] - asum[N][0] + asum[0][0]
            s2 = asum[N][k] - asum[0][k] - asum[N][i] + asum[0][i]
            s3 = asum[N][M] - asum[0][M] - asum[N][k] + asum[0][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 2: 가로 분할. N>=3
    for i in range(1, N-1):  # i: 첫번째 사각형의 세로길이. 1 ~ N-2
        for k in range(i+1, N): # k: 첫번째와 두번째 사각형의 길이. i+1 ~ N-1
            #   +-------+---
            #   |   1   |i
            #   +-------+- k
            #   |   2   |
            #   +-------+---
            #   |   3   |
            #   +-------+
            #
            s1 = asum[i][M] - asum[0][M] - asum[i][0] + asum[0][0]
            s2 = asum[k][M] - asum[i][M] - asum[k][0] + asum[i][0]
            s3 = asum[N][M] - asum[k][M] - asum[N][0] + asum[k][0]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 3: T 분할.  N>=2, M>=2
    for i in range(1, N): # i: 위 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌하단 사각형의 가로 길이. 1 ~ M-1
            #   +-------+
            #   |   1   |i
            #   +-k-+---+
            #   | 2 | 3 |
            #   +---+---+
            #
            s1 = asum[i][M] - asum[0][M] - asum[i][0] + asum[0][0]
            s2 = asum[N][k] - asum[i][k] - asum[N][0] + asum[i][0]
            s3 = asum[N][M] - asum[i][M] - asum[N][k] + asum[i][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 4: ㅗ 분할.  N>=2, M>=2
    for i in range(1, N): # i: 위 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌상단 사각형의 가로 길이. 1 ~ M-1
            #   +---+---+
            #   | 1 | 2 |i
            #   +-k-+---+
            #   |   3   |
            #   +-------+
            #
            s1 = asum[i][k] - asum[0][k] - asum[i][0] + asum[0][0]
            s2 = asum[i][M] - asum[0][M] - asum[i][k] + asum[0][k]
            s3 = asum[N][M] - asum[i][M] - asum[N][0] + asum[i][0]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 5: ㅏ 분할.  N>=2, M>=2
    for i in range(1, N): # i: 우상단 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌측 사각형의 가로 길이. 1 ~ M-1
            #   +-k-+---+
            #   |   | 2 |i
            #   | 1 +---+
            #   |   | 3 |
            #   +---+---+
            #
            s1 = asum[N][k] - asum[0][k] - asum[N][0] + asum[0][0]
            s2 = asum[i][M] - asum[0][M] - asum[i][k] + asum[0][k]
            s3 = asum[N][M] - asum[i][M] - asum[N][k] + asum[i][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    # case 6: ㅓ 분할.  N>=2, M>=2
    for i in range(1, N): # i: 우상단 사각형의 세로 길이. 1 ~ N-1
        for k in range(1, M): # k: 좌측 사각형의 가로 길이. 1 ~ M-1
            #   +-k-+---+
            #   | 1 |   |i
            #   +---+ 3 +-
            #   | 2 |   |
            #   +---+---+
            #
            s1 = asum[i][k] - asum[0][k] - asum[i][0] + asum[0][0]
            s2 = asum[N][k] - asum[i][k] - asum[N][0] + asum[i][0]
            s3 = asum[N][M] - asum[0][M] - asum[N][k] + asum[0][k]
            v = s1*s2*s3
            if v > maxval: maxval = v

    return maxval

if __name__ == '__main__':
    print(solve(*get_input()))
