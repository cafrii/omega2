'''
2606번



바이러스 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	208133	99106	65456	46.193%

문제

신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
'''


import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)



def solve(graph:list[list]):
    # note: graph has size of (number of node + 1)
    #       graph[0] is not used.

    # use DFS, from node 1
    stack = [ 1 ]
    visited = [ 0 ] * (len(graph) + 1)
    num_visited = 0

    while stack:
        log('stack: %s', stack)
        v = stack.pop()
        visited[v] = 1
        num_visited += 1

        # next
        stack.extend([ x for x in graph[v] if x not in stack and visited[x] == 0 ])
        log('node %d, visited %s', v, [ i for i,x in enumerate(visited) if x==1 ] )

    return num_visited - 1 # do not count 1 itself.



N = int(input().strip())
graph = [ [] for x in range(N+1) ]
# node 0 (graph[0]) will not be used.

num_links = int(input().strip())

for _ in range(num_links):
    s,e = map(int, input().split())
    graph[s].append(e) if e not in graph[s] else None
    graph[e].append(s) if s not in graph[e] else None

log('graph: %s', graph)
print(solve(graph))


'''
예제 입력 1
7
6
1 2
2 3
1 5
5 2
5 6
4 7
예제 출력 1
4


echo '1\n0' | python3 2606.py
1
echo '2\n0' | python3 2606.py
1
echo '2\n1\n1 2' | python3 2606.py
2
echo '4\n2\n1 2\n3 4' | python3 2606.py
2
echo '4\n2\n1 2\n3 2' | python3 2606.py
3


(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,L = 100,1150
print(N); print(L)
get_01 = lambda p_of_1 : ('1' if randint(1, 100) <= p_of_1 else '0')
for _ in range(L):
    use_1 = randint(1, 100) < 50
    if use_1:
        print(1, randint(2, N))
    else:
        a = randint(2, N)
        b = (a + randint(0, N-2)) % N + 1
        print(a, b) # a != b. b != 0, b can be 1, but it's ok in testing.
EOF
) | time python3 2606.py 2> /dev/null

'''