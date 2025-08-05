'''
14950번
정복자 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	2803	1650	1346	57.719%

문제
서강 나라는 N개의 도시와 M개의 도로로 이루어졌다.
모든 도시의 쌍에는 그 도시를 연결하는 도로로 구성된 경로가 있다.
각 도로는 양방향 도로이며, 각 도로는 사용하는데 필요한 비용이 존재한다.
각각 도시는 1번부터 N번까지 번호가 붙여져 있다.
그 중에서 1번 도시의 군주 박건은 모든 도시를 정복하고 싶어한다.

처음 점거하고 있는 도시는 1번 도시 뿐이다.
만약 특정 도시 B를 정복하고 싶다면, B와 도로로 연결된 도시들 중에서 적어도 하나를 정복하고 있어야 한다.
조건을 만족하는 도시 중에서 하나인 A를 선택하면, B를 정복하는 과정에서 A와 B를 연결하는 도로의 비용이 소모된다.
박건은 한번에 하나의 도시만 정복을 시도하고 언제나 성공한다.
한 번 도시가 정복되면, 모든 도시는 경계를 하게 되기 때문에 모든 도로의 비용이 t만큼 증가하게 된다.
한 번 정복한 도시는 다시 정복하지 않는다.

이때 박건이 모든 도시를 정복하는데 사용되는 최소 비용을 구하시오.

입력
첫째 줄에 도시의 개수 N과 도로의 개수 M과 한번 정복할 때마다 증가하는 도로의 비용 t가 주어진다.
N은 10000보다 작거나 같은 자연수이고, M은 30000보다 작거나 같은 자연수이다.
t는 10이하의 자연수이다.

M개의 줄에는 도로를 나타내는 세 자연수 A, B, C가 주어진다.
A와 B사이에 비용이 C인 도로가 있다는 뜻이다.
A와 B는 N이하의 서로 다른 자연수이다. C는 10000 이하의 자연수이다.

출력
모든 도시를 정복하는데 사용되는 최소 비용을 출력하시오.

----

12:38~


MST 문제인데, 간선 비용이 고정되어 있지 않고 점점 증가한다는 것이 특징.
간선 비용은 고정하고, 총 비용 합산 할 때만 추가 비용을 고려해 주면 됨.

핵심은 kruscal 과 prim 중 어떤 알고리즘을 사용할 것인지인데..
1번부터 정복을 시작해야 한다는 조건이 있음.
kruscal 의 경우 임의 간선부터 선택할 것이므로,
kruscal 로도 구현이 가능할 것인지가 관건.
비용이 증가되긴 하지만, 산술 증분 이다.
사용되는 총 간선 개수가 N-1로 고정되므로, 사실 어느 간선 부터 사용하더라도
최종적으로 증가되는 비용은 T * (N-2) 로 일정할 것으로 보임.

일단 prim 으로 구현한 것으로 제출하여 통과 되었으나 kruscal 도 가능해 보임.
어느 쪽이 더 빠르게 구현될 것인지는 노드와 간선 수 고려하여 비교해 봐야 함.
실제로 아주 약간 더 빠른 제출 답안 중 일부는 kruscal 로 구현한 것으로 확인됨.

'''


import sys
from heapq import heappush, heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)

INF = 10001

def get_input_kruscal():
    input = sys.stdin.readline
    N,M,T = map(int, input().split())
    edges = [] # (cost, a, b)
    for _ in range(M):
        a,b,c = map(int, input().split())
        heappush(edges, (c, a, b))
    return N,T,edges

def get_input_prim():
    input = sys.stdin.readline
    N,M,T = map(int, input().split())
    # 간선의 수가 노드 대비 아주 많지 않으니 sparse array 로.
    edges = [ [] for k in range(N+1) ]
    for _ in range(M):
        a,b,c = map(int, input().split())
        edges[a].append((b,c))
        edges[b].append((a,c))
    return N,T,edges


def solve_kruscal(N:int, T:int, hq:list)->int:
    '''
    hq: heapque of edges (cost,u,v)
    '''
    roots = list(range(N+1))

    def find_root(a:int)->int:
        if a == roots[a]:
            return a
        roots[a] = ra = find_root(roots[a])
        return ra

    num_conn = 0
    extra_cost = 0
    total_cost = 0

    while hq:
        c,a,b = heappop(hq)
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue

        roots[b] = roots[rb] = ra
        total_cost += (c + extra_cost)
        num_conn += 1
        extra_cost += T

        if num_conn >= N-1:
            break
    return total_cost


def solve_prim(N:int, T:int, edges:list[list[tuple[int,int]]])->int:
    '''
    edges[u]: list of (v,cost) which is cost of u-v edge
    '''
    visited = [0]*(N+1) # visited[]가 true 이면 연결 완료.
    num_conn = 0 # 연결된 노드 수. early exit 목적.
    extra_cost = 0  # 추가로 부과되는 비용
    sum_costs = 0   # 총 누적 비용

    # 불필요한 push를 막기 위한 최적화 트릭.
    # cost_in_que[k]는 que에 추가된 node-k로의 최소 cost
    cost_in_que = [INF] * (N+1)

    hq = []
    heappush(hq, (0, 1)) # cost:0, node:1
    cost_in_que[1] = 0
    # 간선 정보는 필요하지 않으므로 외부 노드만 que에 push하면 됨.

    while hq:
        cost,v = heappop(hq)
        log("(-> %d) cost %d", v, cost)
        if visited[v]: continue

        visited[v] = 1
        num_conn += 1
        sum_costs += (cost + extra_cost)

        if num_conn > 1:
            extra_cost += T  # 하나가 연결이 되면 추가 비용이 증가함.
        log("  conn %d, sum cost %d, extra %d", num_conn, sum_costs, extra_cost)

        # exit condition
        if num_conn >= N:
            log("    early exit")
            break

        # for x in range(1, N+1): # next
        for x,xc in edges[v]: # next_node, next_cost
            # if xc == 0: continue # 연결 없음.
            if visited[x]: continue  # 이미 포함.
            if cost_in_que[x] <= xc: continue # 더 작은 cost의 간선이 pending.

            log("    push (%d: %d)", x, xc)
            heappush(hq, (xc, x))
            cost_in_que[x] = xc

    return sum_costs



if __name__ == '__main__':
    # inp = get_input_kruscal()
    # r = solve_kruscal(*inp)
    inp = get_input_prim()
    r = solve_prim(*inp)
    print(r)




'''
예제 입력 1
4 5 8
1 2 3
1 3 2
2 3 2
2 4 4
3 4 1
예제 출력 1
29


run=(python3 14950.py)

echo '4 5 8\n1 2 3\n1 3 2\n2 3 2\n2 4 4\n3 4 1' | $run
# -> 29

echo '1 1 1\n1 1 1' | $run
# -> 0

echo '2 1 5\n1 2 10' | $run
# -> 10

echo '3 2 20\n1 2 10\n2 3 7' | $run
# -> 37

echo '3 2 100\n3 2 10\n3 1 20' | $run
# -> 130


'''

