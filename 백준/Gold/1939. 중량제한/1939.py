'''
1939번
중량제한
골드3

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	43860	12560	7745	26.595%

문제
N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다.
이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다.
물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다.
그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다.
만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M(1 ≤ M ≤ 100,000)이 주어진다.
다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)가 주어진다.
이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다.
서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다.
마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다.
공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.

출력
첫째 줄에 답을 출력한다.

----------

3:37~3:51 실패.
dsu 문제인 줄 알았는데, 그래프 문제이다.

가장 중량제한이 높은 (조건이 좋은) 다리 순서로 정렬한 후
mst 트리를 구성한다.

노드 N: 2 ≤ N ≤ 10,000
간선 M: 1 ≤ M ≤ 100,000

노드 수에 비해 간선이 적은 편. kruscal 추천.
필요 정보: edges list(tuple(a,b,w))
결과물: graph[a]: [ (b,w), .. ]

완전한 트리를 구성하는 건 다시 graph -> dfs 등을 통해야 하는데,
굳이 트리 구성 필요 없이 bfs 로 바로 문제를 풀도록 한다.

-----------

그 외에도 여러가지 다른 알고리즘으로 해결하는 방법들이 있는 모양이다.
각각에 대해서도 검토를 해 보도록 하자.

순수하게 dijkstra 로만 풀 수 있는가?
풀 수 있음!
이것으로 먼저 제출.

---------
속도 개선

97359241 cafrii  1939 맞았습니다!! 50120KB 164ms Python 3 1428B   <- (4) dsu 개선  (1939_dsu2.py)
97358535 cafrii  1939 맞았습니다!! 53700KB 220ms Python 3 2082B   <- (3) mst/kruscal, dfs2  (1939_dsu.py)
97357378 cafrii  1939 맞았습니다!! 66184KB 236ms Python 3 1423B   <- (2) dijkstra optimized  (1939.py)
97357164 cafrii  1939 맞았습니다!! 73112KB 268ms Python 3 1478B   <- (1) dijkstra


'''



import sys
from heapq import heappush, heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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

    # trimming
    # 탐색 전에 미리 edge 정리를 수행하는 작업인데, 이게 훨씬 더 느리게 함??

    # for a in range(1,N+1):
    #     if not graph[a]: continue
    #     graph[a].sort(key=lambda x:x[1], reverse=True) # large weight first

    #     # if not graph[a]: continue
    #     # wl = [0]*(N+1)
    #     # for i,(b,w) in enumerate(graph[a]):
    #     #     wl[b] = max(w, wl[b])  # remove redundancy
    #     # graph[a] = [  (b, wl[b]) for b in range(1,N+1) if wl[b] > 0 ]
    #     # graph[a].sort(key=lambda x:x[1], reverse=True) # large weight first

    start,end = fac

    mxw = [0] * (N+1)
    # mxw[k]: start 부터 k 까지 탐색된 여러 경로들 중 최대 path weight 값.
    #         값이 0 이면 아직까지 visit 하지 않은 노드.

    que = [(-MAX_W, start)]  # (-overall_weight, node)
    # max que 로 동작시키기 위해 음의 부호 붙여서 추가

    while que:
        pathw,cur = heappop(que)
        pathw = -pathw  # start 부터 cur 현재까지의 경로의 path weight

        # log("(%d, w %d)", cur, pathw)

        if cur == end: # 무조건 먼저 발견되는 것 선택해도 됨. heapq가 최대 pathw 임을 보장하기 때문.
            return pathw

        # log("   edge: %s", graph[cur])
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




'''
예제 입력 1
3 3
1 2 2
3 1 3
2 3 2
1 3

예제 출력 1
3


run=(python3 1939.py)

echo '3 3\n1 2 2\n3 1 3\n2 3 2\n1 3' | $run
# -> 3

echo '3 2\n1 2 1\n2 3 2\n1 2' | $run
# -> 1

echo '3 2\n1 2 1\n2 3 2\n2 3' | $run
# -> 2

echo '3 2\n1 2 1\n2 3 2\n1 3' | $run
# -> 1



속도 개선 실험

_T=100 _N=10000 _M=100000 python3 1939t.py
...
0.15 real         0.14 user         0.00 sys  # dijkstra
0.09 real         0.09 user         0.00 sys  # dsu
0.07 real         0.06 user         0.00 sys  # dsu2


'''
