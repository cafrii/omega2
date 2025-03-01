

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

def fill():
    changed = False
    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                continue
            # try to find path from i to j indirectly
            for k in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
                    changed = True
                    break
    return changed

# repeat call fill() until no change
while fill():
    pass
[ print(*graph[i]) for i in range(N) ]
