import math
import sys
input = sys.stdin.readline


def solve(N:int)->int:

    dp = [9]*(N+1)
    dp[1] = 1

    # populate power of integers
    is_power_num = [0]*(N+1)  # 0~N
    for i in range(1,int(math.sqrt(N))+1):
        i2 = i*i
        if i2 <= N:
            is_power_num[i2] = i

    for i in range(2, N+1):
        # check if i is square number
        if is_power_num[i]:
            dp[i] = 1
            continue

        # i-1 부터 0을 향해 거슬러 올라가면서 검색
        candidates = []
        for k in range(1,i):
            n = i - k*k
            if n < 1: break
            candidates.append(dp[n])
            # pruning. 자체 제곱수가 아닌 이상, 후보에서 1이 나오면 그게 최선이다.
            if dp[n]==1: break

        dp[i] = min(candidates)+1

    return dp[N]

N = int(input().strip())
print(solve(N))
