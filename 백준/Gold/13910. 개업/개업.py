
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    W = list(map(int, input().split())) # wok sizes
    assert len(W) == M, "wrong wok num"
    return N,W

def solve(N:int, W:list[int])->int:
    '''
    Args
        N: target num to compose. <= 10_000
        W: list of wok sizes. len <= 100, 1<=w<=N
    '''
    ws = set(W) # wok size set. 단독 사용

    # 웍 두개 조합 사용. 총합 만 중요.
    for j in range(1, len(W)):
        for i in range(j):
            ws.add(W[i]+W[j])

    INF = max(10_001, N+1)
    dp = [ INF ] * (N+1)
    # dp[k]: k 인분 식사를 준비하기 위해 필요한 최소 요리 회수
    dp[0] = 0

    for k in range(1, N+1):
        # dp[1] 부터 dp[N] 까지 단계적으로 계산
        for w in ws: # 모든 wok 조합에 대해서
            if w <= k:
                dp[k] = min(dp[k], dp[k-w]+1)

    return dp[N] if dp[N] < INF else -1


if __name__ == '__main__':
    print(solve(*get_input()))
