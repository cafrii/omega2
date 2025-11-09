import sys

def get_input():
    input = sys.stdin.readline
    def gen():
        while True:
            N,M = map(int, input().split())
            if N==0: return
            A = [ input().rstrip() for _ in range(N) ]
            yield N,M,A
    return gen()

def solve(N:int, M:int, A:list[str])->str:
    '''
    Args:
    Returns:
    '''
    dp = [ [0]*(M+1) for _ in range(N+1) ]
    # dp[y][x] 는 (y,x)를 우하단 모서리로 하는 정사각형 중 가장 큰 것의 한변의 길이
    #  y,x 좌표는 1-base.

    max_w = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            # "1 2 3" -> 숫자가 있는 인덱스는 0 2 4
            if A[y-1][(x-1)*2] == '0':
                continue
            dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y][x-1]) + 1
            if dp[y][x] > max_w:
                max_w = dp[y][x]

    return str(max_w)

if __name__ == '__main__':
    print('\n'.join(
        [ solve(N,M,A) for N,M,A in get_input() ]
    ))
