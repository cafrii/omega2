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

def solve_fast(N:int, M:int, A:list[str])->str:
    '''
    Args:
    Returns:
    2d dp 대신 두벌의 1-d dp로 풀이
    '''
    dp,dp_old = [0]*(M+1),[0]*(M+1)
    max_w = 0
    for y in range(1, N+1):
        for x in range(1, M+1):
            if A[y-1][(x-1)*2] == '0':
                continue
            dp[x] = min(dp_old[x], dp_old[x-1], dp[x-1]) + 1
        max_w = max(max(dp), max_w)
        dp,dp_old = [0]*(M+1),dp
    return str(max_w)

if __name__ == '__main__':
    print('\n'.join(
        [ solve_fast(N,M,A) for N,M,A in get_input() ]
    ))
