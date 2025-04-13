
import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

INFINITY = int(1e8)

def solve2(K, probe:list[tuple]):
    #
    # 정수 칸 대신 위치와 위치 사이 지점을 노드로 간주한다.
    # 문제에서는 1 ~ K 까지의 숫자 칸으로 설명했지만
    # 우리는 0 ~ K 까지의 노드로 관리. 그래야 그래프를 그리기 편함.
    #
    #          +-----+-----+-----+-----+---------+-----+
    #          |  1  |  2  |  3  |  4  | ...     |  K  |
    #          +-----+-----+-----+-----+---------+-----+
    #  Node   (0)---(1)---(2)---(3)---(4)- .. -(K-1)--(K)
    #
    #  Example       [  #     _  ]     Probe[2,3]=1
    #         (0)---(1)---(2)---(3)---(4)--
    #  edge            \---1---/       edge (1,3), cost 1
    #
    # 그래프로 풀기 위해, 물체의 개수를 간선에 대한 cost로 인식.
    # 방향 그래프이며 역방향은 음의 cost
    edges = []
    for x,y,r in probe:
        edges.append((x-1, y, r))
        edges.append((y, x-1, -r))

    # 노드 사이에는 최대 1개의 물체만 가능. 즉 최대 cost를 1로 등록
    for i in range(1, K+1): # 1~K
        edges.append((i-1, i, 1))
        edges.append((i, i-1, 0))

    min_cost = [ INFINITY for x in range(K+1) ]
    min_cost[0] = 0

    # 노드 개수가 0 부터 K 까지 총 K+1 이고,
    #  K+1 루프는 음의 사이클 감지용.
    for i in range(K+1):
        for s,e,c in edges: # start, end, cost
            if min_cost[s] == INFINITY: continue
            if min_cost[s] + c >= min_cost[e]: continue
            if i < K:
                min_cost[e] = min_cost[s] + c
            else:
                #log("negative cycle!")
                return 'NONE'

    #log("min_cost: %s", min_cost)
    ans = []
    for i in range(1, K + 1): # 1~K
        # 차이는 0 아니면 1 이어야 함.
        ans.append('#' if min_cost[i-1] < min_cost[i] else '-')
    return ''.join(ans)


K, N = map(int, input().split())
probe = []
for _ in range(N):
    x,y,r = map(int, input().split())
    probe.append((x,y,r))

ans = solve2(K, probe)
print(ans)
