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
    Args:
        A: fuel loss matrix, NxM
    Returns:
        minimum fuel loss consumed
    '''
    INF = 1000*1000*100 + 1

    dp = [ [ [INF]*3 for m in range(M+2) ] for n in range(N) ]
    # dp[n][m][dir]
    # dir 은 마지막 우주선의 움직임. 0:/↙️ 1:|⬇️ 2:\\↘️
    # m 은 좌우 1칸 씩 여백을 두었음. if 검사가 귀찮으니..

    # dp[0] 초기화
    for m in range(1, M+1):
        dp[0][m][:] = [ A[0][m-1] ]*3 # 처음엔 방향 제약 없으니 모두 동일하게.

    for n in range(1, N):  # n: 1 ~ N-1
        for m in range(1, M+1):
            c = A[n][m-1] # fuel loss in current loc.
            dp[n][m][0] = c + min(dp[n-1][m+1][1], dp[n-1][m+1][2])
            dp[n][m][1] = c + min(dp[n-1][m  ][0], dp[n-1][m  ][2])
            dp[n][m][2] = c + min(dp[n-1][m-1][0], dp[n-1][m-1][1])

    return min( min(dp[N-1][m]) for m in range(1,M+1) )

if __name__ == '__main__':
    print(solve(*get_input()))
