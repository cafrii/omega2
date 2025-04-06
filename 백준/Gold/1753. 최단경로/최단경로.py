import sys
from heapq import heappop, heappush

input = sys.stdin.readline

INF = int(1e8) # should be > max E * max w

def solve(graph, start):
    dist = [INF] * (V + 1)
    # dist[k]: 'start'에서부터 k까지의 최단 거리(비용)
    # 초기값을 가장 큰 값으로 설정.

    dist[start] = 0
    # dist 가 visited 역할도 수행함.

    hq = [(0, start)] # (cost, node)
    # 갱신 회수를 줄이기 위해서 최소 heapq 사용

    while hq:
        cost, node = heappop(hq)
        # cost: 노드 node 까지 오는 최단 경로 (비용)

        # 추가 할 때는 최소였겠지만 그 이후에 더 작은 경로로 업데이트 되었을 수 있으므로
        # 한번 더 확인해야 함.
        if dist[node] < cost:
            continue

        for v, w in graph[node]:
            if dist[v] > cost + w:
                dist[v] = cost + w
                heappush(hq, (dist[v], v))
    #
    return dist


V, E = map(int, input().split())
# V: 1~20_000, E: 1~300_000

K = int(input()) # start node

graph = [[] for _ in range(V + 1)] # [0] is not used
# V**2 보다 E가 훨씬 작으므로, 2차원 배열 대신 그냥 간선 리스트로 만든다.
# 어차피 모든 간선을 다 확인해야 하므로 retrieve 시간은 상관 없음.

for _ in range(E):
    u, v, w = map(int, input().split())
    if u == v:
        continue
    graph[u].append((v, w))

dist = solve(graph, K)

for i in range(1, V + 1):
    print("INF") if dist[i] == INF else print(dist[i])
