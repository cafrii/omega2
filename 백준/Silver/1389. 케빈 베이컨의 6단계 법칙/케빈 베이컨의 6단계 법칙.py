
import sys
input = sys.stdin.readline

from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def graph2str(g:list[list[int]], indent='  ')->str:
    res = []
    for ln in g:
        res.append(indent + ' '.join([str(e) for e in ln]))
    return '\n'.join(res)

def solve_floydwarshall(graph:list[list[int]])->int:
    '''
    warning: graph will be updated here.
    '''
    N = len(graph)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                # update i->j path via k
                if i == j or i == k or k == j:
                    continue
                if not (graph[i][k] and graph[k][j]):
                    continue
                if graph[i][j]: # already related? then update it.
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                else:
                    graph[i][j] = graph[i][k]+graph[k][j]

    # check if non-relation person exist. it should not exist!
    assert [ graph[k][j] for k in range(N) for j in range(N) if k != j ].count(0) == 0

    # get kevin bacon number of each
    relationships = [ sum(graph[k]) for k in range(N) ]

    # if multiple ties, return smaller index (first occurrence)
    # also, we should return 1-based index
    return relationships.index(min(relationships))+1


def solve_bfs(graph:list[list[int]])->int:
    '''
    graph should contain 'direct' link only.
    graph should not be updated!
    '''
    N = len(graph)

    # convert mask graph to index graph. [[0 0 0 1 0 1] ..] -> [[3, 5], ..]
    relgraph = []
    for k in range(N):
        relgraph.append([ j for j in range(N) if graph[k][j] ])

    def get_kb(start:int)->int:
        # start 부터 시작하여, 모든 사람에게 다 도달시키도록 graph update
        INF = N+1
        distances = [INF]*N
        que = deque([start])
        distances[start] = 0
        while que:
            cur = que.popleft()
            d = distances[cur]
            for nxt in relgraph[cur]:
                # check if already visited
                if distances[nxt] < INF: continue
                que.append(nxt)
                distances[nxt] = d+1

        # 도달하지 못한 사람은 없어야 하는데..
        assert INF not in distances

        kb = sum(distances)
        # log("[%d] %s -> %d", start, distances, kb)
        return kb

    relationships = [ get_kb(k) for k in range(N) ]
    return relationships.index(min(relationships))+1

    # winner,minrel = -1,N
    # for k in range(len(graph)):
    #     rel = get_kb(k)
    #     if rel < minrel:
    #         winner,minrel = k,rel
    # return winner+1


N,M = map(int, input().split())
graph = [[0]*N for i in range(N)]
for _ in range(M):
    A,B = map(int, input().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

print(solve_bfs(graph))
# print(solve_floydwarshall(graph)) # <- 훨씬 느리다!

