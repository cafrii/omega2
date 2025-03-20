

def solve(graph:list[list]):
    # note: graph has size of (number of node + 1)
    #       graph[0] is not used.

    # use DFS, from node 1
    stack = [ 1 ]
    visited = [ 0 ] * (len(graph) + 1)
    num_visited = 0

    while stack:
        v = stack.pop()
        visited[v] = 1
        num_visited += 1

        # next
        stack.extend([ x for x in graph[v] if x not in stack and visited[x] == 0 ])

    return num_visited - 1 # do not count 1 itself.



N = int(input().strip())
graph = [ [] for x in range(N+1) ]
# node 0 (graph[0]) will not be used.

num_links = int(input().strip())

for _ in range(num_links):
    s,e = map(int, input().split())
    graph[s].append(e) if e not in graph[s] else None
    graph[e].append(s) if s not in graph[e] else None

print(solve(graph))
