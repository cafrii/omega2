'''
1939 를 dijkstra 가 아닌 mst 처럼 처리.
트리를 그래프로 다시 변환 하고 bfs, dfs 를 해야 하는 번거로움은 있음.

'''



import sys
from heapq import heappush, heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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
    # log("edges: %s", edges)
    # log("factory: %s", fac)

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

    def bfs(start:int, end:int)->int:
        '''
        use bfs to search path from start to end
        and return minimum edge weight
        (which is same as max allowed weight on the whole path)

        mstree 상태이므로 cycle 이 없음. 따라서 일단 목적지에 도달하기만 하면
        나중에 더 나은 값으로 갱신될 가능성이 없으므로 바로 종료 가능함.
        '''
        visited = [0]*(N+1)
        hq = [ (0,start,MAX_W) ] # (dist, node, path_weight)
        visited[start] = 1
        while hq:
            dist,cur,pathw = heappop(hq)
            if cur == end:
                return pathw
            for nxt,edgew in graph[cur]:
                if visited[nxt]: continue
                heappush(hq, (dist+1, nxt, min(edgew,pathw)))
                visited[nxt] = 1
        return MAX_W # something wrong!

    def dfs(start:int, end:int)->int:
        '''
        '''
        visited = [0]*(N+1)
        stack = [ (start,MAX_W) ]
        visited[start] = 1
        while stack:
            cur,pathw = stack.pop()
            if cur == end: return pathw
            for nxt,edgew in graph[cur]:
                if visited[nxt]: continue
                stack.append((nxt, min(edgew, pathw)))
                visited[nxt] = 1
        return MAX_W # something wrong!

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
    # return bfs(*fac)
    # return dfs(*fac)
    return dfs2(*fac)


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
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


# dijkstra 와 비교.
_T=5 _N=10 _M=40 python3 1939t.py
out1: **34**, ####
out2: **78**, ####

_T=5 _N=10 _M=24 python3 1939t.py

9 2 78
2 6 3
6 7 66
7 10 56
10 8 74
8 4 48
4 3 80
3 5 71
5 1 97
1 2 16
7 3 13
3 9 64
3 7 77
9 5 74
3 7 9
1 10 8
3 1 22
9 10 14
10 1 13
10 8 83
8 3 17
2 6 7
10 5 48
3 10 10
3 1



'''
