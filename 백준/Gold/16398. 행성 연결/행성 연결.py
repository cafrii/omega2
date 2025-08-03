import sys
import heapq
from heapq import heappush,heappop

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    mat = []
    for i in range(N):
        m = list(map(int, input().split()))
        mat.append(m)
    return mat

def solve_prim(mat:list[list[int]])->int:
    '''
    '''
    N = len(mat)

    # node indexing: node-0 is first node.
    visited = [0]*N
    # visited[k] is true if node-k is already belonged to tree
    num_nodes = 0
    sum_costs = 0
    INF = int(1e8) + 1
    costs = [INF]*N
    # costs: hq 의 효율적인 관리를 위해, 각 노드 별 네트워크로의 최소 연결 비용을 추적한다.

    start = 0 # start node
    hq = [ (0, start)]
    costs[start] = 0
    # 후보 노드 힙 큐. 리스트 요소: (cost, node) 튜플
    # cost 는 네트워크에 이미 소속된 임의 노드와 이 node와의 연결 비용.
    # 최초 시작 노드는 cost 0 부터 시작.

    while hq:
        cur_cost,cur_node = heappop(hq)
        if visited[cur_node]: continue
        visited[cur_node] = 1
        # hq 에서 pop 될 때 비로소 해당 노드가 네트워크에 연결됨.
        num_nodes += 1
        sum_costs += cur_cost
        if num_nodes >= N:
            break
        # 후보 등록
        for nxt_node,nxt_cost in enumerate(mat[cur_node]):
            if visited[nxt_node]: continue
            if costs[nxt_node] <= nxt_cost: continue
            # 연결 후보 노드 nxt_node 와 연결 cost 를 힙큐에 추가.
            # 네트워크의 어느 노드와 연결되는지는 관심 사항 아님.
            heappush(hq, (nxt_cost, nxt_node))
            costs[nxt_node] = nxt_cost

    return sum_costs


if __name__ == '__main__':
    mat = get_input()
    print(solve_prim(mat))
