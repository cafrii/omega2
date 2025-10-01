import sys

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    C = list(map(int, input().split()))
    return N,K,C


def solve_dp(N:int, K:int, C:list[int])->int:
    MAX_V = N+1
    dp = [MAX_V] * (K+1)
    # dp[k]: 카페인 k를 맞추는 커피 최소 잔 수
    dp[0] = 0
    for c in C:
        for k in range(K, c-1, -1):
            if dp[k-c] == MAX_V: continue
            dp[k] = min(dp[k], dp[k-c]+1)
    return dp[K] if dp[K]<MAX_V else -1


def solve_dp3(N:int, K:int, C:list[int])->int:
    MAX_V = N+1
    dp = [ [MAX_V] * (K+1) for _ in range(N+1) ]
    # dp[n][k]: n번째 커피잔 까지만 고려했을 때, 카페인 k를 맞추는 커피 최소 잔 수
    maxk = 0
    dp[0][0] = 0

    for i,c in enumerate(C):
        dp[i+1][0] = 0
        maxk = min(K, maxk + c)
        for k in range(maxk, -1, -1): # k: maxk ~ c
            if k < c:
                dp[i+1][k] = dp[i][k]
            else:
                dp[i+1][k] = min(dp[i][k], dp[i][k-c]+1)

    return dp[N][K] if dp[N][K]<MAX_V else -1


def solve_dp5(N:int, K:int, C:list[int])->int:
    '''
    Returns:
        min number of coffee. -1 if no answer
    '''
    # pre-processing.
    # 계산에 도움이 안되는 것들 제거.
    C = [ c for c in C if c <= K ]
    N = len(C)

    # edge case들 별도 처리
    if sum(C) < K: return -1
    if K == 0: return 0

    MAX_V = N+1

    dp = [MAX_V] * (K+1)
    # dp[k]: 카페인 k를 맞추는 커피 최소 잔 수
    dp[0] = 0
    # c 루프의 초기에는 대부분 k 루프는 공회전. 따라서 k 범위를 최대한 줄여주면 도움이 된다.
    maxk = 0
    for c in C:
        # c 만큼의 카페인이 함유된 커피 1잔.
        maxk = min(K, maxk+c)
        for k in range(maxk, c-1, -1):
            dp[k] = min(dp[k], dp[k-c]+1)

    return dp[K] if dp[K]<MAX_V else -1


def solve_backtrack(N:int, K:int, C:list[int])->int:
    '''
    using backtracking
    동작을 하긴 하는데, N의 크기가 23 부터 경과 시간이 1초를 초과함.
    '''
    C.sort(reverse=True)

    MAX_CUPS = N+1
    min_cups = MAX_CUPS
    used = [0]*N

    def back(index:int, num_used:int, caffsum:int)->bool:
        '''
        Args:
            cup index: 0 ~ N-1
            caffsum: total accumulated caffein amount
        '''
        nonlocal min_cups
        if caffsum == K:
            min_cups = min(min_cups, num_used)
            return True
        if index >= N:
            return False
        # prunning, early drop
        if num_used >= min_cups:
            return False
        # used case
        if caffsum + C[index] <= K:
            used[index] = 1
            back(index+1, num_used+1, caffsum + C[index])
            used[index] = 0
        # not-used case
        back(index+1, num_used, caffsum)

    back(0, 0, 0)
    return min_cups if min_cups <= N else -1


if __name__ == '__main__':
    print(solve_dp5(*get_input()))


