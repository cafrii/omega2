'''
1389번
케빈 베이컨의 6단계 법칙 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	54205	27884	22032	53.987%

문제
케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다.
케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임이다.

예를 들면, 전혀 상관없을 것 같은 인하대학교의 이강호와 서강대학교의 민세희는 몇 단계만에 이어질 수 있을까?

천민호는 이강호와 같은 학교에 다니는 사이이다. 천민호와 최백준은 Baekjoon Online Judge를 통해 알게 되었다.
최백준과 김선영은 같이 Startlink를 창업했다. 김선영과 김도현은 같은 학교 동아리 소속이다.
김도현과 민세희는 같은 학교에 다니는 사이로 서로 알고 있다.
즉, 이강호-천민호-최백준-김선영-김도현-민세희 와 같이 5단계만 거치면 된다.

케빈 베이컨은 미국 헐리우드 영화배우들 끼리 케빈 베이컨 게임을 했을때 나오는 단계의 총 합이 가장 적은 사람이라고 한다.

오늘은 Baekjoon Online Judge의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 찾으려고 한다.
케빈 베이컨 수는 모든 사람과 케빈 베이컨 게임을 했을 때, 나오는 단계의 합이다.

예를 들어, BOJ의 유저가 5명이고, 1과 3, 1과 4, 2와 3, 3과 4, 4와 5가 친구인 경우를 생각해보자.

1은 2까지 3을 통해 2단계 만에, 3까지 1단계, 4까지 1단계, 5까지 4를 통해서 2단계 만에 알 수 있다.
따라서, 케빈 베이컨의 수는 2+1+1+2 = 6이다.

2는 1까지 3을 통해서 2단계 만에, 3까지 1단계 만에, 4까지 3을 통해서 2단계 만에, 5까지 3과 4를 통해서 3단계 만에 알 수 있다.
따라서, 케빈 베이컨의 수는 2+1+2+3 = 8이다.

3은 1까지 1단계, 2까지 1단계, 4까지 1단계, 5까지 4를 통해 2단계 만에 알 수 있다.
따라서, 케빈 베이컨의 수는 1+1+1+2 = 5이다.

4는 1까지 1단계, 2까지 3을 통해 2단계, 3까지 1단계, 5까지 1단계 만에 알 수 있다.
4의 케빈 베이컨의 수는 1+2+1+1 = 5가 된다.

마지막으로 5는 1까지 4를 통해 2단계, 2까지 4와 3을 통해 3단계, 3까지 4를 통해 2단계, 4까지 1단계 만에 알 수 있다.
5의 케빈 베이컨의 수는 2+3+2+1 = 8이다.

5명의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람은 3과 4이다.

BOJ 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다.
둘째 줄부터 M개의 줄에는 친구 관계가 주어진다.
친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다.
친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다. 또, 모든 사람은 친구 관계로 연결되어져 있다.
사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.

출력
첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다.
그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.

-----

9:47~10:20, floyd..
10:29~11:?, bfs

'''



import sys
input = sys.stdin.readline

from collections import deque


def log(fmt, *args): print(fmt % args, file=sys.stderr)

def graph2str(g:list[list[int]], indent='  ')->str:
    res = []
    for ln in g:
        res.append(indent + ' '.join([str(e) for e in ln]))
    return '\n'.join(res)

def solve_floydwarshall(graph:list[list[int]])->int:
    '''
    warning: graph will be updated here.
    '''
    N = len(graph)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                # update i->j path via k
                if i == j or i == k or k == j:
                    continue
                if not (graph[i][k] and graph[k][j]):
                    continue
                if graph[i][j]: # already related? then update it.
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                else:
                    graph[i][j] = graph[i][k]+graph[k][j]

    # log('after fw:\n%s', graph2str(graph))

    # check if non-relation person exist. it should not exist!
    assert [ graph[k][j] for k in range(N) for j in range(N) if k != j ].count(0) == 0

    # get kevin bacon number of each
    relationships = [ sum(graph[k]) for k in range(N) ]
    # log('relationship count: %s', relationships)

    # if multiple ties, return smaller index (first occurrence)
    # also, we should return 1-based index
    return relationships.index(min(relationships))+1


def solve_bfs(graph:list[list[int]])->int:
    '''
    graph should contain 'direct' link only.
    graph should not be updated!
    '''
    N = len(graph)

    # convert mask graph to index graph. [[0 0 0 1 0 1] ..] -> [[3, 5], ..]
    relgraph = []
    for k in range(N):
        relgraph.append([ j for j in range(N) if graph[k][j] ])


    def get_kb(start:int)->int:
        # start 부터 시작하여, 모든 사람에게 다 도달시키도록 graph update
        INF = N+1
        distances = [INF]*N
        que = deque([start])
        distances[start] = 0
        while que:
            cur = que.popleft()
            d = distances[cur]
            for nxt in relgraph[cur]:
                # check if already visited
                if distances[nxt] < INF: continue
                que.append(nxt)
                distances[nxt] = d+1

        # 도달하지 못한 사람은 없어야 하는데..
        assert INF not in distances

        kb = sum(distances)
        # log("[%d] %s -> %d", start, distances, kb)
        return kb

    relationships = [ get_kb(k) for k in range(N) ]
    return relationships.index(min(relationships))+1

    # winner,minrel = -1,N
    # for k in range(len(graph)):
    #     rel = get_kb(k)
    #     if rel < minrel:
    #         winner,minrel = k,rel
    # return winner+1


N,M = map(int, input().split())
graph = [[0]*N for i in range(N)]
for _ in range(M):
    A,B = map(int, input().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

# log('graph\n%s', graph2str(graph))
# print(solve_bfs(graph))
print(solve_floydwarshall(graph))




'''

run=(python3 1389.py)


예제 입력 1
5 5
1 3
1 4
4 5
4 3
3 2
예제 출력 1
3


echo '5 5\n1 3\n1 4\n4 5\n4 3\n3 2' | $run
-> 3    [6, 8, 5, 5, 8]

echo '5 4\n1 2\n2 3\n3 4\n4 5' | $run
-> 3    [10, 7, 6, 7, 10]


echo '5 6\n1 3\n1 3\n1 4\n4 5\n4 3\n3 2' | $run
-> 3    [6, 8, 5, 5, 8]




# worst-case

(python3 <<EOF
import time
from random import seed,randint,shuffle

# seed(43)
seed(time.time())

N,M = 1000,5000
assert M >= N-1, "M >= N-1"

graph = [[0]*N for k in range(N)]
# first, guarantee that everyone has a relation at least.
orders = list(range(N))
shuffle(orders)
p1 = orders[0]
for p2 in orders[1:]:
    graph[p1][p2] = 1
    p1 = p2
# assert sum([sum(e) for e in graph]) == N-1

# 나머지 개수 만큼 연결 더 채우기. (M - (N-1))
rel_count = N-1
while rel_count < M:
    i,j = randint(0,N-1),randint(0,N-1)
    if i == j: continue
    if graph[i][j]: continue
    graph[i][j] = 1
    rel_count += 1

rellist = []
for k in range(N):
    rellist.extend([ (k,j) for j in range(N) if graph[k][j] ])
# print(rellist)
assert len(rellist) == M

# final print
print(N,M)
for rel in rellist:
    print(rel[0], rel[1])

EOF
) | time $run


bfs
-> $run  0.36s user 0.01s system 89% cpu 0.413 total

floyd
-> 완료 되지 못함!! 훨씬 느리다!!


'''
