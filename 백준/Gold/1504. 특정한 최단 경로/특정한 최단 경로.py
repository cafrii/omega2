
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

MAX_N = 800
MAX_LC = 1000 # link cost

graph = [ [] for _ in range(MAX_N+1) ]
    # graph[s] = [ (v1, c1), (v2, c2), .. ]

def find_path(S, E) -> int:
    # S 에서 시작하여 V 를 경유하여 E에 도달하는 최소 비용 경로 리턴
    # dijkstra 이용

    min_cost = [ MAX_N * MAX_LC + 1 ] * (MAX_N+1)
        # min_cost[0] is not used.
    que = []
    heappush(que, (0, S))

    while que:
        cost,now = heappop(que)
        if now == E:
            return cost
        if min_cost[now] < cost:
            continue
        for e,c in graph[now]:
            next_cost = cost + c
            if min_cost[e] < next_cost:
                continue
            min_cost[e] = next_cost
            heappush(que, (next_cost, e))
    #
    return -1

def find_path2(S, V:list) -> int:
    start = S
    if not V:
        return -1
    cost = 0 # total accumulated cost
    for v in V:
        c = find_path(start, v)
        if c < 0:
            return -1
        cost += c
        start = v
    return cost

def solve(N, v1, v2) -> int:
    # 노드 1 에서, 노드 v1, v2 를 (순서 무관) 경유한 후 N 에 도달하는 최단 거리 구하기
    c1 = find_path2(1, [v1, v2, N])
    c2 = find_path2(1, [v2, v1, N])
    if c1 < 0 and c2 < 0:
        return -1
    if c1 < 0:
        return c2
    if c2 < 0:
        return c1
    return min(c1, c2)

N,E = map(int, input().split())
for _ in range(E):
    a,b,c = map(int, input().split())
    if a == b: continue
    graph[a].append((b, c))
    graph[b].append((a, c)) # 양방향 그래프

v1,v2 = map(int, input().split())

print(solve(N, v1, v2))

