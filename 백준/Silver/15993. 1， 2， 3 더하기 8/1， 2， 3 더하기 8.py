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
    Args:
        list of test case. [ n1, n2, .. ]
    Returns:
        answer string list. [ "<cases_odd> <cases_even>", ... ]
    '''
    max_n = max(A)
    alloc_n = max(4, max_n)

    dp = [ [0,0] for k in range(alloc_n+1) ]
    # dp[k][0]: 1,2,3 을 짝수개 사용하여 n을 만든 경우의 수
    # dp[k][1]: 홀수개 사용

    # dp[0][*] = 0
    dp[1][0] = 0
    dp[1][1] = 1 # 1

    dp[2][0] = 1 # 1+1
    dp[2][1] = 1 # 2

    dp[3][0] = 2 # 2+1 1+2
    dp[3][1] = 2 # 1+1+1 3

    # dp[4][0] = 4 # 1+1+1+1 3+1 2+2 1+3
    # dp[4][1] = 3 # 2+1+1 1+2+1 1+1+2

    # dp[k] 는 dp[k-1]에 +1, dp[k-2]에 +2, dp[k-3]에 +3 하는 경우가 존재함.
    # 각 경우마다 숫자 하나만을 추가하는 것이므로 홀/짝이 바뀐다는 점에 유의.

    for k in range(4, max_n+1): # k: 4 ~ max_n
        dp[k][0] = (dp[k-1][1] + dp[k-2][1] + dp[k-3][1]) % MOD
        dp[k][1] = (dp[k-1][0] + dp[k-2][0] + dp[k-3][0]) % MOD

    return [ f'{dp[n][1]} {dp[n][0]}' for n in A ]

if __name__ == '__main__':
    print('\n'.join( solve(*get_input()) ))
