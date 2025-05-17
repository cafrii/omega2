
import sys
input = sys.stdin.readline

#def log(fmt, *args): print(fmt % args, file=sys.stderr)

MOD = 1_000_000_000

def solve(N, K):

    dp = [ [ 0 for n in range(N+1) ] for k in range(K+1) ]
    # dp[k][n] 는 N=n, K=k 일때의 답.
    # dp[0] 은 의미 없음.

    # dp[1] 은 특정 N을 만드는 경우는 1가지씩 밖에 없음.
    # dp[1][0] 부터 dp[1][N] 까지 존재함.

    dp[1] = [ 1 ] * (N+1)
    # log("dp[%d]: %s", 1, dp[1])

    '''
        dp[K] 는 이전 계산들 중 K-1 로 이루어진 값들을 재활용해야 한다.
        dp[K][N] = (
            dp[K-1][N] + # 끝에 0 을 더하는 경우
            dp[K-1][N-1] +  # 끝에 1 을 더하는 경우
            dp[K-1][N-2] +  # 끝에 2 을 더하는 경우
            ...
            dp[K-1][1] +
            dp[K-1][0]
        )
        그런데 이는 앞의 계산식을 다시 재활용할 수 있다.
        dp[K][N-1] = (
            dp[K-1][N-2] +  # 끝에 1 을 더하는 경우
            ...
            dp[K-1][0]
        )
        따라서..
        dp[K][N] = dp[K][N-1] + dp[K-1][N]

        dp[K][N]을 구하려면 k<=K, n<=N 인 모든 k,n 에 대해서 미리 계산이 되어 있어야 한다.
        (k 는 1 부터 K 까지, n 은 0 부터 N 까지.)
    '''

    for k in range(2, K+1):
        dp[k][0] = 1
        for n in range(1, N+1): # n: 1 ~ N
            dp[k][n] = (dp[k][n-1] + dp[k-1][n]) % MOD
        # log("dp[%d]: %s", k, dp[k])
    return dp[K][N]


N, K = map(int, input().split())
print(solve(N, K))
