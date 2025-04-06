'''
1753번
최단경로 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	238752	74362	38287	26.333%

92657268	cafrii	1753	맞았습니다!!	69516KB	596ms	Python 3 / 수정	1513	1분 전

문제
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
단, 모든 간선의 가중치는 10 이하의 자연수이다.

입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다.
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.


- graph is 1-indexed
- dist[0] is not used
- dist[i] is the shortest distance from start to i
- dist[i] == INF means i is not reachable from start
- dist[i] is the shortest distance from start to i
- dist[i] is updated only when a shorter path is found

'''



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



'''
예제 입력 1
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

예제 출력 1
0
2
3
7
INF



시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
V,E = 20_000,300_000
# V,E = 20_000,1000
K = 1
print(V,E)
print(K)
num_edges = 0
# while num_edges < (V // 2) and num_edges < E:
#     print(1,randint(2,V),randint(1,10))
#     num_edges += 1
while num_edges < E:
    u,v,w = randint(1,V),randint(1,V),randint(1,10)
    if u == v:
        continue
    print(u,v,w)
    num_edges += 1
EOF
) | time python3 1753.py



'''
