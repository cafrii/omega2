
import sys
from heapq import heappush, heappop

MAX_W = 1_000_000_000

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))
    a,b = map(int, input().split())
    return N,edges,(a,b)

def solve(N:int, edges:list[tuple[int,int,int]], fac:tuple[int,int])->int:
    '''
    island number: 1-based. 1~N
    Returns:
        max possible weights that can be moved between factories
    '''
    # create min-spanning tree (w/ kruscal)
    # use largest weight edge first
    edges.sort(key=lambda x: x[2], reverse=True) # sort by weight, descending
    roots = list(range(N+1))  # 0 ~ N

    def find_root(a:int)->int:
        if a == roots[a]: return a
        stack = []
        while a != roots[a]:
            stack.append(a)
            a = roots[a]
        for k in stack: roots[k] = a
        return a

    num_edge = 0
    graph = [ [] for k in range(N+1) ]
    for a,b,w in edges:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue # already in same set

        roots[b] = roots[rb] = ra
        graph[a].append((b,w))
        graph[b].append((a,w))
        num_edge += 1
        if num_edge >= N-1:
            break

    def dfs2(start:int, end:int)->int:
        '''
        stack 에 노드 만 추가하는 방식. weight 는 상태 갱신 과 visited 역할을 같이 수행.
        '''
        INF = MAX_W + 1
        weight = [ INF ] * (N+1)
        stack = [ start ]
        weight[start] = MAX_W
        while stack:
            cur = stack.pop()
            pathw = weight[cur]
            if cur == end: return pathw
            for nxt,edgew in graph[cur]:
                if weight[nxt] < INF: continue # already visit
                stack.append(nxt)
                weight[nxt] = min(edgew, pathw)
        return MAX_W # something wrong!

    # find max allowed weights on the path between two factories.
    return dfs2(*fac)


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)

