
def solve_dfs(graph:list[list], start):
    # graph is list of list
    # graph[k] is list of links starting from node-k
    #
    visited = set()
    result = []
    stack = [ start ]

    # reverse sort each links
    for a in graph:
        a.sort(reverse=True)

    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        result.append(u)

        # 다음 노드들을 위한 준비
        # 스택에 넣은 후 나중에 visited 체크를 하는 것 보다는
        # 스택에 넣기 전에 체크를 하는 것이 좋겠음.
        #
        # 문제 예제 답변대로 하려면 거꾸로 스택에 넣어야만 함.
        # stack.extend([ a for a in sorted(graph[u], reverse=True) if a not in visited ])

        # 아예 루프 전에 미리 리버스 sorting 을 해 놓고 여기서는 순서대로 처리.
        stack.extend([ a for a in graph[u] if a not in visited ])

    return result


from collections import deque

def solve_bfs(graph:list[list], start):
    for a in graph:
        a.sort()

    visited = set()
    result = []
    que = deque([ start ])

    while que:
        u = que.popleft()
        if u in visited:
            continue
        visited.add(u)
        result.append(u)
        que.extend([ a for a in graph[u] if a not in visited ])
    return result


N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)] # index: 0 ~ N. index 0 is not used.

for _ in range(M):
    a,b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

print(' '.join(map(str, solve_dfs(graph, V))))
print(' '.join(map(str, solve_bfs(graph, V))))
