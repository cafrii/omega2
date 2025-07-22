'''
 15681번
제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
난이도 기여
질문 게시판
트리와 쿼리 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	21903	10446	7917	45.224%
문제
간선에 가중치와 방향성이 없는 임의의 루트 있는 트리가 주어졌을 때, 아래의 쿼리에 답해보도록 하자.

정점 U를 루트로 하는 서브트리에 속한 정점의 수를 출력한다.
만약 이 문제를 해결하는 데에 어려움이 있다면, 하단의 힌트에 첨부한 문서를 참고하자.

입력
트리의 정점의 수 N과 루트의 번호 R, 쿼리의 수 Q가 주어진다. (2 ≤ N ≤ 105, 1 ≤ R ≤ N, 1 ≤ Q ≤ 105)

이어 N-1줄에 걸쳐, U V의 형태로 트리에 속한 간선의 정보가 주어진다. (1 ≤ U, V ≤ N, U ≠ V)

이는 U와 V를 양 끝점으로 하는 간선이 트리에 속함을 의미한다.

이어 Q줄에 걸쳐, 문제에 설명한 U가 하나씩 주어진다. (1 ≤ U ≤ N)

입력으로 주어지는 트리는 항상 올바른 트리임이 보장된다.

출력
Q줄에 걸쳐 각 쿼리의 답을 정수 하나로 출력한다.


----

10:05~50

재귀 호출 없이 dfs 로 해 보려고 했는데 구조가 더 복잡해졌음.
그래서 일단 재귀 호출로 제출.

이것을 dp로 풀 수 있는 지도 한번 생각을 해 보아야 함.
미리 계산을 해 놓는 것이므로 dfs 로 아래에서부터 계산해 올라가는 것도 dp라고 부를 수 있다.

재귀 vs. 비-재귀 수행 성능

이번 문제를 재귀 호출 없이 해결하려면, 트리의 후위 순회를 해야 한다.
각 노드 별로 stack 에 두 번 들어간다.
첫번째 방문은 깊이 우선 탐색, 두번째 방문은 size sum 계산이다.
스택의 push, pop 연산이 x2 로 수행되어야 해서,
이런 복잡한 과정이 없는 재귀 호출 보다 더 느려지는 것으로 보인다.


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MAX_N = int(1e5)

def get_input():
    input = sys.stdin.readline

    N,R,Q = map(int, input().split())
    links = [ [] for k in range(N+1) ]
    # links[k]: list of all nodes which are connected to node-k, including parent.
    # links[0] is not used.

    for _ in range(N-1):
        u,v = map(int, input().split())
        links[u].append(v)
        links[v].append(u)

    queries = []
    for _ in range(Q):
        queries.append(int(input().strip()))
    return N,R,links,queries


def solve_recursive(N, R, links:list[list[int]], queries)->list[int]:
    '''

    '''
    # log("N %d, R %d, Q %s", N, R, queries)
    # log("links: %s", links)

    assert len(links) == N+1, "wrong links size"
    # Q = len(queries)

    visited = [0] * (N+1)  # mem: 100K * 4 (32bit)
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
                log("!! cycle! %d -> %d", subroot, n)
                continue
            count_subtree_recursive(n, subroot)
            treesz[subroot] += treesz[n]

    count_subtree_recursive(R, 0)
    # log("root %d, total size %d", R, treesz[R])

    return [ treesz[q] for q in queries ]



def solve_nonrecursive(N:int, R:int, links:list[list[int]], queries)->list[int]:
    '''
    Args:
        N: number of nodes in tree
        R: root node
        links: all links in tree (no weight, bi-directional)
        queries: queries of question:
            what is the size(number of nodes) of subtree whose sub-root is queries[k]?
    Returns:
        list of answers, ie, size of each subtree. (length = len(queries))

    스택을 두 벌 관리하여 더 복잡하다.
    아래 solve_dfs() 가 더 최적이다.
    '''

    visited = [0] * (N+1)  # mem: 100K * 4 (32bit)
    treesz = [0] * (N+1)   # mem: 100K * 4 (32bit)

    stack = [R]
    rstack = [R]
    visited[R] = 1

    while stack:
        c = stack.pop() # current node

        n_child = 0
        for n in links[c]:
            if visited[n]: # it might be parent
                continue
            stack.append(n)
            rstack.append(n)
            visited[n] = 1
            n_child += 1
        if n_child == 0: # leaf
            treesz[c] = 1

    for c in reversed(rstack):
        if treesz[c] == 1: continue
        treesz[c] = sum( treesz[n] for n in links[c] ) + 1

    return [ treesz[q] for q in queries ]



def solve_dfs(N:int, R:int, links:list[list[int]], queries)->list[int]:
    '''
    Args:
        N: number of nodes in tree
        R: root node
        links: all links in tree (no weight, bi-directional)
        queries: queries of question:
            what is the size(number of nodes) of subtree whose sub-root is queries[k]?
    Returns:
        list of answers, ie, size of each subtree. (length = len(queries))

    재귀 호출 없는 구현이지만, 수행 속도는 solve_recursive() 보더 더 느린 것으로 측정된다.
    '''

    visited = [0] * (N+1)  # mem: 100K * 4 (32bit)
    treesz = [0] * (N+1)   # mem: 100K * 4 (32bit)

    stack = [(R, False)] # (node, children_processed)
    visited[R] = 1
    # 주의: visited 설정 시점이 위의 구현들과는 약간 다르니 주의.

    while stack:
        node,childready = stack.pop() # current node

        if not childready:
            visited[node] = 1
            stack.append((node, True))

            for c in links[node]: # for all children..
                if visited[c]: # c is parent of node
                    continue
                stack.append((c, False))
        else:
            # assume there is no cycle!
            # then 'if' condition is not required.
            treesz[node] = 1 + sum( treesz[c] for c in links[node]
                                # if visited[c] and c != node
                                )
    return [ treesz[q] for q in queries ]




if __name__ == '__main__':
    inp = get_input()

    # log("args: %s", sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == 'recursive':
        log("recursive")
        answer = solve_recursive(*inp)
        print('\n'.join(map(str, answer)))
    else:
        log("non-recursive")
        # answer = solve_nonrecursive(*inp)
        answer = solve_dfs(*inp)
        print('\n'.join(map(str, answer)))



'''

예제 입력 1
9 5 3
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
5
4
8
예제 출력 1
9
4
1

run=(python3 15681.py)

echo '9 5 3\n1 3\n4 3\n5 4\n5 6\n6 7\n2 3\n9 6\n6 8\n5\n4\n8' | $run


_T=10 python3 15681t.py

'''

