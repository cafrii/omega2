import sys
from heapq import heappush, heappop

INF = 10001

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

def solve_prim(N:int, T:int, edges:list[list[tuple[int,int]]])->int:
    '''
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
        if visited[v]: continue

        visited[v] = 1
        num_conn += 1
        sum_costs += (cost + extra_cost)
        if num_conn > 1: # 최초 노드-1은 제외
            extra_cost += T  # 하나가 연결이 되면 추가 비용이 증가함.

        if num_conn >= N: # early exit
            break
        for x,xc in edges[v]: # next_node, next_cost
            if visited[x]: continue  # 이미 포함.
            if cost_in_que[x] <= xc: continue # 더 작은 cost의 간선이 pending.
            heappush(hq, (xc, x))
            cost_in_que[x] = xc
    return sum_costs

if __name__ == '__main__':
    inp = get_input_prim()
    print(solve_prim(*inp))

