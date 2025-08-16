'''
좀 더 개선한 버전.

1.
    map1 -> grid 로 변환 불필요. 그냥 map1 그대로 사용.
    어차피 grid[y][x] 가 1 인 것을 0 으로 변경하지 않고 탐색을 계속 진행하기 때문.
2.
    heapq 로 순서를 조정하게 하는 대신, 0-1 bfs 를 명시적으로 사용.
    즉, deque 의 앞에 추가하는 방법 사용



'''


import sys
from collections import deque

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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
        # log("(%d,%d) jumps %d", y, x, jumps)

        for dy,dx in deltas:
            ny,nx = y+dy,x+dx
            if not (0<=ny<N and 0<=nx<M): continue # out-of-bound
            if jumpmap[ny][nx]: continue # already visited
            if grid[ny][nx] == '#': return jumps # reached to target
            if grid[ny][nx] == '1':
                que.append((ny,nx))
                jumpmap[ny][nx] = jumps+1
                # log("  (%d,%d) jumps -> %d", ny,nx, jumps+1)
            else:
                que.appendleft((ny,nx))
                jumpmap[ny][nx] = jumps
    # did not meet target. it should not happen
    return -1


if __name__ == '__main__':
    inp = get_input()
    r = solve_01bfs(*inp)
    print(r)




'''
전체 예제는 14497b.py 참고.


run=(python3 14497a.py)

echo '5 7\n3 4 1 2\n1#10111\n1101001\n001*111\n1101111\n0011001' | $run
# -> 3

echo '3 5\n3 5 1 1\n#0000\n11111\n0000*' | $run
# -> 2

echo '3 3\n2 2 1 1\n#00\n0*0\n000' | $run
# -> 1



'''

