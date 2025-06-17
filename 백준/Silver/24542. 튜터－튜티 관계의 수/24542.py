'''
24542번

튜터-튜티 관계의 수 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	1024 MB (추가 메모리 없음)	1283	509	405	38.980%

문제
대학생 찬솔이는 이번 학기부터 헬로알고에서 멘토로 활동하게 되었다. 현재 찬솔이가 담당한 반에는 총
$N$명의 교육생이 있다.

사전 정보를 통해 찬솔이는 헬로알고 교육생 간의 친분 관계를 나타내는 양방향 그래프를 하나 획득할 수 있었다.
정말 특이하게도 이 친분 관계를 나타낸 그래프는 포레스트 형태였다. 포레스트란 사이클이 없는 그래프를 의미한다.
찬솔이는 이 교육생 간 친분관계를 토대로 교육생들끼리 튜터-튜티 관계를 구성하고자 한다.
튜터-튜티 관계는 기존에 친분 관계가 있던 두 사람 사이에서만 정할 수 있으며 단방향으로만 지정할 수 있다.

찬솔이가 배포한 교육 자료는 튜터가 튜티에게만 전달할 수 있도록 하였다.
이런 방식으로 모든 교육생에게 교육 자료가 전달되어야만 한다. 이렇게 되면 부득이하게 찬솔이로부터 최초로 교육 자료를 받는 인원이 생길 수밖에 없다.
찬솔이는 수줍음이 많은 성격이기 때문에 이런 인원수가 최소가 되기를 희망한다.

위 조건을 만족하면서 교육생의 튜터-튜티 관계를 정하는 경우의 수를
$1\,000\,000\,007$로 나눈 나머지를 출력하자.

입력
교육생의 수
$N$과 친분 관계의 수
$M$이 공백으로 구분되어 주어진다. (
$2 \leq N \leq 200\,000$,
$1 \leq M \leq N - 1$)

다음
$M$개의 줄에 친분 관계를 맺고 있는 두 교육생인
$u$,
$v$가 공백으로 구분되어 주어진다. (
$1 \leq u, v \leq N$,
$u \neq v$)

교육생의 번호는
$1$ 이상
$N$ 이하의 정수이며, 주어지는 그래프는 포레스트이다.

출력
첫째 줄에 튜터-튜티 관계를 정하는 경우의 수를
$1\,000\,000\,007$로 나눈 나머지를 출력한다.



-------
9:56~10:24




- 튜터 한 학생이 여러명의 튜티를 둘 수 있다.
- 한 학생이 여러 관계를 맺으면서, 튜터와 튜티가 동시에 될 수도 있다.

포레스트를 연결 된 그룹으로 분리를 해야 한다.


'''


from collections import defaultdict
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MAX_N = 200_000
MOD = 1_000_000_007


def solve(graph:defaultdict, N:int):
    '''
    '''
    node_info = [ -1 for x in range(N+1) ]
    # node_info[k] 는 노드-k 가 어느 그룹에 속했는지를 식별.

    def mark_group(start:int, id:int):
        # start 노드 부터 시작하여 연결된 그룹에 그룹 식별자 id 를 할당.
        # node_info 이 visited 의 역할을 수행할 수 있음.
        num = 0
        if node_info[start] >= 0: # already marked
            return num
        node_info[start] = id
        num += 1
        stack = [ start ]
        while stack:
            cur = stack.pop()
            if cur not in graph: continue;
            for nxt in graph[cur]:
                if node_info[nxt] >= 0: continue # already visited
                node_info[nxt] = id
                num += 1
                stack.append(nxt)
        return num

    group_info = []
    # 그룹 정보 저장. (id, any_node_in_group)
    #  id 는 0 부터 증가하는 숫자.

    # 연결 관계가 하나도 없는 노드가 있을 수 있는지는 문제에서 명확하지 않음.
    # nodes = graph.keys()
    nodes = range(1, N+1) # 단독 노드도 고려하려면 모든 노드에 대해서 검사 필요.
    for n in nodes:
        if node_info[n] >= 0: continue
        # 노드 n 부터 시작하여, 연결된 모든 노드를 하나의 그룹으로 묶는다.
        num_nodes = mark_group(n, len(group_info))
        group_info.append((num_nodes, n))

    # log("%d groups, %s", len(group_info), [t[0] for t in group_info])

    # 각 그룹에서는 임의의 하나의 노드만 선택하면 됨.
    cases = 1
    for g in group_info:
        cases = (cases * g[0]) % MOD
    return cases


N,M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(solve(graph, N))



'''
예제 입력 1
3 2
1 2
2 3
예제 출력 1
3

run=(python3 24542.py)

echo '3 2\n1 2\n2 3' | $run
-> 3

예제 입력 2
6 4
1 2
3 1
4 5
4 6
예제 출력 2
9

echo '6 4\n1 2\n3 1\n4 5\n4 6' | $run
-> 9




export _N=200000
export _N=10
run=(python3 24542.py)

(python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
N = int(os.getenv('_N','10'))
graph=[]
for k in range(1,N+1,3): # 1,4,7,10
    if k+1 <= N: graph.append((k,k+1))
    if k+2 <= N: graph.append((k+1,k+2))
print(N,len(graph))
for s,e in graph:
    print(s,e)
EOF
) | time $run

_N=200000 인 경우
-> 703236849
$run  0.17s user 0.01s system 81% cpu 0.223 total

'''

