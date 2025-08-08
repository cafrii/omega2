
import sys

def get_input():
    # return generator
    input = sys.stdin.readline
    while True:
        m,n = map(int, input().split())
        if m == 0: break
        edges = []
        for _ in range(n):
            edges.append(tuple(map(int, input().split())))
        yield m,edges  # number of houses, edges
    return

def solve(m:int, edges:list[tuple[int,int,int]])->int:
    '''
    Arguments:
        m: number of houses
        1 ≤ m ≤ 200_000, m-1 ≤ n ≤ 200_000
        edges: list of tuple(i,j,d) distance d between house i and j.
    Returns:
        max savings possible
    '''
    roots = list(range(m))

    def find_root(a:int)->int:
        if roots[a] == a: return a
        stack = []
        while roots[a] != a:
            stack.append(a)
            a = roots[a]
        for k in stack: roots[k] = a
        return a

    edges.sort(key=lambda x: x[2]) # sort by distance, ascending

    total_cost = sum(k for i,j,k in edges)
    num_roads, opt_cost = 0,0

    for a,b,dist in edges:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue
        # make union
        roots[rb] = roots[b] = ra
        num_roads += 1
        opt_cost += dist
        if num_roads >= m-1:
            break
    return total_cost - opt_cost

if __name__ == '__main__':
    it = get_input()
    for m,edges in it:
        r = solve(m, edges)
        print(r)
