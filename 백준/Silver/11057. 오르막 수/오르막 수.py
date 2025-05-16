
import sys
input = sys.stdin.readline

#MAX_N = 1000
MOD = 10007

def solve(N):
    # N==1 일 때의 각 끝자리 별 경우의 수
    dp = [1]*10  # answer for N==1

    for k in range(2, N+1):
        for j in range(9,-1,-1):
            dp[j] = sum(dp[:j+1]) % MOD

    return sum(dp) % MOD


N = int(input().strip())
print(solve(N))
