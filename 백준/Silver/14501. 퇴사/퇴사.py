
def solve(Ti:list, Pi:list):
    # dynamic programming version
    N = len(Ti)

    max_price = [ 0 ] * N
    # max_price[i] 는 day i 부터 고려했을 때의 최대 이익

    def get_max_price(start):
        # easy access method
        return max_price[start] if 0 <= start < N else 0

    for k in range(N-1, -1, -1):
        # take
        p1 = (Pi[k] if k + Ti[k] <= N else 0) + get_max_price(k + Ti[k])
        # skip
        p2 = get_max_price(k+1)
        max_price[k] = max(p1, p2)

    return max_price[0]



N = int(input().strip())
Ti = [0] * N
Pi = [0] * N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())

print(solve(Ti, Pi))
