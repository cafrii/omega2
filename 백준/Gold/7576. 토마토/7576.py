'''
7576번

토마토 성공

- 유사문제: 7569

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	219474	88958	56600	37.887%

문제

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

입력
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다.
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다.
둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

토마토가 하나 이상 있는 경우만 입력으로 주어진다.

출력
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

-------

9:50~10:38

'''


from collections import deque
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def showbox(box, indent='', title=''):
    if title: log("%s", title)
    for row in box:
        log("%s%s", indent, ' '.join([ (str(e) if e>=0 else '.') for e in row ]))


MAX_DAYS = 1000*1000

# box status
#  1: 익은 토마토
#  0: 익지 않은 토마토
#  -1: 토마토 없음


def solve(box:list[list])->int:
    # returns
    #   토마토가 모두 익을 때 까지의 최소 날짜
    #   0: 저장될 때부터 모든 토마토가 익어있는 상태
    #   -1: 토마토가 모두 익지는 못하는 상황
    N,M = len(box), len(box[0])

    visited = [ [ -1 for c in range(M) ] for r in range(N) ]
    # days when the tomato in the cell is matured
    # -1 if not visited

    que = deque()
    # element: tuple (row, col)

    # 시작 상태의 모든 익은 토마토를 큐에 넣기
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                que.append((r,c))
                visited[r][c] = 0 # matured at day 0

    # showbox(visited, '  ', f'day{0}')

    deltas = [(-1,0), (1,0), (0,-1), (0,1)]
    d = -1
    while que:
        y,x = que.popleft()
        if visited[y][x] != d:
            showbox(visited, '  ', f'day{visited[y][x]}')
        d = visited[y][x]

        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            if not (0<=ny<N and 0<=nx<M):
                continue
            if visited[ny][nx] >= 0: # already matured
                continue
            if box[ny][nx] == -1: # no tomato here
                continue

            que.append((ny,nx))
            visited[ny][nx] = d+1

    showbox(visited, '  ', 'final')

    # box[][] 가 0 이면서 visited 못한 cell 이 있다면 not-finish!
    if sum(1 if (box[y][x] == 0 and visited[y][x] < 0) else 0
            for y in range(N) for x in range(M)):
        return -1

    return max(max(r) for r in visited)




M,N = map(int, input().split())
# N rows, M columns

box = [] # [ [0]*M for _ in range(N) ]
for _ in range(N):
    box.append(list(map(int, input().split())))
    assert len(box[-1]) == M

showbox(box, '  ', 'box')

print(solve(box))


'''
예제 입력 1
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
예제 출력 1
8
echo '6 4\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 0\n0 0 0 0 0 1' | python3 7576.py


예제 입력 2
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
예제 출력 2
-1


예제 입력 3
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
예제 출력 3
6

예제 입력 4
5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
예제 출력 4
14

예제 입력 5
2 2
1 -1
-1 1
예제 출력 5
0

echo '2 2\n1 -1\n-1 1' | python3 7576.py

'''

