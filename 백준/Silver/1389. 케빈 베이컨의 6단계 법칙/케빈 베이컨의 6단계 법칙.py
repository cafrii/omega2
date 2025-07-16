
import sys
input = sys.stdin.readline

def solve_floydwarshall(graph:list[list[int]])->int:
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
    #assert [ graph[k][j] for k in range(N) for j in range(N) if k != j ].count(0) == 0

    # get kevin bacon number of each
    relationships = [ sum(graph[k]) for k in range(N) ]

    # if multiple ties, return smaller index (first occurrence)
    # also, we should return 1-based index
    return relationships.index(min(relationships))+1


N,M = map(int, input().split())
graph = [[0]*N for i in range(N)]
for _ in range(M):
    A,B = map(int, input().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

print(solve_floydwarshall(graph))

