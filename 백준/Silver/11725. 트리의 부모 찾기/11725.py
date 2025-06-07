'''
11725번

트리의 부모 찾기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	107078	49309	34464	43.604%

문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

----

4:18~38

'''


import sys
input = sys.stdin.readline

from typing import Iterable


def solve(N:int, graph:list[list])->Iterable:
    # traverse tree, to find parent node
    # returns 'iterable' from which parent node is iterated since node 2.
    #
    parent = [-1]*(N+1)
        # parent[k] means parent of node-k.
        #  valid range: 1 ~ N-1
        #  -1: unknown (not visited yet)
    stack = [1]
    parent[1] = 0 # 0 means it is root!

    while stack:
        u = stack.pop()
        for v in graph[u]:
            if parent[v] >= 0: continue # already visited
            stack.append(v)
            parent[v] = u

    for i in range(2,N+1):
        # check all nodes has parent
        assert parent[i] > 0
        yield parent[i]


N = int(input().strip())
# 2 <= N <= 100_000

graph = [ [] for k in range(N+1) ]

for _ in range(N-1):
    u,v = map(int, input().split())
    assert 1<=u<=N and 1<=v<=N
    graph[u].append(v)
    graph[v].append(u)

it = solve(N, graph)
print(*it, sep='\n')




'''
예제 입력 1
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1
4
6
1
3
1
4

run=(python3 11725.py)
echo '7\n1 6\n6 3\n3 5\n4 1\n2 4\n4 7' | $run


예제 입력 2
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
예제 출력 2
1
1
2
3
3
4
4
5
5
6
6




(python3 <<EOF
N = 100_000
print(N)
for k in range(1,N):
    print(k, k+1)
EOF
) | time $run > /dev/null

->  0.16s user 0.02s system 99% cpu 0.183 total



'''
