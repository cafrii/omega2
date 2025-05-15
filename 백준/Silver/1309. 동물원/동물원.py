
import sys
input = sys.stdin.readline

MAX_N = 100_000
MOD = 9901

def solve(N):
    dp = [ [0,0,0] for k in range(N+1) ]
    '''
        dp[k] 는 N==k 일 때의 정보. 크기 3의 리스트
        dp[k][0] 은 마지막행 (row=k-1) 에 배치를 안하는 경우
        dp[k][1] 은 마지막행 (row=k-1) 에 왼쪽에만 배치
        dp[k][2] 은 마지막행 (row=k-1) 에 오른쪽에만 배치
        dp[0] 은 미사용
    '''
    dp[1] = [ 1, 1, 1 ]

    for k in range(2, N+1):
        dp[k][0] = sum(dp[k-1]) % MOD
        dp[k][1] = (dp[k-1][0] + dp[k-1][2]) % MOD
        dp[k][2] = (dp[k-1][0] + dp[k-1][1]) % MOD

    return sum(dp[N]) % MOD


N = int(input().strip())
print(solve(N))
