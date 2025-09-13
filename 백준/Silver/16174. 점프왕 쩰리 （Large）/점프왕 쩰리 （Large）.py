import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    return N,A

def solve(N:int, A:list[list[int]])->int:
    '''
    Returns: 1: success, 0: fail
    '''
    dp = [ [0]*N for _ in range(N) ]
    # dp[y][x] is 1 if we can reach
    dp[0][0] = 1

    for y in range(N):
        for x in range(N):
            if A[y][x] <= 0: continue
            if dp[y][x] == 0: continue
            # jump to right
            nx = x + A[y][x] # next x
            if nx < N: dp[y][nx] = 1
            # jump to down
            ny = y + A[y][x]
            if ny < N: dp[ny][x] = 1

    return dp[N-1][N-1]

if __name__ == '__main__':
    r = solve(*get_input())
    print('HaruHaru' if r else 'Hing')
