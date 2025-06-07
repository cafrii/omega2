import sys
input = sys.stdin.readline

def solve(N:int, graph:list[list])->list:
    # traverse tree, to find parent node
    parent = [-1]*(N+1)
        # parent[k] means parent of node-k.
        #  valid range: 1 ~ N-1
        #  -1: unknown (not visited yet)
    stack = [1]
    parent[1] = 0 # 0 means it is root!

    while stack:
        u = stack.pop()
        for v in graph[u]:
            if parent[v] >= 0: continue # already visited
            stack.append(v)
            parent[v] = u
    return parent

N = int(input().strip())
graph = [ [] for k in range(N+1) ]

for _ in range(N-1):
    u,v = map(int, input().split())
    assert 1<=u<=N and 1<=v<=N
    graph[u].append(v)
    graph[v].append(u)

answer = solve(N, graph)
for i in range(2,N+1):
    print(answer[i])
