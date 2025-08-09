'''
2350번
대운하 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	408	197	145	54.717%

문제
4대강 사업의 성공에 힘입은 정부는 대한민국의 도시들을 모두 운하로 연결하여 뱃길로 KTX를 대체하려는 계획을 세웠다.

대한민국에는 N개의 도시가 있고, 이들을 연결하는 M개의 운하를 건설하려고 한다.
하지만 지형의 문제로 운하의 폭을 제한할 수 밖에 없었기 때문에, 문제가 생겼다.
배의 폭이 운하의 폭보다 작거나 같아야 운하를 무사히 통과할 수 있기 때문이다.

정부는 K개의 노선을 준비했다.
각 노선의 도시 i와 j간을 운행하는 배는 도시 i와 j 간의 경로에 포함되는 운하를 통과할 수 있어야 한다.
(이 경로는 여러 개가 존재할 수 있다.)
배가 클수록 많은 사람을 실을 수 있으므로, 정부는 배의 폭을 최대화하기를 원한다.

N개의 도시는 운하로 서로 연결되어 있음이 보장되며, 운하는 양방향으로 통행이 가능하다.

입력
입력의 첫 번째 줄에는 도시의 수 N, 운하의 수 M, 노선의 수 K가 주어진다.
(N ≤ 1000, M ≤ 100000, K ≤ 10000)

다음 M개의 줄에는 세 정수 i, j, w가 주어지며,
이는 도시 i와 j 사이에 폭이 w인 운하를 건설할 것임을 의미한다. (1 ≤ i, j ≤ N, w ≤ 200)

다음 K개의 줄에는 각 노선이 연결하는 도시 i, j가 주어진다. (1 ≤ i, j ≤N)

출력
K개의 줄에 각 노선을 운행할 수 있는 최대 배의 폭을 출력한다.



-------

2:36~

## 조건
- N ≤ 1000, M ≤ 100000, ..

## mst 구성 방식
edge 를 2d 리스트로 하면 1000*1000*szint = 1M*28
dict 로 저장하면, 10만개..

## 절차
1.
먼저 최소 비용 트리 (mst) 구성.
운하의 폭이 간선의 비용인데, 폭이 클 수록 비용이 적음.

2.
만들어진 트리 내에서, 주어진 임의의 두 노드 간의 경로를 구하고
(경로는 하나만 존재한다.) 경로 상의 최소 폭 간선을 찾아야 한다.
a, b 라면 c = nca(a,b) 를 구하고
min_edge(path(a,b)) = min_edge(path(a,c), path(c,b))
를 구한다.


'''


import sys
from collections import defaultdict
from heapq import heappush, heappop



def log(fmt, *args): print(fmt % args, file=sys.stderr)

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
    log("mst graph: %s", graph)

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

    # tree 는 (parent, width, level)

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
        log("a-root path: %s", branch_a)

        nca = 0
        branch_b = []
        width = max_w
        while b > 0:
            branch_b.append((b,width))
            if b in set_a: break # b is nca node
            width = min(width, tree[b][1])
            b = tree[b][0]
        nca = b
        log("b-nca path: %s", branch_b)

        i = next(i for i,(a,_) in enumerate(branch_a) if a == nca)
        del branch_a[i+1:] # remove elements after nca

        log("a-nca path: %s", branch_a)

        minw_a = min(w for n,w in branch_a)
        minw_b = min(w for n,w in branch_b)
        log("min-a: %d, min-b: %d", minw_a, minw_b)

        return min(minw_a, minw_b)

    return [ find_cap(a,b) for a,b in cities ]


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print('\n'.join(map(str, r)))



'''
예제 입력 1
6 9 4
1 2 2
1 4 3
1 6 1
2 3 3
2 5 2
3 4 4
3 6 2
4 5 5
5 6 4
2 6
3 5
1 2
4 6

예제 출력 1
3
4
3
4

run=(python3 2350.py)

echo '6 9 1\n1 2 2\n1 4 3\n1 6 1\n2 3 3\n2 5 2\n3 4 4\n3 6 2\n4 5 5\n5 6 4\n2 6' | $run
-> 3

echo '6 9 4\n1 2 2\n1 4 3\n1 6 1\n2 3 3\n2 5 2\n3 4 4\n3 6 2\n4 5 5\n5 6 4\n2 6\n3 5\n1 2\n4 6' | $run
-> 3 4 3 4

echo '7 6 3\n1 2 3\n1 3 1\n2 4 4\n2 5 5\n3 6 9\n3 7 2\n5 7\n5 4\n1 5' | $run
-> 1 4 3

echo '7 6 1\n1 2 3\n1 3 1\n2 4 4\n2 5 5\n3 6 9\n3 7 2\n5 5' | $run
-> 200



(python3 <<EOF
import time
from random import seed,randint,shuffle
# seed(time.time())
seed(43)
N,M,K = 1000,100_000,10_000
# N,M,K = 10,20,10
orders = list(range(1,N+1)) # 1~N
shuffle(orders)
edges = [ (orders[k-1],orders[k],randint(1,200)) for k in range(1,len(orders)) ]
# N-1 edges generated with all cities connected. add more random edges.
while len(edges) < M:
    i,j,w = randint(1,N),randint(1,N),randint(1,200)
    if i == j: continue
    edges.append((i,j,w))
cities = []
while len(cities) < K:
    i,j = randint(1,N),randint(1,N)
    if i == j: continue
    cities.append((i,j))
print(N,M,K)
for i,j,w in edges: print(i,j,w)
for i,j in cities: print(i,j)
EOF
) | time $run


'''

