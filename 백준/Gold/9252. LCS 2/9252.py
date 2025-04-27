'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초 (하단 참고)	256 MB	51459	19656	15094	38.671%

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

'''



import sys
input = sys.stdin.readline

a1 = input().strip()
a2 = input().strip()

len1 = len(a1)
len2 = len(a2)

# 인덱싱의 편의를 위해 prefix 붙임. 이제 a1[1] ~ a1[len1] 으로 접근.
a1, a2 = ' '+a1, ' '+a2

# create dp table
# dp[i][j]: list of lcs_len, lcs
#      lcs_len: a1 의 첫 i 개 문자와 a2 의 첫 j개 문자의 LCS 길이
#      lcs: lcs 문자열
#      dp[0][*] 과 dp[*][0] 은 항상 0,'' 으로 고정됨.
dp = [ [ [0, ''] for j in range(len2 + 1) ] for k in range(len1 + 1)]

# populate dp table
for j in range(1, len1 + 1):
    for k in range(1, len2 + 1):
        # dp[1][1] 부터 채우기 시작함.
        # a1 의 i번째 문자와 a2 의 k번째 문자가 같은 경우
        if a1[j] == a2[k]:
            # 현재 위치의 문자를 LCS에 포함
            dp[j][k][0] = dp[j-1][k-1][0] + 1
            dp[j][k][1] = dp[j-1][k-1][1] + a1[j]
        else: # 문자가 다른 경우
            if dp[j-1][k][0] >= dp[j][k-1][0]:
                dp[j][k][:] = dp[j-1][k]
                # 어차피 한번 기록된 후에 바뀌지 않을 거라서 그냥 []를 붙이는 것도 가능함. 메모리 절약 가능.
                # dp[j][k] = dp[j-1][k]
            else:
                dp[j][k][:] = dp[j][k-1]

print(dp[len1][len2][0])
if dp[len1][len2][0]:
    print(dp[len1][len2][1])


'''
예제 입력 1
ACAYKP
CAPCAK

예제 출력 1
4
ACAK


'''