import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''
    dp = [ [0,0] for _ in range(N) ]
    # dp[k][0] 는 A[k]를 끝자리로 하는 부분수열 중 1의 초과 개수 (1개수-2개수)
    # dp[k][1] 는 ... 2의 초과 개수 (2 개수 - 1 개수)

    dp[0][0] = (1 if A[0]==1 else 0)
    dp[0][1] = (1 if A[0]==2 else 0)

    maxval = abs(dp[0][0] - dp[0][1])

    for k in range(1, N):
        # 끝자리가 1로 끝나는 것. 다시 1이 오면 하나 증가됨.
        dp[k][0] = ((dp[k-1][0] + 1) if A[k]==1 else \
                    max(dp[k-1][0] - 1, 0))
        # 끝자리가 2로 끝나는 것.
        dp[k][1] = ((dp[k-1][1] + 1) if A[k]==2 else \
                    max(dp[k-1][1] - 1, 0))
        maxval = max(maxval, abs(dp[k][0] - dp[k][1]))

    return maxval

if __name__ == '__main__':
    print(solve(*get_input()))
