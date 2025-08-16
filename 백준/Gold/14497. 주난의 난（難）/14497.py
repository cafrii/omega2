'''
14497번
주난의 난(難) 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	6641	3503	2245	52.355%

문제
주난이는 크게 화가 났다. 책상 서랍 안에 몰래 먹으려고 숨겨둔 초코바가 사라졌기 때문이다.
주난이는 미쳐 날뛰기 시작했다. 사실, 진짜로 뛰기 시작했다.

‘쿵... 쿵...’

주난이는 점프의 파동으로 주변의 모든 친구들을 쓰러뜨리고(?) 누군가 훔쳐간 초코바를 찾으려고 한다.
주난이는 N×M크기의 학교 교실 어딘가에서 뛰기 시작했다.
주난이의 파동은 상하좌우 4방향으로 친구들을 쓰러뜨릴(?) 때 까지 계속해서 퍼져나간다.
다르게 표현해서, 한 번의 점프는 한 겹의 친구들을 쓰러뜨린다. 다음의 예를 보자.

1 # 1 0 1 1 1
1 1 0 1 0 0 1
0 0 1 * 1 1 1
1 1 0 1 1 1 1
0 0 1 1 0 0 1

주난이를 뜻하는 *은 (3, 4)에 있고, 초코바를 가진 학생 #는 (1, 2)에 있다.
0은 장애물이 없는 빈 공간임을 뜻하고, 1은 친구들이 서있음을 의미한다.
다음은 주난이의 점프에 따른 생존(?) 학생들의 변화이다.

1 # 1 0 1 1 1
1 1 0 0 0 0 1
0 0 0 * 0 1 1
1 1 0 0 1 1 1
0 0 1 1 0 0 1

1 # 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 * 0 0 1
0 0 0 0 0 1 1
0 0 0 0 0 0 1

0 X 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 * 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0

위의 예시에서 주난이는 3번의 점프 만에 초코바를 훔쳐간 범인을 찾아낼 수 있다!

주난이를 빨리 멈춰야 교실의 안녕을 도모할 수 있다. 주난이에게 최소 점프 횟수를 알려줘서 교실을 지키자.

입력
첫째 줄에 주난이가 위치한 교실의 크기 N, M이 주어진다. (1 ≤ N, M ≤ 300)

둘째 줄에 주난이의 위치 x1, y1과 범인의 위치 x2, y2가 주어진다.
(1 ≤ x1, x2 ≤ N, 1 ≤ y1, y2 ≤ M)

이후 N×M 크기의 교실 정보가 주어진다. 0은 빈 공간, 1은 친구, *는 주난, #는 범인을 뜻한다.

출력
주난이가 범인을 잡기 위해 최소 몇 번의 점프를 해야 하는지 출력한다.


-----

알고리즘 개선 버전. 원본은 14497b.py 참고.

start 점으로부터의 위치적인 거리 보다
step (stage)를 더 우선하여 정렬

heapq 를 사용 (stage, dist, y, x)
나중엔 dist 도 제거했음. 오직 stage 만..

더 개선된 버전은 14497a.py 참고.

------

97535239 cafrii    14497 맞았습니다!! 34984KB 108ms Python 3 1529B  <- 14497a.py, best
97534301 cafrii    14497 맞았습니다!! 35904KB 168ms Python 3 1944B  <- 14497.py

97152309 dbsqja353 14497 맞았습니다!! 35016KB 144ms Python 3 1098B
95939600 sik1015   14497 맞았습니다!! 34984KB 124ms Python 3  982B
93096286 s_s_w     14497 맞았습니다!! 34984KB 116ms Python 3 1089B


'''


import sys
# from collections import deque
from heapq import heappush, heappop


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
        sy, sx: start location (zero-base)
    Returns:
        number of jumps to reach to target
    '''
    N,M = len(map1),len(map1[0])
    # grid = [ [ 0 for x in range(M) ] for y in range(N) ]

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

        # log("search from (%d,%d)", sy, sx)
        heappush(que, (jumps, sy,sx))
        visited[sy][sx] = 1

        while que:
            jumps,y,x = heappop(que)
            # log("(%d,%d) jumps %d", y, x, jumps)
            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<M): continue
                if visited[ny][nx]: continue

                if grid[ny][nx] == 9:
                    # log("got to target at jumps %d", jumps)
                    return jumps
                if grid[ny][nx] == 1:
                    # grid[ny][nx] = 0
                    visited[ny][nx] = 1
                    heappush(que, (jumps+1,ny,nx))
                    # log("  (%d,%d) jumps -> %d", ny,nx, jumps+1)
                else:
                    heappush(que, (jumps,ny,nx))
                    visited[ny][nx] = 1
        # did not meet target
        return -1

    return search(sy, sx)


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
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

