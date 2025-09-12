import sys

MOD = 1_000_000_009

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        n = int(input().rstrip())
        A.append(n)
    return A,

def solve(A:list[int])->list[str]:
    '''
    Returns: answer. list of string.
    '''
    max_n = max(A)
    alloc_n = max(max_n, 5)
    dp = [0]*(alloc_n + 1)

    '''
    dp[k]는 다음과 같은 조합으로 생성될 수 있음.
        dp[k-2] 의 양쪽에 1+...+1 을 더하기
        dp[k-4] 의 양쪽에 2+...+2
        dp[k-6] 의 양쪽에 3+...+3
    dp[6] 까지는 미리 구해두고, dp[7] 부터 점화식.
    '''
    dp[0] = 1  # 이 자체는 정답에 사용이 안되지만 x+?+x 형태로 계산에는 사용될 수 있음.
    dp[1] = 1  # 1
    dp[2] = 2  # 1+1  2
    dp[3] = 2  # 1+1+1  3
    dp[4] = 3  # 1+1+1+1 1+2+1  2+2
    dp[5] = 3  # 1+1+1+1+1 1+3+1  2+1+2
    # dp[6] = 6 # 1+1+1+1+1+1 1+1+2+1+1 1+2+2+1  2+1+1+2 2+2+2  3+3

    for k in range(6, max_n+1):
        dp[k] = (dp[k-2] + dp[k-4] + dp[k-6]) % MOD
        
    return [ str(dp[n]) for n in A ]

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))
