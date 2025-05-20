
import sys
input = sys.stdin.readline


def solve(A:list[list]) -> int:
    N = len(A)
    # N: size of triagle (height or bottom size)

    dp = [ [0 for x in range(N+2)] for y in range(N+2) ]
    # dp[y][x]: 위에서부터의 레벨 y, 왼쪽에서부터 x 번째의 칸 까지의 경로 합.
    #           y: 1~N.  dp[0] 은 모두 0 으로 미사용.
    #           x: 1~y.  dp[y][0] 은 미사용.

    for k in range(1, N+1): # k: 1 ~ N
        for j in range(1, k+1): # j: 1 ~ k
            dp[k][j] = max(dp[k-1][j-1], dp[k-1][j]) + A[k-1][j-1]

    return max(dp[N])


N = int(input().strip())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
    assert len(A[-1]) == i+1

print(solve(A))
