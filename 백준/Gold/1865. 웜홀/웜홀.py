
import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

INFINITY = int(1e8)
# max edge cost = 10_000, max N = 500
# max total costs ~= 500 * 10_000 = 5e6


def solve(N:int, edges:list[tuple[int,int,int]]):
    # N: number of node
    # edges: list of (start,end,cost)
    #        1<=start,end<=N
    #        cost can be negative

    # 출발 위치가 명시되어 있지 않음. 즉, 어느 노드에서도 출발 할 수 있다는 말임.
    # 모든 노드를 출발 노드로 해서 다 확인 필요. 단, 이미 방문한 노드는 skip 가능함.
    visited = [0] * (N+1)
    visited[0] = 1  # 노드 0은 사용하지 않을 것이고, 그래서 방문으로 체크.

    for S in range(N+1):
        if visited[S]: continue

        mc = [INFINITY]*(N+1) # minimum cost
        mc[S] = 0
        visited[S] = 1

        for i in range(N): # 노드 개수 횟수. 마지막 루프는 음의 사이클 검사용.
            for s,e,c in edges:
                if mc[s] == INFINITY: continue
                if mc[s]+c >= mc[e]: continue
                # update 필요
                visited[e] = 1
                if i < N-1:
                    mc[e] = mc[s] + c
                else: # 음의 cycle!
                    #log('negative cycle! S:%d, cycle:%d,%d', S, s,e)
                    return 'YES'
        #log('no cycle from S:%d', S)
    return 'NO'


TC = int(input().strip())
for _ in range(TC):
    N,M,W = map(int, input().split())
    # N(1 ≤ N ≤ 500), M(1 ≤ M ≤ 2500), W(1 ≤ W ≤ 200)
    edges = []
    graph = [ [ INFINITY for x in range(N+1) ] for y in range(N+1) ]
    # graph[k][j]: k -> j 간선의 cost
    for m in range(M):
        S,E,T = map(int, input().split())
        # 두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. -> cost 가 작은 것 하나만 선택
        # 도로는 양방향이므로 두 곳에 업데이트
        if graph[S][E] == INFINITY:
            graph[E][S] = graph[S][E] = T
        else:
            graph[E][S] = graph[S][E] = min(graph[S][E], T)

    for w in range(W):
        S,E,T = map(int, input().split())
        # 웜홀은 단방향.
        # 도로와 웜홀이 동일한 시작/끝 노드로 존재하는지는 명확하지 않지만, 있다고 하더라도 웜홀만 의미가 있음.
        if graph[S][E] == INFINITY:
            graph[S][E] = -T
        else:
            graph[S][E] = min(graph[S][E], -T)

    # 간선 정보로 취합
    for a in range(1, N+1): # 1~N
        for b in range(1, N+1):
            if graph[a][b] < INFINITY:
                edges.append((a,b,graph[a][b]))

    #log("%s", edges)
    print(solve(N,edges))
