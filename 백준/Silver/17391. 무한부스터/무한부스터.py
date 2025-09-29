import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    return N,M,A

def solve(N:int, M:int, A:list[list[int]])->int:
    '''
    '''
    INF = N*M + 1
    dp = [ [INF]*M for n in range(N) ]
    dp[0][0] = 0

    for y in range(N):
        for x in range(M):
            cur = dp[y][x] # accululated stops
            if cur == INF: continue
                
            b = A[y][x] # boost
            # x direction
            for dx in range(1, b+1):
                if x+dx >= M: break
                dp[y][x+dx] = min(dp[y][x+dx], cur+1)
            # y direction
            for dy in range(1, b+1):
                if y+dy >= N: break
                dp[y+dy][x] = min(dp[y+dy][x], cur+1)

    return dp[N-1][M-1]

if __name__ == '__main__':
    print(solve(*get_input()))
