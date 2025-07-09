import sys

MOD = 10_007

def solve(N)->int:
    '''
    동적프로그래밍으로 시도.
    dp[k] 는 길이 k 까지의 솔루션. 즉 2 x k 직사각형을 채우는 방법의 수.

    dp[0] = 0
    dp[1] = 1  # 세로타일 1개. I
    dp[2] = 3  # ==, ||, ㅁ
    '''
    dp = [0]*(N+1)
    dp[1:3] = [1,3]
    for k in range(3, N+1):
        # dp[k-1] 의 경우에 | 하나 추가하는 경우.
        # dp[k-2] 의 경우에 ㅁ 와 == 추가하는 경우.
        dp[k] = (dp[k-1] + dp[k-2]*2) % MOD

    return dp[N]



N = int(input().strip())
print(solve(N))
