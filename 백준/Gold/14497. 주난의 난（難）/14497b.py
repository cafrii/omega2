'''

최초 구현. 제출하진 않았지만, 제출했어도 timeout fail 되었을 가능성 큼.


4:09~4:55

-------
개선 방향.

일단 bfs 를 여러번 반복 수행하는 방식으로 구현.
예시는 모두 pass. 하지만 이게 최적은 아님을 금방 알게 됨.

매번 동일한 위치에서 wave 시작하면, 시작부 위치는 여러 번 중복 계산을 반복하게 된다.
그냥 한번에 쭈욱 끝까지 가는 계산법이 필요.

-> 14497.py

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
        sy, sx: start location
    Returns:
        number of jumps to reach to target
    '''
    N,M = len(map1),len(map1[0])
    # grid = [ [ 0 for x in range(M) ] for y in range(N) ]

    # convert map to mutable 2d grid
    map2grid = lambda s: 9 if s=='#' else 1 if s=='1' else 0
    grid = [ [ map2grid(map1[y][x]) for x in range(M) ] for y in range(N) ]

    deltas = [ (1,0),(-1,0),(0,1),(0,-1) ]

    def wave(stage:int, sy:int, sx:int):
        '''
        Args:
            stage: for debugging
            (sy,sx): start location
        '''
        visited = [ [0]*M for _ in range(N) ]
        que = deque()
        que.append((sy,sx))
        visited[sy][sx] = 1

        while que:
            y,x = que.popleft()
            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<M): continue
                if visited[ny][nx]: continue

                if grid[ny][nx] == 9:
                    # log("reached to target")
                    return True
                elif grid[ny][nx] == 1:
                    grid[ny][nx] = 0
                    visited[ny][nx] = 1
                    continue
                que.append((ny,nx))
                visited[ny][nx] = 1
        # did not meet target
        return False

    for i in range(1,N*M+1):
        if wave(i, sy, sx):
            return i
    return 0 # failed

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)


'''
예제 입력 1
5 7
3 4 1 2
1#10111
1101001
001*111
1101111
0011001
예제 출력 1
3

예제 입력 2
3 5
3 5 1 1
#0000
11111
0000*
예제 출력 2
2

예제 입력 3
3 3
2 2 1 1
#00
0*0
000
예제 출력 3
1



run=(python3 14497b.py)

echo '5 7\n3 4 1 2\n1#10111\n1101001\n001*111\n1101111\n0011001' | $run
# -> 3

echo '3 5\n3 5 1 1\n#0000\n11111\n0000*' | $run
# -> 2

echo '3 3\n2 2 1 1\n#00\n0*0\n000' | $run
# -> 1



'''

