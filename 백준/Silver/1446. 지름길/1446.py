'''

1446번

이걸 DP 로 풀면 더 간단하게 풀리는 것 같음.
D 값의 크기가 크지 않으므로, 모든 가능한 자연수<D 를 노드로 잡아 버리고

지름길 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	15133	8853	6711	58.714%

문제
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다.
이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다.
어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

입력
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다.
N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다.
다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다.
모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

출력
세준이가 운전해야하는 거리의 최솟값을 출력하시오.

'''


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
    log("min_cost: %s", min_cost)

    que = []  # 요소 타입: tuple(누적_cost, 노드)
    heappush(que, (0, 0))

    while que:
        log("que: %s", que)

        cost, now = heappop(que)
        log("cost %d: node %d", cost, now)
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
            log("    add node %d, cost %d", next_node, next_cost)

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
for n,d in paths2.items():
    log("[%d]: { %s }", n, ', '.join([ f'{k}:{v}' for k,v in d.items() ]))


print(solve(D, paths2))



'''
예제 입력 1
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90

예제 출력 1
70

5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 10
-> 50

2 20
0 10 5
2 7 3
-> 15




echo '5 150\n0 50 10\n0 50 20\n50 100 10\n100 151 10\n110 140 90' \
   | python3 1446.py
-> 70

예제 입력 2
2 100
10 60 40
50 90 20
예제 출력 2
80

echo '2 100\n10 60 40\n50 90 20' | python3 1446.py
-> 80

예제 입력 3
8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0
예제 출력 3
432

echo '8 900\n0 10 9\n20 60 45\n80 190 100\n50 70 15\n160 180 14\n140 160 14\n420 901 5\n450 900 0' |\
    python3 1446.py
-> 432

echo '3 100\n10 60 40\n40 90 20\n50 90 20' | python3 1446.py
-> 70

'''

# DP 풀이법
'''
import sys
input = sys.stdin.readline

n, d = map(int, input().split())

shortcut = []
for _ in range(n):
    start, end, cost = map(int, input().split())
    shortcut.append((start, end, cost))

dp = [i for i in range(d + 1)]

shortcut.sort()

for start, end, cost in shortcut:
    if end > d or cost >= end - start:
        continue
    if dp[start] + cost < dp[end]:
        dp[end] = dp[start] + cost
        for i in range(end + 1, d + 1):
            if dp[i] > dp[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
            else:
                break

print(dp[d])
'''