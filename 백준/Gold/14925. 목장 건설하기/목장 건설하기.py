def get_input():
    import sys
    input = sys.stdin.readline
    M,N = map(int, input().split())
    A = []
    for _ in range(M):
        A.append(list(map(int, input().split())))
        #assert len(A[-1]) == N
    return M,N,A

def solve(M:int, N:int, A:list[list[int]])->int:
    '''
    Args: A: ground map, MxN matrix
            M: 세로길이, num of rows
            N: 가로길이, num of columns
    '''
    dp = [ [0]*(N+1) for _ in range(M+1) ]
    max_l = 0
    for y in range(1, M+1):
        for x in range(1, N+1):
            if A[y-1][x-1]: continue # 나무 또는 돌
            dp[y][x] = min(dp[y][x-1], dp[y-1][x], dp[y-1][x-1]) + 1
        max_l = max(max_l, max(dp[y]))
    return max_l

if __name__ == '__main__':
    print(solve(*get_input()))
