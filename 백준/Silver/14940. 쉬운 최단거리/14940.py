'''
14940
쉬운 최단거리 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	44191	17745	14287	37.753%

문제
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다. (2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다.
입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다.
원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

'''


import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

map1 = []
goal = None
for y in range(N):
    map1.append(list(map(int, input().split())))



def solve():
    '''
    Globals:
        map1, N, M
    Returns: visited
    '''

    goal = None  # find goal
    for y,m in enumerate(map1):
        try: goal = (y, m.index(2))
        except: pass
    assert goal is not None
    # print(f'goal: {goal}')

    visited = [[-1 for x in range(M)] for y in range(N)]
    # -1: not visited (or cannot reach)
    #  0: goal or wall
    # >0: distance

    # mark wall
    for y in range(N):
        for x in range(M):
            if map1[y][x] == 0:
                visited[y][x] = 0

    que = deque()

    que.append(goal)
    visited[goal[0]][goal[1]] = 0

    delta = [(1,0), (0,1), (-1,0), (0,-1)]

    while que:
        y,x = que.popleft()
        dist = visited[y][x]

        for dy,dx in delta:
            ny,nx = y+dy,x+dx
            if not (0<=ny<N and 0<=nx<M): # boundness check
                continue
            # check if it is wall
            if map1[y][x] == 0: # it is wall. cannot move.
                continue
            # check it is already visited
            if visited[ny][nx] >= 0:
                continue
            que.append((ny,nx))
            visited[ny][nx] = dist+1

    return visited

ans = solve()
for a in ans:
    print(*a)


'''
예제 입력 1
15 15
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
예제 출력 1
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
11 12 13 14 15 16 17 18 19 20 0 0 0 0 25
12 13 14 15 16 17 18 19 20 21 0 29 28 27 26
13 14 15 16 17 18 19 20 21 22 0 30 0 0 0
14 15 16 17 18 19 20 21 22 23 0 31 32 33 34


echo '1 3\n2 1 1' | python3 14940.py
-> 0 1 2

echo '1 3\n1 1 2' | python3 14940.py
-> 2 1 0

echo '1 3\n1 2 0' | python3 14940.py
-> 1 0 0

echo '1 7\n2 1 1 1 0 1 1' | python3 14940.py
-> 0 1 2 3 0 -1 -1

1 1 1 1 1
1 0 1 0 1
2 0 1 1 1

echo '3 5\n1 1 1 1 1\n1 0 1 0 1\n2 0 1 1 1' | python3 14940.py
2 3 4 5 6
1 0 5 0 7
0 0 6 7 8


1 1 0 1 1
1 0 1 0 1
2 1 1 1 0

echo '3 5\n1 1 0 1 1\n1 0 1 0 1\n2 1 1 1 0' | python3 14940.py
2 3 0 -1 -1
1 0 3 0 -1
0 1 2 3 0


'''


