

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)


MAX_N = 500
# MAX_EDGE = 6_000
# MIN_EC = -10_000  # minimum edge cost
MAX_EC = 10_000

# 비용 (경로 길이)가 음수가 될 수 있으니 -1 과 같은 초기값을 쓸 수 없음.
# 예상되는 최소 비용의 최대값은 1에서 출발하여 모든 정점을 다 거치는 것.
# INFINITY = ((MAX_N-1) * MAX_EC) + 1
INFINITY = (MAX_N * MAX_EC) + 1 # 넉넉하게 더 큰값을..


def solve(N:int, E:list[tuple]) -> tuple[list,list]:
    # N: 노드 (정점) 개수. 노드 번호는 1~N
    # E: 간선 리스트. 간선 형식: (start, end, cost)
    #    1<=start,end<=N,  cost는 음수가 될 수 있음.
    # return (min_cost, in_cycle)
    #    min_cost[k]: 1에서 k에 이르는 최소 비용
    #        min_cost[0]은 사용되지 않음.
    #    in_cycle[k]: k가 음의 cycle 안에 포함된 노드라면 True
    #
    # 벨만 포드 알고리즘 참고
    # https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm#Algorithm
    #

    # step 1: 초기화
    min_costs = [ INFINITY for x in range(N+1) ]
    in_cycle = [ False for x in range(N+1) ]
    # predecessor = [ -1 ] * (N+1) # 음의 사이클 경로 추적용

    min_costs[1] = 0 # starting point

    # step 2: relax edges repeatedly
    for i in range(N):
        for u,v,c in E:
            if min_costs[u] == INFINITY:
                continue

            if min_costs[u] + c >= min_costs[v]:
                continue

            # 더 적은 cost(짧은 경로)가 발견되었으므로 갱신
            if i < N-1:  # N-1 루프는 음의 cycle 검사용
                min_costs[v] = min_costs[u] + c
                # predecessor[v] = u
                continue

            # 음의 cycle 감지됨
            #log('edge (%d, %d) in negative cycle!', u, v)
            in_cycle[v] = True

            # 만약 이 음의 cycle 구성 정보를 추출하고 싶다면 predecessor[]를 이용해 역추적.

            # 더 진행 하는 것이 의미가 있는지는 문제 유형에 따름.
            # 모든 음의 사이클 간선을 다 체크하는게 필요하다면 계속 진행하면 됨.
            # 음의 사이클과는 완전히 독립적인 노드가 있을 수 있고, 그 노드까지의 답을 구해야 한다면
            # 끝까지 진행 한 후 결과를 보고 확인하면 된다.

    return min_costs, in_cycle


N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

min_costs, in_cycle = solve(N, edges)

# log("costs: %s,  cycle: %s", min_costs, in_cycle)
# print costs
#log(','.join([ ('-' if x >= INFINITY else str(x)) for x in min_costs[1:] ]))
# print cycle
#log(''.join([ ('1' if x else '.' ) for x in in_cycle[1:] ]))


# 이 문제에서는, 그래프 어딘가에 음의 사이클이 하나라도 있으면 그냥 -1 하나면 출력하라고 함.
if True in in_cycle:
    print(-1)
else:
    for c in min_costs[2:]:
        print(c if c < INFINITY else -1)

