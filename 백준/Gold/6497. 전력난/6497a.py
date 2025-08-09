'''

두번째 제출.

전체 비용 계산 없이, mst 완성 이후에 절감 비용만 별도 계산.
그런데 첫번째 제출보다도 더 느렸음. why?

'''

import sys

def get_input():
    # return generator
    input = sys.stdin.readline
    while True:
        m,n = map(int, input().split())
        if m == 0:
            break
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
    saved_cost = 0

    for a,b,dist in edges:
        ra,rb = find_root(a),find_root(b)
        if ra == rb:
            saved_cost += dist
        else:
            roots[rb] = roots[b] = ra
    return saved_cost

if __name__ == '__main__':
    it = get_input()
    for m,edges in it:
        r = solve(m, edges)
        print(r)

