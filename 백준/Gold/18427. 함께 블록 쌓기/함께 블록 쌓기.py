import sys

def get_input():
    input = sys.stdin.readline
    N,M,H = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
        #assert len(A[-1]) <= M
    return N,M,H,A

def solve(N:int, M:int, H:int, A:list[list[int]])->int:
    '''
    '''
    MOD = 10_007

    dp = [0]*(H+1)
    dp[0] = 1  # 높이 0을 만드는 경우는 1가지

    for k in range(1, N+1):
        dpx = dp[:]  # copy
        # 학생 k가 가지고 있는 블럭의 높이는 A[k-1]
        for a in A[k-1]:
            for h in range(a, H+1):
                dpx[h] = (dpx[h] + dp[h-a]) % MOD
        dp = dpx

    return dp[H]

if __name__ == '__main__':
    print(solve(*get_input()))
