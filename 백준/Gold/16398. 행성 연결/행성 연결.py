
import sys
from heapq import heappush,heappop

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    costs = []  # heapq of format (c,i,j)
    for i in range(N):
        m = list(map(int, input().split()))
        #assert len(m) == N, f'wrong row[{i}] length'
        for j in range(i+1,N): # we care only in upper trangle
            heappush(costs, (m[j],i,j))
    return N,costs


def solve(N:int, costs:list[tuple[int,int,int]])->int:
    '''
    sort by cost
    start merge N single-node trees into one unified tree
    use mst kruscal algorithm
    return total cost
    '''
    # `costs` is heap-sorted list (ascending order)

    roots = list(range(N))  # planet: 0 ~ N-1

    def find_root(a:int):
        if a == roots[a]:
            return a
        roots[a] = ra = find_root(roots[a])
        return ra

    # we will not make cycle.
    # so, only N-1 flows are needed.
    num_flow = 0
    total_cost = 0

    # for c,a,b in costs:
    while costs:
        c,a,b = heappop(costs)
        ra,rb = find_root(a),find_root(b)
        if ra == rb: # they are alredy in same tree. skip!
            continue
        roots[rb] = roots[b] = ra # merge two tree!
        total_cost += c
        num_flow += 1
        if num_flow >= N-1:
            break
    return total_cost


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
