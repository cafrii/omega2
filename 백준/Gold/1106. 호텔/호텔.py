
import sys

def get_input():
    input = sys.stdin.readline
    C,N = map(int, input().split())
    A = []  # A: cost/profit info of all city
    for _ in range(N):
        c,p = map(int, input().split()) # cost, profit
        A.append((c, p))
    return C,A


INF = int(1e9)

def solve_dp(T:int, A:list[tuple[int,int]])->int:
    '''
    T: target profit (number of extra customer wanted)
    A: array of (cost, profit) of each city

    cost 와 customer 가 둘 다 c 이니까 헷갈림.
    cost (비용) 과 profit (이윤) 으로 간주. 이윤을 target profit 이상 낼 수 있도록 계산.
    '''
    N = len(A)
    max_profit = max(p for c,p in A)

    dp = [ INF ] * (T + max_profit + 1)
    # dp[k]: k 명의 고객 (profit) 을 얻기 위한 최소 비용
    dp[0] = 0
    for i in range(N):
        cost, profit = A[i]
        for j in range(profit, T+profit):
            if dp[j-profit] >= INF: continue
            dp[j] = min(dp[j], dp[j-profit] + cost)

    return min(dp[T:])

if __name__ == '__main__':
    inp = get_input()
    # print(solve_backtrack(*inp))
    print(solve_dp(*inp))
