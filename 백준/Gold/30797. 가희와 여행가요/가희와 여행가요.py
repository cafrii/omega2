import sys
from heapq import heappush, heappop

def get_input_kruscal():
    input = sys.stdin.readline
    N,Q = map(int, input().split())
    edges = []
    for _ in range(Q):
        a,b,c,t = map(int, input().split())
        heappush(edges, (c,t,a,b))
    return N,edges

def solve_kruscal(N:int, edges:list):
    roots = list(range(N+1))

    def find_root(a:int)->int:
        if roots[a] == a: return a
        roots[a] = find_root(roots[a])
        return roots[a]

    num_links,total_cost = 0,0
    finished_at = 0
    while edges:
        c,t,a,b = heappop(edges)
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue  # cycle!

        roots[rb] = roots[b] = ra
        total_cost += c
        num_links += 1
        finished_at = max(finished_at, t)

        if num_links >= N-1:
            return finished_at,total_cost
    return -1,-1

if __name__ == '__main__':
    sys.setrecursionlimit(3 * (10**5))
    inp = get_input_kruscal()
    t,c = solve_kruscal(*inp)
    if t < 0: print(-1)
    else: print(t, c)

