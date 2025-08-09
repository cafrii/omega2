
import sys

def get_input():
    # return generator
    input = sys.stdin.readline
    T = int(input().rstrip())
    for _ in range(T):
        N = int(input().rstrip())
        graph = [ [] for k in range(N+1) ]
        for _ in range(N-1):
            p,c = map(int, input().split()) # parent, child
            graph[p].append(c)
        a,b = map(int, input().split())
        yield N,graph,a,b
    return

def solve(N:int, graph:list[list[int]], A:int, B:int)->int:
    '''
    graph 관계를 parent, level 형식의 트리로 표현.
    그 다음 level 비교를 통한 lca 알고리즘 사용.
    '''
    # finding root..
    is_child = [0]*(N+1)
    for n in range(1,N+1):
        for c in graph[n]: is_child[c] = 1
    root = next(i for i in range(1,N+1) if not is_child[i])
    # assume there is only one root.

    parents = list(range(N+1))
    levels = [-1]*(N+1)

    # 트리 노드의 level 결정. dfs 탐색. non-recursive.
    parents[root] = root
    levels[root] = 0
    stack = [root]

    while stack:
        node = stack.pop()
        lvl = levels[node]
        for c in graph[node]:
            if levels[c] >= 0: continue # cycle 방지용. 문제 조건에 의해 없어도 되긴 함.
            parents[c] = node
            levels[c] = lvl+1
            stack.append(c)

    # A 와 B 의 LCA (least common ancestor) 탐색
    def find_lca(a:int, b:int)->int:
        # let a be deeper node
        if levels[a] < levels[b]:
            a,b = b,a
        # go up until they are same level
        lvlb = levels[b]
        while levels[a] != lvlb:
            a = parents[a]
        # go up until they meet
        while a != b:
            a,b = parents[a],parents[b]
        return a

    return find_lca(A, B)


if __name__ == '__main__':
    it = get_input()
    for inp in it:
        r = solve(*inp)
        print(r)
