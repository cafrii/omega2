'''
좀 더 빠른 버전.
dp table 만 먼저 다 계산한 후, 나중에 역추적하여 lcs 문자열 역추적 복원.
'''


A = input()
B = input()
n, m = len(A), len(B)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, m + 1):
    if A[i - 1] == B[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i, j = n, m
LCS = []
while i > 0 and j > 0:
  if A[i - 1] == B[j - 1]:
    LCS.append(A[i - 1])
    i ,j = i - 1, j - 1
  elif dp[i - 1][j] > dp[i][j - 1]:
    i -= 1
  else:
    j -= 1
print(dp[n][m])
print("".join(reversed(LCS)))
