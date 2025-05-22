
K = int(input().strip())

dp = [ [0,0] for _ in range(K+1) ]

# dp[k][0]: count of A in step k
# dp[k][1]: count of B

dp[0][0] = 1

for k in range(1, K+1):
    # A -> B
    # B -> BA
    dp[k][0] = dp[k-1][1]
    dp[k][1] = dp[k-1][0] + dp[k-1][1]

print(dp[K][0], dp[K][1])
