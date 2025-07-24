
import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    N = int(input().strip())
    C = [] # C[k]: cost of painting house-k, zero-based.
    for _ in range(N):
        r,g,b = map(int, input().split())
        C.append((r, g, b))
    return C


MAX_COST = int(1e7) # > 1000*1000

def solve_dp(C:list[tuple[int,int,int]])->int:
    '''
    첫번째 집의 조건이 마지막 집과 연계되어 있으므로, 초기 최적값을 확정할 수 없다.
    따라서 세가지 모두 시도한 후 선택해야 한다.
    '''
    N = len(C)
    min_costs = []

    # try three possible cases.
    for h in range(3):
        # h: 첫번째 집의 색상을 각 세 가지 경우를 가정하여 반복 계산.

        dp = [ [0,0,0] for k in range(N) ]
        # dp[k]: 0부터 k번째 집까지 이미 칠했고, 이제 k+1번째 집을 칠 할 차례임.
        #        dp[k][*]는 마지막 k번째 집이 각각 r, g, b 로 칠해진 경우, 각각의 최소 비용

        # first house. 현재 계산 중인 색상 이외에는 선택이 불가하도록 최대 비용 설정.
        dp[0][:] = [ (C[0][j] if j==h else  MAX_COST) for j in range(3) ]

        for k in range(1,N):
            # dp[k] 번째 집을 r 로 칠하려면 dp[k-1] 집이 g 또는 b 이어야 함. 이 두가지 중 최소 비용 선택.
            dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + C[k][0]
            dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + C[k][1]
            dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + C[k][2]

        # 마지막 집. 첫번째 집과 같은 색상은 선택 불가함.
        dp[N-1][h] = MAX_COST
        min_costs.append(min(dp[N-1]))

    return min(min_costs)


if __name__ == '__main__':
    inp = get_input()
    print(solve_dp(inp))
