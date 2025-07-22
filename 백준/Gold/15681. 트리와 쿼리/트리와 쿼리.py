
import sys

#def log(fmt, *args): print(fmt % args, file=sys.stderr)

# MAX_N = int(1e5)

def get_input():
    input = sys.stdin.readline
    N,R,Q = map(int, input().split())
    links = [ [] for k in range(N+1) ]
    # [ linked_nodes.. ]
    for _ in range(N-1):
        u,v = map(int, input().split())
        links[u].append(v)
        links[v].append(u)
    queries = []
    for _ in range(Q):
        queries.append(int(input().strip()))
    return N,R,links,queries


def solve(N, R, links:list[list[int]], queries)->list[int]:
    '''
    '''
    assert len(links) == N+1, "wrong links size"

    visited = [0] * (N+1)  #
    treesz = [0] * (N+1)   # mem: 100K * 4 (32bit)

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, int(N * 1.5)))

    def count_subtree_recursive(subroot:int, parent:int):
        treesz[subroot] = 1
        visited[subroot] = 1
        for n in links[subroot]:
            if n == parent:
                continue
            if visited[n]:
                #log("!! cycle! %d -> %d", subroot, n)
                continue
            count_subtree_recursive(n, subroot)
            treesz[subroot] += treesz[n]

    count_subtree_recursive(R, 0)
    # log("root %d, total size %d", R, treesz[R])

    return [ treesz[q] for q in queries ]


if __name__ == '__main__':
    inp = get_input()
    answer = solve(*inp)
    print('\n'.join(map(str, answer)))

