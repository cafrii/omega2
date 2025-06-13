'''


제출용

'''

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
            # for nxt,lc in enumerate(graph[cur]): # for all (node,link_cost)..
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
# graph = [ [INF for e in range(N)] for s in range(N)]
graph = [ [] for s in range(N) ]
# node starts from 0. ie, instead of [1,N], i use [0,N-1].
for _ in range(M):
    s,e,c = map(int, input().split())
    # graph[s-1][e-1] = c  # convert zero-based!
    graph[s-1].append((e-1,c))

print(solve(graph, X-1))


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
-> 10


echo '6 20 3\n3 2 45\n6 1 66\n6 2 31\n2 4 94\n5 3 46\n5 2 79\n3 1 64\n4 3 74\n3 5 59\n1 6 93\n3 6 45\n6 4 40\n3 4 67\n1 3 61\n1 2 42\n4 2 50\n4 1 55\n2 6 93\n5 4 95\n1 4 54' | time $run
-> 213



'''

