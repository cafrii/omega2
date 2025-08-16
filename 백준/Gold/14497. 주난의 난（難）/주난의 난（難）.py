
import sys
from heapq import heappush, heappop

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())  # y, x
    y1,x1,y2,x2 = map(int, input().split())
    map1 = []
    for _ in range(N):
        map1.append(input().rstrip())
        assert len(map1[-1]) == M, "wrong width"
    y1,x1 = y1-1,x1-1
    assert map1[y1][x1] == '*', "wrong *"
    y2,x2 = y2-1,x2-1
    assert map1[y2][x2] == '#', "wrong #"
    return map1,y1,x1

def solve(map1:list[str], sy:int, sx:int)->int:
    '''
    Args:
        map:
        sy, sx: start location (zero-base)
    Returns:
        number of jumps to reach to target
    '''
    N,M = len(map1),len(map1[0])

    # convert map to mutable 2d grid
    map2grid = lambda s: 9 if s=='#' else 1 if s=='1' else 0
    grid = [ [ map2grid(map1[y][x]) for x in range(M) ] for y in range(N) ]

    deltas = [ (1,0),(-1,0),(0,1),(0,-1) ]

    def search(sy:int, sx:int)->int:
        '''
        Args:
            (sy,sx): start location
        Returns:
            number of jumps required to reach target
        '''
        jumps = 1
        visited = [ [0]*M for _ in range(N) ]
        que = [] # heap que

        heappush(que, (jumps, sy,sx))
        visited[sy][sx] = 1

        while que:
            jumps,y,x = heappop(que)
            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<M): continue
                if visited[ny][nx]: continue
                if grid[ny][nx] == 9: # target
                    return jumps
                if grid[ny][nx] == 1:
                    visited[ny][nx] = 1
                    heappush(que, (jumps+1,ny,nx))
                else:
                    heappush(que, (jumps,ny,nx))
                    visited[ny][nx] = 1
        # did not meet target
        return jumps

    return search(sy, sx)

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
