
def get_input():
    import sys
    input = sys.stdin.readline
    N,X = map(int, input().split())
    return N,X

def solve(N:int, X:int)->int:
    '''
    Args: N: level
    Returns: number of patties of lower X layers of level-N burger
    '''
    # 최대 recursive depth 는 50을 넘지 않음.

    dp = [ [0,0] for _ in range(N+1) ]
    # dp[k][0]: size of this level burger
    # dp[k][1]: number of patties of this level burger

    dp[0] = [1, 1] # P
    dp[1] = [5, 3] # BPPPB
    # dp[2] = [13, 7]

    for k in range(2, N+1):
        dp[k][0] = dp[k-1][0]*2 + 3
        dp[k][1] = dp[k-1][1]*2 + 1

    def count_patty(n:int, x:int)->int:
        # 레벨 n 버거의 아래 x 장에 포함된 패티 수를 리턴
        if n <= 1:
            if n < 0: return 0
            if n == 0: return 1 if x >= 1 else 0
            # n == 1
            return 0 if x<=1 else x-1 if x<=4 else 3

        # 먼저 레벨 n 버거의 구성 파악
        prev_sz = dp[n-1][0]
        #  B (n-1 burger, prev_sz) P (prev_sz) B

        if x <= 1+prev_sz:
            return count_patty(n-1, x-1)
        if x < 1+prev_sz+1+prev_sz:
            return count_patty(n-1, x-1-prev_sz-1) + dp[n-1][1] + 1
        else:
            return dp[n][1]

    return count_patty(N, X)

if __name__ == '__main__':
    print(solve(*get_input()))

