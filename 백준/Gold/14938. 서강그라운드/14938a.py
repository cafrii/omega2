'''
dijkstra 풀이. 한번 검토해 보자. 시간은 더 단축된다.

https://www.acmicpc.net/source/95537516

'''

import sys, heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())

items = [0]
item = list(map(int, input().split()))
items.extend(item)
road = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())

    road[a].append((l,b))
    road[b].append((l,a))

def dijkstra(x):
    dist = [1e9] * (n+1)
    dist[x] = 0
    hq = [(0, x)]

    while hq:
        cost, p = heapq.heappop(hq)

        if dist[p] < cost:
            continue

        for v, u in road[p]:
            if dist[u] > cost + v and m >= cost + v:
                dist[u] = cost + v
                heapq.heappush(hq, (dist[u], u))

    return dist

answer = 0
for i in range(1, n+1):
    d = dijkstra(i)[1:]
    cnt = 0

    for index, j in enumerate(d):
        if j <= m:
            cnt += items[index+1]
    answer = max(answer, cnt)
print(answer)
