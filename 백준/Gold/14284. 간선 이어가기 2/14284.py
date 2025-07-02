'''
14284번
간선 이어가기 2 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	3894	2315	1949	59.403%

문제
정점 n개, 0개의 간선으로 이루어진 무방향 그래프가 주어진다. 그리고 m개의 가중치 간선의 정보가 있는 간선리스트가 주어진다.
간선리스트에 있는 간선 하나씩 그래프에 추가해 나갈 것이다. 이때, 특정 정점 s와 t가 연결이 되는 시점에서 간선 추가를 멈출 것이다.
연결이란 두 정점이 간선을 통해 방문 가능한 것을 말한다.

s와 t가 연결이 되는 시점의 간선의 가중치의 합이 최소가 되게 추가하는 간선의 순서를 조정할 때, 그 최솟값을 구하시오.

입력
첫째 줄에 정점의 개수 n, 간선리스트의 간선 수 m이 주어진다.(2≤n≤5000,1≤m≤100,000)

다음 m줄에는 a,b,c가 주어지는데, 이는 a와 b는 c의 가중치를 가짐을 말한다. (1≤a,b≤n,1≤c≤100,a≠b)
다음 줄에는 두 정점 s,t가 주어진다. (1≤s,t≤n,s≠t)
모든 간선을 연결하면 그래프는 연결 그래프가 됨이 보장된다.

출력
s와 t가 연결되는 시점의 간선의 가중치 합의 최솟값을 출력하시오,

-------

11:23~41, 채점까지 완료

이건 그냥 dijkstra 문제일 뿐이다. 말을 어렵게 써 놓았을 뿐...
최소 비용의 s->t 경로를 구하면 된다.

'''


import sys
from heapq import heappush, heappop

input = sys.stdin.readline

INF = 500001  # 5000 * 100 + 1

def solve(graph:list[list[tuple[int,int]]], s:int, t:int)->int:
    '''
    '''
    N = len(graph)-1
    mincost = [INF] * (N+1)
    que = []
    # element: (cost, node)
    heappush(que, (0, s))
    mincost[s] = 0

    while que:
        cost,now = heappop(que)
        if now == t:
            return cost
        if cost > mincost[now]: # during queued, there was visit
            continue

        for nxt,lc in graph[now]:
            # nxt: next node, lc: link cost
            if cost + lc >= mincost[nxt]: continue
            heappush(que, (cost+lc, nxt))
            mincost[nxt] = cost+lc

    return -1 # we cannot reach the goal


N,M = map(int, input().split())
graph = [[] for k in range(N+1)]
# node-0 is not used. ie, graph[0] is always [].
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int, input().split())

print(solve(graph, s, t))



'''
예제 입력 1
8 9
1 2 3
1 3 2
1 4 4
2 5 2
3 6 1
4 7 3
5 8 6
6 8 2
7 8 7
1 8
예제 출력 1
5



run=(python3 14284.py)

echo '8 9\n1 2 3\n1 3 2\n1 4 4\n2 5 2\n3 6 1\n4 7 3\n5 8 6\n6 8 2\n7 8 7\n1 8' | $run


'''
