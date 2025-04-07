import sys
import heapq

input = sys.stdin.readline

MAX_M = 100_000
MAX_C0 = 100_000
MAX_COST = 1e10 + 1 # MAX_M * MAX_C0 보다 작아야 함

def solve(graph, S, E):
    #
    min_cost = [ MAX_COST ] * len(graph)
        # min_cost[k]: 노드 S 에서 노드 k 에 이르는 "전체 경로"의 최소 비용.
        # 이론상 비용의 최대 값으로 초기화 함.

    hq = [ (0, S) ] # minimum heap que
    # S 에서 출발함. 자기 자신까지의 cost 는 0
    # 반드시 순서는 (cost, node) 순서가 되어야 함. 그래야 min_cost 갱신을 최소화 할 수 있음.

    # print(graph)

    while hq:
        # print(f'q: {hq}')
        cost, node = heapq.heappop(hq)
        # cost: 이 노드까지의 최소 전체 경로 비용
        # node: 현재 방문(검토)중인 노드

        # 실수하기 쉬운 지점. q 에 넣을 때는 조건에 맞춰 넣었더라도, 그 동안 상황이 변했을 수 있으므로 다시 한번 더 체크.
        if min_cost[node] < cost:
            continue

        # 현재의 노드에서 다음 인접 노드들까지의 간선에 대해 고려
        # print(f'[{node}: c{cost}] checking {','.join([ str(x) for x,y in graph[node]])}')
        for (nn, lc) in graph[node]:
            # nn: next_node, lc: link_cost
            if nn == node:
                continue
            new_cost = cost + lc
            if min_cost[nn] <= new_cost:
                continue
            min_cost[nn] = new_cost
            #print(f'  update [{nn}: c{new_cost}]')
            # nn 의 cost 가 갱신되었으므로, 다시 한번 더 재검토가 필요함.
            heapq.heappush(hq, (new_cost, nn))

    return min_cost[E]



N = int(input().strip())
M = int(input().strip())

graph = [ [] for _ in range(N+1) ] # graph[0] not used

for _ in range(M):
    s,e,c = map(int, input().split())
    if not (1 <= s <= N and 1 <= e <= N):
        continue
    graph[s].append((e, c))
        # 그래프에는 (next_node, link_cost) 튜플로 저장됨.

S,E = map(int, input().split())

print(solve(graph, S, E))
