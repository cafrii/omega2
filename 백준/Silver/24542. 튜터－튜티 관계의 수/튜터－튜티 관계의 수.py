from collections import defaultdict
import sys
input = sys.stdin.readline

MAX_N = 200_000
MOD = 1_000_000_007

def solve(graph:defaultdict, N:int):
    '''
    '''
    node_info = [ -1 for x in range(N+1) ]
    # node_info[k] 는 노드-k 가 어느 그룹에 속했는지를 식별.

    def mark_group(start:int, id:int):
        # start 노드 부터 시작하여 연결된 그룹에 그룹 식별자 id 를 할당.
        # node_info 이 visited 의 역할을 수행할 수 있음.
        num = 0
        if node_info[start] >= 0: # already marked
            return num
        node_info[start] = id
        num += 1
        stack = [ start ]
        while stack:
            cur = stack.pop()
            if cur not in graph: continue;
            for nxt in graph[cur]:
                if node_info[nxt] >= 0: continue # already visited
                node_info[nxt] = id
                num += 1
                stack.append(nxt)
        return num

    group_info = []
    # 그룹 정보 저장. (id, any_node_in_group)
    #  id 는 0 부터 증가하는 숫자.

    # 연결 관계가 하나도 없는 노드가 있을 수 있는지는 문제에서 명확하지 않음.
    # nodes = graph.keys()
    nodes = range(1, N+1) # 단독 노드도 고려하려면 모든 노드에 대해서 검사 필요.
    for n in nodes:
        if node_info[n] >= 0: continue
        # 노드 n 부터 시작하여, 연결된 모든 노드를 하나의 그룹으로 묶는다.
        num_nodes = mark_group(n, len(group_info))
        group_info.append((num_nodes, n))

    # log("%d groups, %s", len(group_info), [t[0] for t in group_info])

    # 각 그룹에서는 임의의 하나의 노드만 선택하면 됨.
    cases = 1
    for g in group_info:
        cases = (cases * g[0]) % MOD
    return cases


N,M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(solve(graph, N))
