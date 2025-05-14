import sys
input = sys.stdin.readline

MAX_N = 100_000
# n은 양수이며 100,000보다 작거나 같다.

MOD = 1_000_000_009

'''
dp[k]: 정수 k를 1,2,3 의 합으로 나타내는 방법의 수 계산에 필요한 정보
    dp[k][0]: 위 조건의 수 중 끝자리가 1로 끝나는 경우의 수
    dp[k][1]: 위 조건의 수 중 끝자리가 2로 끝나는 경우의 수
    dp[k][2]: 위 조건의 수 중 끝자리가 3로 끝나는 경우의 수
dp[0] 은 미사용.
'''
dp = [ [0,0,0] for k in range(MAX_N+1) ]

dp[1] = [ 1, 0, 0 ] # 1
dp[2] = [ 0, 1, 0 ] # 2
dp[3] = [ 1, 1, 1 ] # 1+2, 2+1, 3

dp_valid_until = 3

def solve(N):
    '''

    '''
    global dp, dp_valid_until

    if dp_valid_until < N:
        # populate dp[] until index N
        #
        for n in range(dp_valid_until+1, N+1):
            dp[n][0] = (dp[n-1][1] + dp[n-1][2]) % MOD # +1 를 하려면 끝자리 1은 사용할 수 없음.
            dp[n][1] = (dp[n-2][0] + dp[n-2][2]) % MOD # +2 하는 경우
            dp[n][2] = (dp[n-3][0] + dp[n-3][1]) % MOD # +3 하는 경우

        dp_valid_until = N

    return sum(dp[N]) % MOD

# main

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(solve(N))

