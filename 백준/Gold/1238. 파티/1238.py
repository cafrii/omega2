'''
1238번

파티 성공다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	60624	31682	21208	49.541%

문제
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다.
하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다.
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다.
두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다.
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.

----

10:13~10:40 1차, 최적화 없음.

이 코드로 시간 초과 걸린 이후에 graph 구조를 바꾸었음. 1238a.py 참고.

'''

# from collections import
from heapq import heappush,heappop

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

INF = 100*1000 # int(1e8)


def solve(graph, X):
    N = len(graph)

    def find_mincost(frm,to):
        #
        # log("find_mincost: %d -> %d", frm, to)
        que = []
        mincost = [INF]*N
        heappush(que, (0,frm))
        mincost[frm] = 0

        while que:
            cost,cur = heappop(que)
            # log("pop: (%d, %d)", cost, cur)
            if cur == to:
                # log("**** [node %d] --> reached to goal %d, cost %d", frm, to, cost)
                return cost
            if mincost[cur]<cost:
                continue
            for nxt,lc in enumerate(graph[cur]):
                if lc >= INF: continue
                if mincost[nxt] <= cost+lc: continue
                # log("push: cost %d+%d=%d, next %d)", cost, lc, cost+lc, nxt)
                heappush(que, (cost+lc,nxt))
                mincost[nxt] = cost+lc

                # 중간 계산 결과를 재활용해 보려는 시도..
                # graph[frm][nxt] = min(cost+lc, graph[frm][nxt])
                # 추가 전: 0.02s user 0.01s system 66% cpu 0.040 total
                # 추가 후: 0.02s user 0.01s system 64% cpu 0.039 total

        return INF

    # log("test: 0->1: %d", find_mincost(0,1))
    # log("#### test: 1->2: %d", find_mincost(1,2))

    costs_all = []
    for node in range(N): # for each node
        mc1 = find_mincost(node,X)
        mc2 = find_mincost(X,node)
        if max(mc1, mc2) >= INF:
            log("node %d cost exceed max, %d %d", node, mc1, mc2)
        costs_all.append(mc1 + mc2)
        log("node %d: %d, %d", node, mc1, mc2)

    log("costs: %s", costs_all)
    return max(costs_all)


N,M,X = map(int, input().split())
# input links, s/e/c

graph = [ [INF for e in range(N)] for s in range(N)]
# 노드 번호를 0부터 시작하는 것으로 간주함.
# 즉, 1~N 이 아니고 0~N-1

for _ in range(M):
    s,e,c = map(int, input().split())
    graph[s-1][e-1] = c

log("graph:\n%s", '\n'.join([ ' '.join([
            (str(e2) if e2<INF else '.') for e2 in e1
        ]) for e1 in graph
    ]))

print(solve(graph,X-1))


'''
예제 입력 1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3

예제 출력 1
10

run=(python3 1238.py)

echo '4 8 2\n1 2 4\n1 3 2\n1 4 7\n2 1 1\n2 3 5\n3 1 2\n3 4 4\n4 2 3' | $run



echo '6 20 3\n3 2 45\n6 1 66\n6 2 31\n2 4 94\n5 3 46\n5 2 79\n3 1 64\n4 3 74\n3 5 59\n1 6 93\n3 6 45\n6 4 40\n3 4 67\n1 3 61\n1 2 42\n4 2 50\n4 1 55\n2 6 93\n5 4 95\n1 4 54' | time $run
->213



'''

