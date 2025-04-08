# based on dijkstra, apply some modification
from heapq import heappop, heappush
import sys

MAX_NK = 100_000

def solve(N, K):
    if N == K:
        return 0
    if K < N:
        return N-K

    que = [] # priority minimum que
        # element of que: tuple (cost, node)
        # cost: number of seconds elapsed since start.

    COST_MAX = MAX_NK + 1
    min_cost = [ COST_MAX ] * (MAX_NK + 1)

    # starting from node N, cost 0
    heappush(que, (0, N))

    while que:
        cost, now = heappop(que)
        if now == K: # reached to target.
            return cost

        if min_cost[now] < cost:
            continue

        # consider next
        # 1. jump case, only when we are ahead of K
        next_node, next_cost = 2*now, cost
        if 0 < now < K and \
                0 < next_node <= MAX_NK and \
                next_cost < min_cost[next_node]:
            min_cost[next_node] = next_cost
            heappush(que, (next_cost, next_node))

        # 2. walk case
        choices = [ now-1, now+1 ] if now < K else [ now-1 ]
        next_cost = cost + 1
        for next_node in choices:
            if next_node < 0 or next_node > MAX_NK:
                continue
            if min_cost[next_node] <= next_cost:
                continue
            min_cost[next_node] = next_cost
            heappush(que, (next_cost, next_node))

    # cannot reach K
    return -1


N, K = map(int, input().split())
print(solve(N, K))

