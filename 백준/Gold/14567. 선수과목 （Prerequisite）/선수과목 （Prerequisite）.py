
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    # reverse graph
    rgraph = [ [] for _ in range(N+1) ]
    for _ in range(M):
        a,b = map(int, input().split()) # a->b
        rgraph[b].append(a)
    return N,rgraph

def solve_dp(N:int, rgraph:list[list[int]])->list[int]:
    '''
    '''
    preq = [1] * (N+1) # pre-requisites
    for b in range(1, N+1):
        if not rgraph[b]: continue
        # rgraph[b] = [a1, a2, a3, ..]  a1->b, a2->b, a3->b, ..
        #   all (a1,a2,a3,..) are greater than b, by pre-condition.
        preq[b] = max(preq[a] for a in rgraph[b]) + 1
    return preq[1:]

if __name__ == '__main__':
    inp = get_input()
    print(*solve_dp(*inp))

