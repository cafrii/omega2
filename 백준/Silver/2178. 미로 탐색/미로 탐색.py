
from collections import deque

def solve(graph:list[list]):
    # graph[k]는 노드 k에서 이동 가능한 노드의 목록.
    # 노드 index는 0-base. 즉, 좌상단(시점)이 0, 우하단(종점)이 N*M-1.
    #
    K = len(graph) # K == N*M

    start = 0
    goal = N*M - 1

    visited = [0] * K
        # 0 또는 1. 1 이면 해당 index의 노드에 방문했음을 의미
    que = deque([ (0,1) ])
        # BFS 를 위한 선입선출 큐.
        # 큐의 요소는 (node, walked)의 튜플.
        # walked 는 시점에서부터의 이동 거리 (시점위치부터 1로 카운팅)

    while que:
        u,walked = que.popleft()
        if u < 0 or u >= K or visited[u]:
            continue

        visited[u] = 1

        if u == goal:
            return walked

        # 다음 노드 검색.
        walked += 1
        for v in graph[u]: # 이동 가능한 이웃 목록 중
            # v는 아마도 u-1, u+1, u-M, u+M 중 일부일 것임.
            if v not in (u-1, u+1, u-M, u+M):
                continue
            if v == u:
                continue
            if visited[v]:
                continue
            que.append((v, walked))

    # 여기에 도달한다면 도착에 실패한 것임.
    return 0


N,M = map(int, input().split())

A = [ input().strip() for _ in range(N) ]
# 각 요소는 길이 M 이면서 0 과 1로만 구성된 문자열. ex: '1010100'

# 그래프 생성
graph = [ [] for _ in range(N*M) ]
for y in range(N):
    for x in range(M):
        k = y*M + x
        if A[y][x] == '0':
            continue
        if x > 0 and A[y][x-1] == '1': # left
            graph[k].append(k-1)
        if x < M-1 and A[y][x+1] == '1': # right
            graph[k].append(k+1)
        if y > 0 and A[y-1][x] == '1': # up
            graph[k].append(k-M)
        if y < N-1 and A[y+1][x] == '1': # down
            graph[k].append(k+M)

print(solve(graph))

