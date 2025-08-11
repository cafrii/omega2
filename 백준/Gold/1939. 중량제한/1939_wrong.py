'''
단순 dsu 문제로만 접근하다가 실패.


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


def solve_wrong(N:int, edges:list[tuple], fac:tuple[int,int])->int:
    '''
    island number: 1-based. 1~N
    Returns:
        max possible weights that can be moved between factories
    '''

    roots = list(range(N+1))  # 0 ~ N
    minw  = [MAX_W] * (N+1)

    def find_root(a:int)->int:
        if a == roots[a]: return a
        stack = []
        while a != roots[a]:
            stack.append(a)
            a = roots[a]
        for k in stack: roots[k] = a
        return a

    for a,b,w in edges:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue # already in same set

        # select minimum weight edges to root
        roots[b] = roots[rb] = ra
        minw[ra] = min(minw[ra], w, minw[rb])

        log("  (%d,%d,%d) ra,rb %d,%d, minw %d", a, b, w, ra,rb, minw[ra])

    log("roots: %s", roots[1:])
    log("minw : %s", minw[1:])

    # check factory
    log("fac: %s", fac)

    a,b = fac
    ra,rb = find_root(a),find_root(b)
    assert ra == rb, "factory not connected"
    return minw[ra]



if __name__ == '__main__':

    inp = get_input()
    r = solve_wrong(*inp)
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
