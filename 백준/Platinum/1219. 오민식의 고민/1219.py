'''
1219번

오민식의 고민 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	18627	3959	2472	18.980%

문제

오민식은 세일즈맨이다. 오민식의 회사 사장님은 오민식에게 물건을 최대한 많이 팔아서 최대 이윤을 남기라고 했다.
오민식은 고민에 빠졌다.
어떻게 하면 최대 이윤을 낼 수 있을까?
이 나라에는 N개의 도시가 있다. 도시는 0번부터 N-1번까지 번호 매겨져 있다. 오민식의 여행은 A도시에서 시작해서 B도시에서 끝난다.

오민식이 이용할 수 있는 교통수단은 여러 가지가 있다. 오민식은 모든 교통수단의 출발 도시와 도착 도시를 알고 있고, 비용도 알고 있다.
게다가, 오민식은 각각의 도시를 방문할 때마다 벌 수 있는 돈을 알고있다. 이 값은 도시마다 다르며, 액수는 고정되어있다.
또, 도시를 방문할 때마다 그 돈을 벌게 된다.

오민식은 도착 도시에 도착할 때, 가지고 있는 돈의 액수를 최대로 하려고 한다. 이 최댓값을 구하는 프로그램을 작성하시오.

오민식이 버는 돈보다 쓰는 돈이 많다면, 도착 도시에 도착할 때 가지고 있는 돈의 액수가 음수가 될 수도 있다.
또, 같은 도시를 여러 번 방문할 수 있으며, 그 도시를 방문할 때마다 돈을 벌게 된다.
모든 교통 수단은 입력으로 주어진 방향으로만 이용할 수 있으며, 여러 번 이용할 수도 있다.

입력
첫째 줄에 도시의 수 N과 시작 도시, 도착 도시 그리고 교통 수단의 개수 M이 주어진다.
둘째 줄부터 M개의 줄에는 교통 수단의 정보가 주어진다.
교통 수단의 정보는 “시작 끝 가격”과 같은 형식이다.
마지막 줄에는 오민식이 각 도시에서 벌 수 있는 돈의 최댓값이 0번 도시부터 차례대로 주어진다.

N과 M은 50보다 작거나 같고, 돈의 최댓값과 교통 수단의 가격은 1,000,000보다 작거나 같은 음이 아닌 정수이다.

출력
첫째 줄에 도착 도시에 도착할 때, 가지고 있는 돈의 액수의 최댓값을 출력한다.
만약 오민식이 도착 도시에 도착하는 것이 불가능할 때는 "gg"를 출력한다.
그리고, 오민식이 도착 도시에 도착했을 때 돈을 무한히 많이 가지고 있을 수 있다면 "Gee"를 출력한다.
'''


import sys

input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)


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
    log("relaxing..")
    for k in range(N):
        log("(%d) min_costs: %s", k, min_costs)
        for s,e,c in edges:
            if min_costs[s] == INFINITY: continue
            if min_costs[s] + c - earning[e] >= min_costs[e]: continue

            if k < N-1:
                log("    min_cost[%d]: %d (+%d-%d) -> %d", e, min_costs[s], c, earning[e], min_costs[s] + c - earning[e])
                min_costs[e] = min_costs[s] + c - earning[e]
            else: # negative cycle detected
                log("!! detect cycle! %d,%d,%d", s, e, c)
                in_cycle[e] = True

    if min_costs[E] == INFINITY:
        log("cannot reach to goal")
        return 0, 'gg'

    if True not in in_cycle:
        log("no negative cycle")
        return min_costs[E], None

    # 음의 cycle 노드에서 E 까지의 경로가 있는지 체크.
    # 경로 유무만 찾는 간단한 내부 함수를 정의하여 사용
    #
    def can_reach(S, E, visited=None) -> bool:
        log("checking reach %d -> %d", S, E)
        # 간단하게 DFS로..
        graph = [ [] for x in range(N) ]
        for s,e,c in edges:
            graph[s].append(e)
        if visited is None:
            visited = [ False ] * N
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

    # u = in_cycle.index(True)
    # if can_reach(u, E):
    #     return 0, 'Gee'

    # cycle 이 하나만 있는 게 아닐 수 있음. cycle 에 속한 모든 노드에서 확인해야 함.
    visited = [ False ] * N
    for u in range(N):  # 모든 노드에 대해
        if not in_cycle[u]: continue
        if visited[u]: continue
        if can_reach(u, E, visited):
            return 0, 'Gee'

    log("harmless negative cycle")
    return min_costs[E], None




N, S, E, M = map(int, input().split())
edges = []  # (start, end, cost)
for _ in range(M):
    edges.append(tuple(map(int, input().split())))
earning = list(map(int, input().split()))

cost, status = solve(N, S, E, edges, earning)

print(status) if status else print(-cost)




'''
예제 입력 1
5 0 4 7
0 1 13
1 2 17
2 4 20
0 3 22
1 3 4747
2 0 10
3 4 10
0 0 0 0 0
예제 출력 1
-32

# 1
echo '5 0 4 7\n0 1 13\n1 2 17\n2 4 20\n0 3 22\n1 3 4747\n2 0 10\n3 4 10\n0 0 0 0 0' | python3 1219.py
# -> -32

# 2
echo '5 0 4 5\n0 1 10\n1 2 10\n2 3 10\n3 1 10\n2 4 10\n0 10 10 110 10' | python3 1219.py
# -> Gee

# 3
echo '3 0 2 3\n0 1 10\n1 0 10\n2 1 10\n1000 1000 47000' | python3 1219.py
# -> gg

# 4
echo '2 0 1 2\n0 1 1000\n1 1 10\n11 11' | python3 1219.py
# -> Gee

# 5
echo '1 0 0 1\n0 0 10\n7' | python3 1219.py
# -> 7

#6
echo '5 0 4 7\n0 1 13\n1 2 17\n2 4 20\n0 3 22\n1 3 4747\n2 0 10\n3 4 10\n8 10 20 1 100000' | python3 1219.py
# -> 99988


# 음의 사이클이 있긴 하지만 사이클에서 E로 도달 가능하지 않은 관계로 문제에 영향을 전혀 끼치지 못하는 경우
5 0 4 5
0 1 0
1 2 0
2 3 0
3 1 0
0 4 0
1 1 1 1 1

echo '5 0 4 5\n0 1 0\n1 2 0\n2 3 0\n3 1 0\n0 4 0\n1 1 1 1 1' | python3 1219.py
# -> 2


# 음의 사이클이 있긴 하지만 S에서 도달 가능하지 않은 관계로 문제에 영향을 전혀 끼치지 못하는 경우.
#    사실 사이클로 인식 조차 되지 않음.
5 0 4 5
1 4 0
1 2 0
2 3 0
3 1 0
0 4 0
1 1 1 1 1

echo '5 0 4 5\n1 4 0\n1 2 0\n2 3 0\n3 1 0\n0 4 0\n1 1 1 1 1' | python3 1219.py
-> 2

# 두 개의 서로 분리된 음의 사이클.
8 0 7 9
0 1 0
1 2 0
2 3 0
3 1 0
0 4 0
4 5 0
5 6 0
6 4 0
6 7 0
1 1 1 1 1 1 1 1
-> Gee
# 22 가 나오면 틀린 것임!


'''
