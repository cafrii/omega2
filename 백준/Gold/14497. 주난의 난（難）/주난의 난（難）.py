
import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())  # y, x
    y1,x1,y2,x2 = map(int, input().split())
    map1 = []
    for _ in range(N):
        map1.append(input().rstrip())
        # assert len(map1[-1]) == M, "wrong width"
    y1,x1 = y1-1,x1-1
    # assert map1[y1][x1] == '*', "wrong *"
    y2,x2 = y2-1,x2-1
    # assert map1[y2][x2] == '#', "wrong #"
    return map1,y1,x1

def solve_01bfs(grid:list[str], sy:int, sx:int)->int:
    '''
    Args:
        map:
        sy, sx: start location (zero-base)
    Returns:
        number of jumps to reach to target
    '''
    N,M = len(grid),len(grid[0])

    que = deque()
    jumpmap = [ [0]*M for _ in range(N) ]

    que.append((sy,sx))
    jumpmap[sy][sx] = 1

    deltas = [ (0,1),(0,-1),(1,0),(-1,0) ]
    while que:
        y,x = que.popleft()
        jumps = jumpmap[y][x]

        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            if not (0<=ny<N and 0<=nx<M): continue # out-of-bound
            if jumpmap[ny][nx]: continue # already visited
            if grid[ny][nx] == '#': return jumps # reached to target
            if grid[ny][nx] == '1':
                que.append((ny,nx))
                jumpmap[ny][nx] = jumps+1
            else:
                que.appendleft((ny,nx))
                jumpmap[ny][nx] = jumps
    # did not meet target. it should not happen
    return -1

if __name__ == '__main__':
    inp = get_input()
    r = solve_01bfs(*inp)
    print(r)
