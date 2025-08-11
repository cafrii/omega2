
import sys

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

    start,end = fac
    if start == end: return MAX_W

    # 가장 큰 edge-weight 부터 순회하므로 
    # 최초로 same-set 이 되는 그 순간의 edge-weight 가 정답
    for a,b,w in edges:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue # already in same set
        roots[b] = roots[rb] = ra
        if find_root(start) == find_root(end):
            return w
    return 0 # 이 경우는 발생하면 안됨

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
