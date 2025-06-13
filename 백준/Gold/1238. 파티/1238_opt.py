'''
최적화 된 풀이로 보이는 예.
dijkstra 를 역방향으로 사용하는 경우는 처음 본 것 같음. 아주 좋은 아이디어임.

https://www.acmicpc.net/source/95292255

메모리 사용량은 거의 같은데 수행 시간은 17배 더 빠름!
                                     메모리  시간(ms)
95292255 chansolpark7 1238 맞았습니다!! 36532 48	Python 3 802   <- 최적
95306485 cafrii       1238 맞았습니다!! 35508 812	Python 3 1346  <- 내 풀이

'''

import heapq
import sys

def dijkstra(graph, x):
    queue = [(0, x)]
    dist = [-1] * (n+1)
    dist[x] = 0
    while queue:
        d, x = heapq.heappop(queue)
        if dist[x] < d: continue
        for y, c in graph[x]:
            if dist[y] == -1 or dist[x] + c < dist[y]:
                dist[y] = dist[x] + c
                heapq.heappush(queue, (dist[y], y))

    return dist

n, m, x = map(int, sys.stdin.readline().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in  range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    graph1[a].append((b, t))
    graph2[b].append((a, t))

visited1 = dijkstra(graph1, x)
visited2 = dijkstra(graph2, x)

answer = 0
for i in range(1, n+1):
    answer = max(answer, visited1[i] + visited2[i])

print(answer)
