
import sys

def get_input():
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    lsk = list(map(int, input().split()))
    #assert len(lsk) == K, "wrong k"
    edges = []
    for _ in range(M):
        u,v,w = map(int, input().split())
        edges.append((u,v,w))
    return N,lsk,edges


def solve(N:int, listk:list[int], edges:list[tuple[int,int,int]])->int:
    '''
    edges: list of tuple(u,v,w) where w is cost between u and v
    use kruscal to complete mst.
    '''
    K = len(listk)
    edges.sort(key = lambda x: x[2]) # sort by w, ascending

    is_k = [0]*(N+1)   # 발전소 여부
    for k in listk: is_k[k] = 1

    root = list(range(N+1))
    num_links = 0
    total_cost = 0

    def find_root(a:int)->int:
        if a == root[a]: return a
        root[a] = find_root(root[a])
        return root[a]

    # 발전소를 subtree 의 root 로 하여 확장시켜야 한다.
    for a,b,w in edges:
        ra,rb = find_root(a), find_root(b)

        if ra == rb: # skip if a,b is in same tree
            continue
        if is_k[ra] and is_k[rb]: # 두 발전소 tree 를 연결할 수 없음.
            continue
        if is_k[ra]: # a 쪽에 발전소가 있음. rb 를 ra 밑으로 붙이자.
            root[b] = root[rb] = ra
        else: # b 쪽에 발전소. ra 를 rb 밑으로.
            root[a] = root[ra] = rb

        total_cost += w
        num_links += 1
        if num_links >= N - K:
            break
    return total_cost


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
