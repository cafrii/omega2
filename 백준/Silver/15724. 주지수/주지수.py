import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    K = int(input().rstrip())
    B = []
    for _ in range(K):
        B.append(list(map(int, input().split())))
    return N,M,A,K,B

def solve(N:int, M:int, A:list[list[int]], K:int, B:list[list[int]])->list[int]:
    '''
    Args:
        N,M: 땅의 크기. N (row) x M (column)
        A: NxM 크기의 2차원 배열. 해당 구역에 거주하는 사람 수.
        K: 아래 B 요소 개수.
        B: 알고자 하는 영역의 좌상단, 우하단 좌표 (sy,sx), (ey,ex). 1-based 좌표.
    주의:
        A 배열의 index는 zero-based. B는 1-based.
        B 요소의 좌표는 우리 기준으로는 y1,x1,y2,x2 이다.
    Returns:
        K개의 영역 내의 거주 사람 수. 길이 K의 배열.
    알고리즘:
        누적 sum 을 이용하여 부분합 계산
    '''
    # 누적 sum 계산
    S = [ [0]*(M+1) for _ in range(N+1) ]
    # S[y][x] 는 A[0][0] 부터 A[y-1][x-1] 범위 내의 사람 수

    for y in range(1, N+1):
        sum1 = 0  # sum of line segment
        for x in range(1, M+1):
            sum1 += A[y-1][x-1]
            S[y][x] = S[y-1][x] + sum1

    return [
        S[y2][x2] - S[y1-1][x2] - S[y2][x1-1] + S[y1-1][x1-1]
        for y1,x1,y2,x2 in B
    ]

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
