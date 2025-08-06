import sys
from heapq import heappush, heappop

def get_input():
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    listk = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        u,v,w = map(int, input().split())
        heappush(edges, (w,u,v))
    return N,listk,edges


def solve_fast2(N:int, listk:list[int], edges:list[tuple[int,int,int]])->int:
    '''
    edges: heapque of tuple(w,u,v) where w is cost between u and v
    use kruscal to complete mst.
    '''
    K = len(listk)
    root = list(range(N+1))

    def find_root(a:int)->int:
        if a == root[a]: return a
        root[a] = find_root(root[a])
        return root[a]

    # 발전소 노드는 가상의 root(노드-0) child 로 미리 등록.
    for k in listk: root[k] = 0

    num_links = K
    total_cost = 0

    while edges:
        w,a,b = heappop(edges)
        ra,rb = find_root(a), find_root(b)
        if ra == rb: # skip if a,b is in same tree
            continue
        if ra == 0: # a 쪽의 subree 가 main
            root[b] = root[rb] = ra
        else:
            root[a] = root[ra] = rb
        total_cost += w
        num_links += 1
        if num_links >= N:
            break
    return total_cost


if __name__ == '__main__':
    inp = get_input()
    r = solve_fast2(*inp)
    print(r)
