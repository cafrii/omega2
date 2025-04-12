import sys
input = sys.stdin.readline

# 최소 비용 구하기 문제: 이동 시 비용이 증가
# 최대 수익 문제: 이동 시 balance 감소. 도착 시 수익이 증가.
#   -> 비용으로 환산. 수익은 -비용으로 간주. 양의 값이 비용. 음의 값이 수익.
#   최종 비용이 나오면 거기에 -1 곱해서 balance 로 환산.

# INFINITY = (50 * 1_000_000 + margin)
INFINITY = int(1e9)

def solve(N, S, E, edges, earning) -> tuple[int, str]:
    #
    min_costs = [ INFINITY for x in range(N) ]
    in_cycle = [ False for x in range(N) ]

    # 시작 도시에서 수입을 허용?
    min_costs[S] = -earning[S]
    # min_costs[S] = 0

    # relax edges
    for k in range(N):
        for s,e,c in edges:
            if min_costs[s] == INFINITY: continue
            if min_costs[s] + c - earning[e] >= min_costs[e]: continue

            if k < N-1:
                min_costs[e] = min_costs[s] + c - earning[e]
            else: # negative cycle detected
                in_cycle[e] = True

    if min_costs[E] == INFINITY:
        return 0, 'gg'

    if True not in in_cycle:
        return min_costs[E], None

    # 음의 cycle 노드에서 E 까지의 경로가 있는지 체크.
    # 경로 유무만 찾는 간단한 내부 함수를 정의하여 사용
    #
    def can_reach(S, E, visited) -> bool:
        graph = [ [] for x in range(N) ]
        for s,e,c in edges:
            graph[s].append(e)
        #visited = [ False ] * N
        visited[S] = True
        stack = [ S ]
        while stack:
            v = stack.pop()
            if v == E:
                break
            for e in graph[v]:
                if visited[e]: continue
                stack.append(e)
                visited[e] = True
        return visited[E]

    # cycle 이 하나만 있는 게 아닐 수 있음. cycle 에 속한 모든 노드에서 확인해야 함.
    # 단, visited 는 공용화 하여 검색 회수 단축
    visited = [ False ] * N
    for u in range(N):  # 모든 노드에 대해..
        if not in_cycle[u]: continue
        if visited[u]: continue
        if can_reach(u, E, visited):
            return 0, 'Gee'

    return min_costs[E], None


N, S, E, M = map(int, input().split())
edges = []  # (start, end, cost)
for _ in range(M):
    edges.append(tuple(map(int, input().split())))
earning = list(map(int, input().split()))

cost, status = solve(N, S, E, edges, earning)

print(status) if status else print(-cost)

