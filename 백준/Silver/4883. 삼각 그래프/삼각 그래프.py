
import sys

def get_input():
    input = sys.stdin.readline
    C = [] # test cases
    while True:
        N = int(input().rstrip())
        if N == 0: break
        A = []
        for _ in range(N):
            a,b,c = map(int, input().split())
            A.append([a,b,c])
        C.append(A)
    return C,

def solve(A:list[list[int]])->int:
    '''
    Args: A: cost matrix, dim: N by 3
    Returns: min cost, from G[0][1]->G[N-1][1]
    '''
    MAX_C = 1000
    N = len(A)

    dp = [ [0,0,0] for _ in range(N) ]
    # dp[k][j]: accululated cost at graph location of row k, column j

    dp[0][0] = MAX_C #A[0][0]
    dp[0][1] = A[0][1]
    dp[0][2] = A[0][1] + A[0][2]

    for k in range(1, N): # k: 1 ~ N-1
        dp[k][0] = min( dp[k-1][0], dp[k-1][1] ) + A[k][0]
        dp[k][1] = min( dp[k][0], dp[k-1][0], dp[k-1][1], dp[k-1][2] ) + A[k][1]
        dp[k][2] = min( dp[k][1], dp[k-1][1], dp[k-1][2] ) + A[k][2]

    return dp[N-1][1]

if __name__ == '__main__':
    C, = get_input()
    print('\n'.join( f'{i+1}. {solve(c)}' for i,c in enumerate(C) ))
