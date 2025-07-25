import sys
from typing import Generator

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    def gen_lines()->Generator:
        for i in range(M):
            a,b = map(int, input().split())
            yield (i+1,a,b) # index is 1-based.
        return
    return (N,gen_lines())

def solve(N:int, g:Generator[tuple[int,int,int]]):
    '''
    '''
    parent = [ k for k in range(N) ]
    depth = [0] * N

    def find_root(node:int)->int:
        if node != parent[node]:
            parent[node] = find_root(parent[node])
        return parent[node]

    for idx,a,b in g:
        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            return idx

        if depth[root_a] > depth[root_b]:
            parent[root_b] = root_a
        elif depth[root_a] < depth[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            depth[root_a] += 1
    return 0


if __name__ == '__main__':
    inp = get_input()
    print(solve(*inp))
