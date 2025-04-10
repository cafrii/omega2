'''
1504번

특정한 최단 경로

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	103879	28749	19524	25.573%

문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데,
그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며,
그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000)
다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.


검토
    세 번의 최단 경로를 찾음. 다음 두 가지 경우가 있음.
        1 > V1 > V2 > N
        1 > V2 > V1 > N
    총 6회의 최단 경로를 찾아야 함.
        c1 = path(1->V1) + path(V1->V2) + path(V2->N)
        c2 = path(1->V2) + path(V1->V1) + path(V2->N)
    정답은 min(c1, c2)
'''

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def log(fmt, *arg):
    print(fmt % arg, file=sys.stderr)


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
        log("%d > %d: cost %d, total %d", start, v, c, cost+c)
        if c < 0:
            return -1
        cost += c
        start = v
    return cost


def solve(N, v1, v2) -> int:
    # 노드 1 에서, 노드 v1, v2 를 (순서 무관) 경유한 후 N 에 도달하는 최단 거리 구하기
    c1 = find_path2(1, [v1, v2, N])
    log("**** path: 1>%d>%d>%d: cost %d", v1, v2, N, c1)

    c2 = find_path2(1, [v2, v1, N])
    log("**** path: 1>%d>%d>%d: cost %d", v2, v1, N, c2)

    if c1 < 0 and c2 < 0:
        return -1
    if c1 < 0:
        return c2
    if c2 < 0:
        return c1
    return min(c1, c2)


#---------

N,E = map(int, input().split())

for _ in range(E):
    a,b,c = map(int, input().split())
    # if not (1<=a<=N and 1<=b<=N): sys.exit(1)
    if a == b: continue
    graph[a].append((b, c))
    graph[b].append((a, c))

v1,v2 = map(int, input().split())

# print graph briefly
# log("graph: %s", graph)
for a in range(1,N+1):
    if not graph[a]: continue
    log(f'{a}:' + ','.join([ f'{b}/{c}' for b,c in graph[a] ]))

log("problem: 1 -> (%d,%d) -> %d", v1, v2, N)

print(solve(N, v1, v2))




'''
예제 입력 1
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

예제 출력 1
7

echo '4 6\n1 2 3\n2 3 3\n3 4 1\n1 3 5\n2 4 5\n1 4 4\n2 3' | python3 1504.py

2 1
1 2 4
1 2
-> 4


14 17
1 2 3
2 3 3
3 7 2
1 4 1
4 5 1
5 6 1
6 7 1
2 6 1
7 8 1
8 9 2
9 10 2
10 11 5
11 14 4
8 12 3
12 13 3
13 14 3
12 11 1
7 8
-> 13

4 5
1 2 3
1 3 1
1 4 1
2 3 3
3 4 4
2 3
echo '4 5\n1 2 3\n1 3 1\n1 4 1\n2 3 3\n3 4 4\n2 3' | python3 1504.py
-> 8

5 4
1 4 1
1 3 1
3 2 1
2 5 1
3 4
-> 5

4 2
1 3 5
2 4 5
3 2
-> -1



'''
