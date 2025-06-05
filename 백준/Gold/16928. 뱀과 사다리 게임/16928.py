'''
16928번

뱀과 사다리 게임 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	55480	20725	15873	34.561%

문제
뱀과 사다리 게임을 즐겨 하는 큐브러버는 어느 날 궁금한 점이 생겼다.

주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착할 수 있을까?

게임은 정육면체 주사위를 사용하며, 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다.
게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행된다.
보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있다.

플레이어는 주사위를 굴려 나온 수만큼 이동해야 한다.
예를 들어, 플레이어가 i번 칸에 있고, 주사위를 굴려 나온 수가 4라면, i+4번 칸으로 이동해야 한다.
만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없다.
도착한 칸이 사다리면, 사다리를 타고 위로 올라간다. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 된다.
즉, 사다리를 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 크고, 뱀을 이용해 이동한 칸의 번호는 원래 있던 칸의 번호보다 작아진다.

게임의 목표는 1번 칸에서 시작해서 100번 칸에 도착하는 것이다.

게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자.

입력
첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)이 주어진다.

둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)가 주어진다.
x번 칸에 도착하면, y번 칸으로 이동한다는 의미이다.

다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)가 주어진다.
u번 칸에 도착하면, v번 칸으로 이동한다는 의미이다.

1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아니다.
모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다.
항상 100번 칸에 도착할 수 있는 입력만 주어진다.

출력
100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력한다.

-------

9:42~10:08 코딩

'''


from collections import deque
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


NODES = 100 # number of nodes
START,END = 1,100


def solve(path:list)->int:
    # path: quick path list, via ladder or snake
    #
    graph = [[] for i in range(NODES+1)]
    # graph[0] is not used.
    for n in range(1,NODES+1):
        graph[n] = [ k for k in range(n+1,min(n+7,NODES+1)) ]

    # use bfs
    que = deque()
    stat = [ -1 for i in range(NODES+1) ]
    #   stat[k]: 노드 k 까지 이동하는데 걸린 횟수 (주사위 굴린 횟수)
    #            <0 if not visited

    que.append(START)
    stat[START] = 0

    while que:
        # log('que: %s', que)

        node = que.popleft()
        count = stat[node]
        # log('(%d) node %d', count, node)

        if node == END:
            # log('reached to end, with count %d', count)
            return count

        for nxt in graph[node]:
            # nxt is next node using dice. usually node+1 ~ +6
            # assume nxt is in valid range. 1<=nxt<=NODES

            if path[nxt] > 0:
                # log('  using path: %d -> %d', nxt, path[nxt])
                nxt = path[nxt]
            if stat[nxt] >= 0: continue

            que.append(nxt)
            stat[nxt] = count+1

    return -1



N,M = map(int, input().split())

path = [0 for i in range(NODES+1)]
# path[0] is not used.

for _ in range(N): # ladder
    s,e = map(int, input().split())
    assert s<e and 1<=s<=NODES and 1<=e<=NODES
    path[s] = e
for _ in range(M): # snake
    s,e = map(int, input().split())
    assert s>e and 1<=s<=NODES and 1<=e<=NODES
    path[s] = e

print(solve(path))



'''
예제 입력 1
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17
예제 출력 1
3

5를 굴려 6으로 이동한다.
6을 굴려 12로 이동한다. 이 곳은 98로 이동하는 사다리가 있기 때문에, 98로 이동한다.
2를 굴려 100으로 이동한다.

예제 입력 2
4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
예제 출력 2
5



run=(python3 16928.py)

1 0
2 99
-> 2

echo '1 0\n2 99' | $run
-> 2

1 0
7 94
-> 2

0 0
-> 17
# 99/6 = 16.5


'''

