import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    T,P = [],[]
    for _ in range(N):
        ti,pi = map(int, input().split())
        T.append(ti); P.append(pi)
    return N,T,P

def solve(N:int, T:list[int], P:list[int])->int:
    '''
    Args:
        N: days, T: list of required days, P: list of profits
    Returns: maximum profit

    모든 배열의 base를 0 으로 간주한다.
    날짜도 1일 ~ N일 대신, 0일 ~ N-1일 로 부름.
    '''

    dp = [0] * (N+1)
    # dp[k]: k 일 부터 N-1 일까지 일하는 경우의 최대 수익
    # 우리가 원하는 최종 답은 dp[0].
    # dp[N] 자리까지 준비한 이유는 아래 계산 편의를 위해서임.

    for k in range(N-1, -1, -1):  # k: N-1 ~ 0
        # 날짜 k 에 일을 하면 P[k] 수익. 하지만 남은 일 수가 T[k] 이상이어야 함
        dp[k] = max(
            dp[k+1], # k날에 일 안하는 경우
            (P[k] + dp[k+T[k]]) if k+T[k]<=N else 0,
        )
    return dp[0]


if __name__ == '__main__':
    print(solve(*get_input()))
