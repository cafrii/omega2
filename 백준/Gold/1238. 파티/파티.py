from heapq import heappush,heappop
import sys
input = sys.stdin.readline

INF = 100*1000 # int(1e8)

def solve(graph:list[list], target):
    # target: node where party is on.
    N = len(graph)

    def findmc(frm,to):
        # find minimum cost from node 'frm' to node 'to'.
        if frm == to: return 0
        que = []
        mincost = [INF]*N
        heappush(que, (0,frm))
        mincost[frm] = 0

        while que:
            cost,cur = heappop(que)
            if cur == to: # reached to goal.
                # return cost
                return mincost[cur]
            if mincost[cur] < cost: # cost updated while que waiting.
                continue
            for nxt,lc in graph[cur]: # for all (node,link_cost)..
                if nxt == cur: continue
                if lc >= INF: continue
                if mincost[nxt] <= cost+lc: continue
                heappush(que, (cost+lc,nxt))
                mincost[nxt] = cost+lc

        return INF # cannot reach. it should not happen.

    max_cost = max(findmc(n,target)+findmc(target,n) for n in range(N))
    return max_cost


N,M,X = map(int, input().split())
graph = [ [] for s in range(N) ]
# node starts from 0. ie, instead of [1,N], i use [0,N-1].
for _ in range(M):
    s,e,c = map(int, input().split())
    graph[s-1].append((e-1,c))

print(solve(graph, X-1))
