'''
1260번

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	323555	129257	76342	38.496%

문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.
'''

import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)
    pass


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
        # log('stack: %s', stack)
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        result.append(u)
        # log('visit %d, visited %s, span %s', u, visited, graph[u])

        # 다음 노드들을 위한 준비
        # 스택에 넣은 후 나중에 visited 체크를 하는 것 보다는
        # 스택에 넣기 전에 체크를 하는 것이 좋겠음.
        #
        #-- stack.extend(graph[u])

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
        # log('que: %s', que)

        u = que.popleft()
        if u in visited:
            continue

        visited.add(u)
        result.append(u)

        # log('visit %d, visited %s, span %s', u, visited, graph[u])

        que.extend([ a for a in graph[u] if a not in visited ])
    return result


N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)] # index: 0 ~ N. index 0 is not used.

for _ in range(M):
    a,b = map(int, input().split())
    # log(f'({a}, {b})')
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

# sort each links
# for e in graph:
#     e.sort()

print(' '.join(map(str, solve_dfs(graph, V)))) # dfs
print(' '.join(map(str, solve_bfs(graph, V)))) # bfs


'''
예제 입력 1
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1
1 2 4 3
1 2 3 4

예제 입력 2
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5

예제 입력 3
1000 1 1000
999 1000
예제 출력 3
1000 999
1000 999


echo "3 3 1
1 2
1 3
2 3" | python3 a.py

'''