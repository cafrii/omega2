'''

초기 구현

입력을 그래프로 받아 저장한 후
따로 원하는 트리 포맷으로 변환
그 다음에 정답 구함.
과정으로 인해 시간 소요가 좀 있음.


'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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
    log("graph: %s", graph)

    # finding root..
    is_child = [0]*(N+1)
    for n in range(1,N+1):
        for c in graph[n]: is_child[c] = 1
    root = next(i for i in range(1,N+1) if not is_child[i])
    # assume there is only one root.

    log("root: %d", root)

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

    log("parents: %s", parents)
    log("levels : %s", levels)

    # A 와 B 의 LCA (least common ancestor) 탐색. level 비교
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


'''
예제 입력 1
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5
예제 출력 1
4
3


run=(python3 3584.py)

echo '2\n16\n1 14\n8 5\n10 16\n5 9\n4 6\n8 4\n4 10\n1 13\n6 15\n10 11\n6 7\n10 2\n16 3\n8 1\n16 12\n16 7\n5\n2 3\n3 4\n3 1\n1 5\n3 5' | $run
-> 4 3

echo '1\n2\n1 2\n2 2' | $run
-> 2

'''
