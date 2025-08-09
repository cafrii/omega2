
import sys

def get_input():
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    edges,cities = [],[]
    for _ in range(M):
        i,j,w = map(int, input().split())
        edges.append((i,j,w))
    for _ in range(K):
        i,j = map(int, input().split())
        cities.append((i,j))
    return N,edges,cities


def solve(N:int, edges:list[tuple], cities:list[tuple])->list[int]:
    '''
    Arguments:
        - N: number of city. city: 1 ~ N
        - edges: list of tuple (i,j,w)
                 where w is canal-width between city i and j
        - cities: two city whose canal-width that we should find.
    Returns:
        - list of max ship size allowed in canal between two city
    '''

    max_w = 200
    graph = [ [] for k in range(N+1) ]

    def get_mst():
        '''
        create min spaning tree with max-width edges
        using kruscal algorithm
        '''
        roots = list(range(N+1))
        # dsu (disjoint set union) 을 만들 때 필요한 정보
        # roots[k] 는 node-k 가 속한 트리의 root.
        # 초기에는 자기 자신 노드 하나로만 구성된 single-node tree.

        def find_root(a:int)->int:
            if a == roots[a]: return a
            stack = []
            while a != roots[a]:
                stack.append(a)
                a = roots[a]
            for s in stack: roots[s] = a
            return a

        edges.sort(key=lambda x: x[2], reverse=True) # sort by width, descending
        num_links = 0

        for a,b,w in edges:
            ra,rb = find_root(a),find_root(b)
            if ra == rb: continue # 이미 같은 dsu 에 속한 상태

            graph[a].append((b,w))
            graph[b].append((a,w))
            # make union
            roots[b] = roots[rb] = ra
            num_links += 1
            if num_links >= N-1:
                break
        return

    get_mst()

    tree = [ (-1,-1,-1) for k in range(N+1) ]
    # tuple (parent, edge width (node-parent), level(depth))

    # dfs 로 트리 구성.
    def dfs(root:int):
        stack = [root]
        tree[root] = (0,0,0) # parent 0 means that this is root node
        while stack:
            node = stack.pop()
            depth = tree[node][2]
            for nxt,w in graph[node]:
                if tree[nxt][0] >= 0: continue  # already in tree
                tree[nxt] = (node, w, depth+1)  # parent, edge width
                stack.append(nxt)
        return

    dfs(1) # 임의 노드를 root로 하여 tree 생성
    # tree[]: (parent, width, level)

    def find_cap(a:int, b:int)->int:
        '''
        Returns:
            도시 a 와 b 사이의 경로 capacity
            (경로 구성 edge 의 width 의 최소값)
        '''
        # a 에서 시작하여 root 까지 이르는 branch node 정보 수집
        branch_a,set_a = [],set()
        width = max_w
        while a > 0:
            branch_a.append((a,width))
            set_a.add(a)
            width = min(width, tree[a][1])
            a = tree[a][0]
        # b 부터 시작하는 branch node 정보. nca 탐색도 같이.
        nca = 0
        branch_b = []
        width = max_w
        while b > 0:
            branch_b.append((b,width))
            if b in set_a: break # b is nca node
            width = min(width, tree[b][1])
            b = tree[b][0]
        nca = b

        i = next(i for i,(a,_) in enumerate(branch_a) if a == nca)
        del branch_a[i+1:] # remove elements after nca
        
        minw_a = min(w for n,w in branch_a)
        minw_b = min(w for n,w in branch_b)

        return min(minw_a, minw_b)

    return [ find_cap(a,b) for a,b in cities ]


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print('\n'.join(map(str, r)))
