
def solve_recursive(Ti:list, Pi:list):
    N = len(Ti)

    #   day  1   2   ...  N-1   N
    #  index 0   1   ...  N-2  N-1
    #
    # 모든 단위는 0-base 로.

    def get_max_profit(start:int):
        # start 날 부터 고려하였을 때의 최대 이익

        if start > N-1:
            return 0
        if start == N-1:
            return Pi[start] if Ti[start] == 1 else 0
        # start < N-1

        # case 1: take
        #  if end day <= N-1
        if start + (Ti[start]-1) <= N-1:
            p1 = Pi[start] + get_max_profit(start + Ti[start])
        else:
            p1 = 0 # cannot take this job

        # case 2: skip
        p2 = get_max_profit(start + 1)

        # print(f"({start}) take[{start}]={p1}, skip[{start}]={p2}, max={max(p1, p2)}")
        return max(p1, p2)

    return get_max_profit(0)


N = int(input().strip())
Ti = [0] * N
Pi = [0] * N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())

print(solve_recursive(Ti, Pi))

