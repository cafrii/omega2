
'''
using simple dp

'''

import sys

# 표준 입력에서 두 문자열을 읽어옵니다.
# rstrip() 또는 strip()을 사용하여 끝에 있을 수 있는 개행 문자를 제거합니다.
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# 두 문자열의 길이를 구합니다.
len1 = len(str1)
len2 = len(str2)

# DP 테이블을 생성합니다. 크기는 (len1 + 1) x (len2 + 1) 입니다.
# 0으로 초기화합니다. dp[i][j]는 str1의 첫 i개 문자와 str2의 첫 j개 문자의 LCS 길이를 저장합니다.
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

# DP 테이블을 채웁니다.
# i는 str1의 인덱스+1, j는 str2의 인덱스+1에 해당합니다.
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # str1의 i번째 문자와 str2의 j번째 문자가 같은 경우
        # (문자열 인덱스는 0부터 시작하므로 i-1, j-1을 사용)
        if str1[i - 1] == str2[j - 1]:
            # 대각선 위의 값(dp[i-1][j-1])에 1을 더합니다.
            # 이는 현재 문자가 LCS에 포함됨을 의미합니다.
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 문자가 다른 경우
        else:
            # 위쪽 값(dp[i-1][j])과 왼쪽 값(dp[i][j-1]) 중 더 큰 값을 선택합니다.
            # 이는 현재 문자 중 하나를 포함하지 않는 경우의 LCS 길이 중 최대값을 따릅니다.
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 최종 결과는 DP 테이블의 가장 오른쪽 아래 값에 저장됩니다.
# 즉, str1 전체와 str2 전체의 LCS 길이입니다.
print(dp[len1][len2])

'''
a = input()
b = input()
n = len(a)
m = len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])
'''
