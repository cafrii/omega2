
import sys

MOD = 1_000_000_000

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N,

def solve_slow(N:int)->int:
    '''
    일반 dp.  O(N logN)
    '''
    dp = [1] * (N+1)
    # dp[j]: j 를 만드는 경우의 수
    # 1 만을 사용하는 경우는 항상 1가지가 존재하므로 초기 값으로 시작.
    # 그런 후, 앞으로 1 사용하는 경우는 빼고 생각.

    tx = 1  # two's exponentiate
    while tx <= N:
        tx = 2*tx  # tx = 2^x, { 2, 4, 8, 16, ..}

        # 모든 ~N 에 대하여 적용. tx 를 하나 추가하는 경우를 카운트.
        for k in range(tx, N+1):
            dp[k] = (dp[k] + dp[k-tx]) % MOD

    return dp[N]


def solve_opt(N:int)->int:
    '''
    2의 멱수 시리즈의 특징을 최대한으로 활용한, O(N) 시간 풀이
    '''
    dp = [0] * (N+1)

    dp[1] = 1 # 초기 값

    for k in range(2, N+1):
        if (k & 1): # 홀수
            dp[k] = dp[k-1]  # n-1 (짝수) 을 만드는 모든 경우에 +1
        else: # 짝수
            dp[k] = (dp[k-1] +  # n-1 (홀수) 만드는 모든 경우에 +1
                     dp[k//2]   # n//2 를 만드는 모든 경우에 x2
                    ) % MOD
    return dp[N]


if __name__ == '__main__':
    print(solve_opt(*get_input()))
