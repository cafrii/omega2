import sys

def get_input():
    input = sys.stdin.readline
    N,T = map(int, input().split())
    A = []
    for _ in range(N):
        d,m = map(int, input().split())
        A.append((d, m)) # (days, penalty)
    return N,T,A

def solve2(N:int, T:int, A:list[tuple[int,int]])->int:
    '''
    Args:
        T: allowed days
        A: [ (days, penalty), ...]
    Returns:
    Logic:
        dp, dpx 두 벌 대신 dp 한 벌만 관리.
        t iteration 방향을 역방향으로 하면 됨.
    '''
    total_penalty = sum(t[1] for t in A)
    dp = [0] * (T+1)
    # dp[t]는 t라는 시간(날짜)가 주어졌을 때 얻을 수 있는 최대 가치(벌금)의 합.

    for c,v in A:  # cost and value
        for t in range(T, c-1, -1):
            # if dp[t-c] + v > dp[t]:
            #     dp[t] = dp[t-c] + v
            dp[t] = max(dp[t], dp[t-c]+v)

    # 제출 기한을 꼭 다 채워야 하는 것은 아니므로, 전체 dp 중에서 최대 값을 찾는다.
    return total_penalty - max(dp)

if __name__ == '__main__':
    print(solve2(*get_input()))

