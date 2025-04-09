


from collections import defaultdict
from heapq import heappop, heappush

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

MAX_COST = 10_001

def solve(D:int, graph:dict):

    # dijkstra 알고리즘 적용.
    # 노드 0 에서 노드 D 까지 도달하기 위한 최소 길이를 구해야 함.
    # graph 에는 0->*

    min_cost = dict()
    for key in graph:
        min_cost[key] = MAX_COST
    min_cost[D] = MAX_COST
    #log("min_cost: %s", min_cost)

    que = []  # 요소 타입: tuple(누적_cost, 노드)
    heappush(que, (0, 0))

    while que:
        #log("que: %s", que)

        cost, now = heappop(que)
        #log("cost %d: node %d", cost, now)
        if now == D:
            return cost

        # 큐 안에 있는 동안 상황이 변경되었을 수 있으니 다시 한번 더 체크
        if min_cost[now] < cost:
            continue

        # now 로부터 시작하는 간선들을 검사
        for next_node, link_cost in graph[now].items():
            if D < next_node:
                continue
            if next_node == now: # link_cost >= 0 이므로, 자기 자신은 제외
                continue
            next_cost = cost + link_cost
            if min_cost[next_node] < next_cost: # 이미 더 적은 cost 로 방문 했음.
                continue

            min_cost[next_node] = next_cost  # 갱신하고 큐잉
            heappush(que, (next_cost, next_node))
            #log("    add node %d, cost %d", next_node, next_cost)

    # 0->D 경로를 path 에 넣었기 때문에, 사실 이 경우는 발생하면 안됨.
    return D



N, D = map(int, input().split())

paths1 = defaultdict(list)
# paths1[k]: list[tuple(dest, len)].
#  k 에서부터 출발하여 dest 로 가는 길이 len 의 지름길 들의 리스트

all_nodes = set([0, D]) # 노드 정보 수집용 set. 기본으로 0, D 포함.
for _ in range(N):
    s,e,l = map(int, input().split())

    if s < 0 or e < 0: continue
    if s >= D or e > D: continue
    paths1[s].append((e, l)) # s->e, length l

    all_nodes.add(s)
    all_nodes.add(e)

# 모든 노드 간의 간선 추가. 메인 도로 상 인접한 간선만 고려.
prev = 0
for k in sorted(all_nodes):
    if k <= prev: continue
    paths1[prev].append((k, k-prev))
    prev = k

if prev < D:
    paths1[prev].append((D, D-prev))

# 간선들의 중복을 제거. 새로운 그래프로 변환함.
paths2 = defaultdict(dict)
# paths2[snode]: dict[dest,min_len]
#    snode -> dest 노드로의 간선 비용의 최소 값만 기억함.

for snode,list1 in paths1.items():
    # list 에는 중복이 있을 수 있음. 또한 동일한 dest 로 가는 지름길이 여럿일 경우는 최소 값만 선택.
    # ex:  [ (100, 20), (100, 7), (100, 20), (110, 10), (110, 5) ]
    #   -> { 100:7, 110:5 }
    dict1 = defaultdict(lambda: MAX_COST)
    for dest,len1 in list1:
        dict1[dest] = min(dict1[dest], len1)
    paths2[snode] = dict1

del paths1
# log("graph: %s", paths2)
#for n,d in paths2.items():
#    log("[%d]: { %s }", n, ', '.join([ f'{k}:{v}' for k,v in d.items() ]))


print(solve(D, paths2))

