import sys

MOD = 1_000_000_009

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        n,m = map(int, input().split())
        A.append((n, m))
    return A,

def solve(A:list[tuple[int,int]])->list[int]:
    '''
    Args:    A: [ (n,m), .. ]
    Returns: list of answers
    '''
    max_n = max(A, key=lambda x:x[0])[0]
    alloc_n = max(4, max_n)

    dp = [ [0]*(alloc_n+1) for k in range(alloc_n+1) ]
    # dp[k]: k 를 1,2,3 합으로 나타내는 방법 중 m개만 사용하는 경우의 수

    dp[1][1] = 1
    dp[2][1:3] = [1,1]
    dp[3][1:4] = [1,2,1]

    for k in range(4, max_n+1):
        for m in range(k, 0, -1): # m: k ~ 1
            dp[k][m] = (dp[k-1][m-1] + dp[k-2][m-1] + dp[k-3][m-1]) % MOD
            if dp[k][m] == 0: break # early exit

    ans = [ (sum(dp[n][:m+1]) % MOD) for n,m in A ]
    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
