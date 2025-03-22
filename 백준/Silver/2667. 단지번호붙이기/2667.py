'''
2667번

단지번호붙이기

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	211546	96320	61116	43.328%

문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

'''

import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)


def solve(N:int, graph:list[list]):

    visited = [ 0 for k in range(N*N) ]
    groups = { } # key:group_id, value:number of houses in this group

    def new_group(start:int):
        # find new house group, starting from location 'start'.
        #
        houses = [] # house list.
        # we will track which houses are belonged to this house group

        stack = [ start ]
        in_stack = [ 0 for k in range(N*N) ] # for quick search in stack
        while stack:
            log('    stack: %s', stack)
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = 1
            houses.append(u)

            # next houses..
            # stack.extend([ x for x in graph[u] if not visited[x] ])
            for x in graph[u]:
                if not visited[x] and not in_stack[x]:
                    stack.append(x)
                    in_stack[x] = 1


        # group id is positive interger. 1, 2, ...
        group_id = len(groups) + 1
        # we just need the number of houses only, not each house list.
        groups[group_id] = len(houses)

        return group_id

    for k in range(N*N):
        if not graph[k]: # no house here
            continue
        if visited[k]:
            continue

        log('finding new group, starting from %d', k)
        gid = new_group(k)
        log(' --> new group %d: %s houses, visited %s', gid, str(groups[gid]), visited)

    result = [ groups[k] for k in groups.keys() ]
    result.sort()
    return result





N = int(input().strip())
A = []
for _ in range(N):
    A.append(input().strip())

# total N**2 nodes, index: 0 ~ N*N-1
graph = [ [] for k in range(N*N) ]

# convert input string to graph
for y in range(N):
    for x in range(N):
        k = y*N + x
        if A[y][x] == '0':
            continue
        graph[k].append(k) # itself

        for (dy,dx) in [ (-1,0), (1,0), (0,-1), (0,1) ]:
            k2 = k + dy*N + dx  # == (y+dy)*N + (x+dx)
            if 0 <= y+dy < N and 0 <= x+dx < N and \
                    A[y+dy][x+dx] == '1' and \
                    k2 not in graph[k]:
                graph[k].append(k2)
        # # check left
        # if x > 0 and A[y][x-1] == '1' and (k-1) not in graph[k]:
        #     graph[k].append(k-1)
        # # check right
        # if x < N-1 and A[y][x+1] == '1' and (k+1) not in graph[k]:
        #     graph[k].append(k+1)
        # # check up
        # if y > 0 and A[y-1][x] == '1' and (k-N) not in graph[k]:
        #     graph[k].append(k-N)
        # # check down
        # if y < N-1 and A[y+1][x] == '1' and (k+N) not in graph[k]:
        #     graph[k].append(k+N)
        if graph[k]:
            graph[k].sort()

log('\n'.join(A))
log('graph: %s', str(graph))

result = solve(N, graph)
print(len(result))
for x in result:
    print(x)


'''
예제 입력 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

예제 출력 1
3
7
8
9


echo '2\n01\n10' | python3 2667.py
2
1
1
echo '2\n01\n01' | python3 2667.py
1
2
echo '3\n000\n000\n000' | python3 2667.py
0
echo '3\n000\n000\n001' | python3 2667.py
1
1
echo '3\n110\n101\n001' | python3 2667.py
2
3



(python3 <<EOF
import time
from random import seed,randint
seed(123) #seed(time.time())
N = 25
print(N)
get_01 = lambda p_of_1 : ('1' if randint(1, 100) <= p_of_1 else '0')
for _ in range(N):
    a = [ get_01(60) for _ in range(N) ]
    if _ == 0: a[0] = '1'
    if _ == N-1: a[-1] = '1'
    print(''.join(a))
EOF
) | time python3 2667.py 2> /dev/null

'''

