import sys
from heapq import heappush, heappop

MAX_W = 1_000_000_000

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    graph = [ [] for _ in range(N+1) ]
    for _ in range(M):
        a,b,w = map(int, input().split())
        graph[a].append((b,w))
        graph[b].append((a,w))
    a,b = map(int, input().split())
    return N,graph,(a,b)

def solve_dijkstra(N:int, graph:list[list[tuple[int,int]]], fac:tuple[int,int])->int:
    '''
    '''
    start,end = fac

    mxw = [0] * (N+1)
    # mxw[k]: start 부터 k 까지 탐색된 여러 경로들 중 최대 path weight 값.
    #         값이 0 이면 아직까지 visit 하지 않은 노드.

    que = [(-MAX_W, start)]  # (-overall_weight, node)
    # max que 로 동작시키기 위해 음의 부호 붙여서 추가

    while que:
        pathw,cur = heappop(que)
        pathw = -pathw  # start 부터 cur 현재까지의 경로의 path weight

        if cur == end: # 무조건 먼저 발견되는 것 선택해도 됨. heapq가 최대 pathw 임을 보장하기 때문.
            return pathw

        for nxt,nxtw in graph[cur]:
            w = min(pathw, nxtw)
            if mxw[nxt] < w:
                mxw[nxt] = w
                heappush(que, (-w, nxt))

    return mxw[end] # 여기까지 오는 경우는 없음.

if __name__ == '__main__':
    inp = get_input()
    r = solve_dijkstra(*inp)
    print(r)
