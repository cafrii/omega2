'''
16398번
행성 연결 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	10587	5077	3675	45.009%

문제
홍익 제국의 중심은 행성 T이다. 제국의 황제 윤석이는 행성 T에서 제국을 효과적으로 통치하기 위해서,
N개의 행성 간에 플로우를 설치하려고 한다.

두 행성 간에 플로우를 설치하면 제국의 함선과 무역선들은 한 행성에서 다른 행성으로 무시할 수 있을 만큼 짧은 시간만에 이동할 수 있다.
하지만, 치안을 유지하기 위해서 플로우 내에 제국군을 주둔시켜야 한다.

모든 행성 간에 플로우를 설치하고 플로우 내에 제국군을 주둔하면,
제국의 제정이 악화되기 때문에 황제 윤석이는 제국의 모든 행성을 연결하면서 플로우 관리 비용을 최소한으로 하려 한다.

N개의 행성은 정수 1,…,N으로 표시하고, 행성 i와 행성 j사이의 플로우 관리비용은 Cij이며, i = j인 경우 항상 0이다.

제국의 참모인 당신은 제국의 황제 윤석이를 도와 제국 내 모든 행성을 연결하고, 그 유지비용을 최소화하자.
이때 플로우의 설치비용은 무시하기로 한다.

입력
입력으로 첫 줄에 행성의 수 N (1 ≤ N ≤ 1000)이 주어진다.

두 번째 줄부터 N+1줄까지 각 행성간의 플로우 관리 비용이 N x N 행렬 (Cij),
(1 ≤ i, j ≤ N, 1 ≤ Cij ≤ 100,000,000, Cij = Cji, Cii = 0) 로 주어진다.

출력
모든 행성을 연결했을 때, 최소 플로우의 관리비용을 출력한다.


--------

8:01~8:20 kruscal


----
알고리즘 비교

prim:    O( (V+E) log V )
kruscal: O( E log E )

Vertex: 1000
Edge  : sum 1~(N-1) = N(N-1)/2 = 999000/2 = 499500


제출 번호  아이디    문제   결과        메모리   시간     언어      코드 길이
97054149 cafrii  16398 맞았습니다!!  75020  340 ms Python 3 1789B   <-- prim
97031039 cafrii  16398 맞았습니다!! 101152 1436 ms Python 3 1397B   <-- kruscal

이 경우는 edge 개수가 너무 많기 때문에,
kruscal 보다는 prim 방식이 메모리도 적게 들고 시간도 훨씬 빠르다.

'''

import sys
from heapq import heappush,heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def get_input():
    '''
    어떤 알고리즘을 사용할 지에 따라서 저장해야 할 정보의 형식이 좀 다르다.
    처음 입력을 받을 때 부터 각 알고리즘에 적합한 형태로 제공해 주는 것이 좋다.
    여기서는 두 가지 형태를 다 만들어 주도록 한다.
    '''
    input = sys.stdin.readline
    N = int(input().rstrip())
    mat = [] # [0]*N for k in range(N) ]
    costs = []  # heapq of format (c,i,j)
    for i in range(N):
        m = list(map(int, input().split()))
        assert len(m) == N, f'wrong row[{i}] length'
        mat.append(m)
        for j in range(i+1,N):
            heappush(costs, (m[j],i,j))
    # 간선 정보는 kruscal 에 필요
    # matrix 형태는 prim 에 필요
    return N,mat,costs


def solve_kruscal(N:int, costs:list[tuple[int,int,int]])->int:
    '''
    start merge N single-node trees into one unified tree
    use mst kruscal algorithm
    costs is heapq format
    return total cost
    '''
    # `costs` is heap-sorted list (ascending order)
    roots = list(range(N))  # planet: 0 ~ N-1

    def find_root(a:int):
        if a == roots[a]:
            return a
        roots[a] = ra = find_root(roots[a])
        return ra

    # we will not make cycle.
    # so, only N-1 flows are needed.
    num_flow = 0
    total_cost = 0

    # for c,a,b in costs:
    while costs:
        c,a,b = heappop(costs)
        ra,rb = find_root(a),find_root(b)
        if ra == rb: # they are alredy in same tree. skip!
            continue
        roots[rb] = roots[b] = ra # merge two tree!
        total_cost += c
        num_flow += 1
        if num_flow >= N-1:
            break
    return total_cost



def solve_prim(mat:list[list[int]])->int:
    '''

    '''
    N = len(mat)
    assert len(mat[0]) == N, "wrong matrix dimension"

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
    n,mat,que = get_input()
    # r1 = solve_kruscal(n,que)
    # print(r1)
    r2 = solve_prim(mat)
    print(r2)


'''
예제 입력 1
3
0 2 3
2 0 1
3 1 0
예제 출력 1
3

예제 입력 2
5
0 6 8 1 3
6 0 5 7 3
8 5 0 9 4
1 7 9 0 6
3 3 4 6 0
예제 출력 2
11


run=(python3 16398.py)

echo '3\n0 2 3\n2 0 1\n3 1 0' | $run
echo '5\n0 6 8 1 3\n6 0 5 7 3\n8 5 0 9 4\n1 7 9 0 6\n3 3 4 6 0' | $run
->
3 11

echo '1\n7' | $run
-> 0
echo '2\n1 4\n4 1' | $run
-> 4



'''
