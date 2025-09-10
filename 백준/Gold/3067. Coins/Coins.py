
import sys

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    def gen():
        for _ in range(C):
            N = int(input().rstrip()) # number of coin types
            A = list(map(int, input().split()))
            #assert len(A)==N, "wrong A"
            M = int(input().rstrip()) # goal, 1~10_000
            yield A,M
    return gen() # return iterator

def solve_dp(A:list[int], M:int)->int:
    '''
    Args:
        A: coin types
        M: goal
    Returns: number of all cases to compose M using A[]-typed coins
    '''
    N = len(A) # sorted by ascending order
    dp = [0] * (M+1)
    # dp[k]: number of cases to compose value k

    dp[0] = 1
    for cv in A: # for each coin value
        for j in range(cv, M+1):
            dp[j] += dp[j-cv]
    return dp[M]

if __name__ == '__main__':
    it = get_input()
    print('\n'.join(map(str, (solve_dp(a,m) for a,m in it) )))
