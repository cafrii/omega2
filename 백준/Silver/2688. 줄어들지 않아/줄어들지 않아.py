import sys

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    A = []
    for _ in range(C):
        N = int(input().rstrip())
        A.append(N)
    return A,

def solve(A:list[int])->list[int]:
    '''
    '''
    MAX_N = 64
    max_n = max(A) # real max

    dp = [ [0]*10 for _ in range(MAX_N+1) ]
    # dp[k][j]는 길이 k 인 non-decreasing 숫자들 중, 끝자리가 j 인 것들의 개수

    dp[1] = [1]*10  # 길이가 1이면 한 가지 경우 밖에 없음. 그냥 그 숫자.

    for k in range(2, max_n+1):
        # dp[k][0] = dp[k-1][0]
        # dp[k][1] = dp[k-1][0] + dp[k-1][1]
        # ...
        for j in range(10): # j: 0 ~ 9
            dp[k][j] = sum( dp[k-1][:j+1] )

    return [ sum(dp[a]) for a in A ]

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
