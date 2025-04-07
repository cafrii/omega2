'''
1916
최소비용 구하기 성공

다른 구현 풀이도 참고할 것.


시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	128 MB	114963	38777	25675	32.884%

문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

입력
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다.
그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다.
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다.
버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

'''

import sys
import heapq

input = sys.stdin.readline

MAX_M = 100_000
MAX_C0 = 100_000 - 1
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
        cost, now = heapq.heappop(hq)
        # cost: 이 노드까지의 최소 전체 경로 비용
        # now: 현재 방문(검토)중인 노드

        # 실수하기 쉬운 지점. q 에 넣을 때는 조건에 맞춰 넣었더라도, 그 동안 상황이 변했을 수 있으므로 다시 한번 더 체크.
        if min_cost[now] < cost:
            continue

        # 현재의 노드에서 다음 인접 노드들까지의 간선에 대해 고려
        # print(f'[{now}: c{cost}] checking {','.join([ str(x) for x,y in graph[now]])}')
        for (nn, lc) in graph[now]:
            # nn: next_node, lc: link_cost
            if nn == now:
                continue
            new_cost = cost + lc
            if min_cost[nn] <= new_cost:
                continue
            min_cost[nn] = new_cost
            # print(f'  update [{nn}: c{new_cost}]')
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

    # TODO: 아예 그래프에 넣을 때 부터, 동일 S/E 의 여러 간선이 있다면
    #       최소 간선 정보만 유지하도록 하면 시간이 개선됨.
    #       중복 간선을 의도한 문제들이 있을 것이므로...
    graph[s].append((e, c))
        # 그래프에는 (next_node, link_cost) 튜플로 저장됨.

S,E = map(int, input().split())

print(solve(graph, S, E))


'''
예제 입력 1
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

예제 출력 1
4


5
4
1 2 0
2 3 0
3 4 0
4 5 100
1 5
-> 100


4
4
1 2 60000
1 3 50000
2 4 60000
3 4 60000
1 4
-> 11000




시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 1000,100_000
print(N); print(M)
print(1,1,0)
for _ in range(M-1):
    print(randint(1, N),randint(1, N),randint(0, 99999))
print(1,randint(1,N))
EOF
) | time python3 1916.py


'''
