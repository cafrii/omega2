'''
2411번
아이템 먹기 성공 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	1432	611	481	44.911%

문제
NxM 모양의 맵에 아이템과 장애물이 있다.
이때 맵의 왼쪽 아래에서 출발하여 오른쪽 위로 가려고 하는데, 중간에 모든 아이템을 먹으려고 한다.
이동할 때에는 오른쪽이나 위쪽으로만 이동할 수 있다. 또, 장애물이 있는 곳으로는 지날 수 없다.

이때, 이동하는 경로의 개수가 총 몇 개인지 알아내는 프로그램을 작성하시오.
위의 예에서 ◎은 장애물, ☆는 아이템이다. 이때 경우의 수는 4 가지가 된다.

입력
첫째 줄에 N, M(1 ≤ N, M ≤ 100), A(1 ≤ A), B(0 ≤ B)가 주어진다.
A는 아이템의 개수이고, B는 장애물의 개수이다.
다음 A개의 줄에는 아이템의 위치, B개의 줄에는 장애물의 위치가 주어진다.
위치를 나타낼 때에는 왼쪽 아래가 (1, 1)이 되고 오른쪽 위가 (N, M)이 된다.

출력
첫째 줄에 경우의 수를 출력한다. 이 값은 int 범위이다.

----

문제에서 주어진 그림과 다르게 해석함. (y, x) 순서로 좌표를 해석. 바뀌어도 상관 없음.

----
구현, 제출, 검증 완료.


'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    input = sys.stdin.readline
    N,M,A,B = map(int, input().split())
    As,Bs = [],[]  # items, blocks
    for _ in range(A): # items, >= 1
        As.append(tuple(map(int, input().split())))
    for _ in range(B): # blocks, >= 0
        Bs.append(tuple(map(int, input().split())))
    return N,M,As,Bs

def map2str(items:list[tuple[int,int]], blks:list[tuple[int,int]]=[], dim=None, offset=(0,0), indent:str='')->str:
    # for debugging purpose
    H,W = 0,0
    if dim is None:
        ys,xs = list(zip(*items))
        H,W = max(ys),max(xs)
    else: # dim is tuple[int,int]
        H,W = dim
    grid = [ [0]*W for _ in range(H) ]

    for y,x in items: grid[y][x] = 1
    for y,x in blks: grid[y][x] = 2

    icon = ['.', 'O', 'X']
    oy,ox = offset
    return '\n'.join(
        indent + ''.join(icon[e] for e in ln[ox:]) for ln in grid[oy:]
    )

def map2str2d(grid:list[list[int]], icon:list[str]=['.','X'], offset=(0,0), indent:str='  ')->str:
    # for debugging purpose
    oy,ox = offset
    return '\n'.join(
        indent + ''.join(icon[e] for e in ln[ox:])
        for ln in grid[oy:]
    )


def solve(N:int, M:int, items:list[tuple[int,int]], blks:list[tuple[int,int]])->int:
    '''
    Returns: number of available paths

    '''
    log("map: %dx%d \n%s", N, M, map2str(items, blks, dim=(N+1,M+1), offset=(1,1), indent=' '*4))

    def get_num_paths(y1:int, x1:int, y2:int, x2:int)->int:
        '''
        item (y1,x1) 과 item (y2,x2) 를 양 끝단으로 하는 부분 영역에서의 경로 개수를 구한다.
        '''
        assert y1 <= y2 and x1 <= x2
        if not (y1 <= y2 and x1 <= x2):
            return 0

        # (y1,x1)을 (1,1)로 하는 좌표로 변환한다.
        # 목적지인 (y2,x2)는 (H,W)로 부르자.
        # (0,0)을 비워두는 이유는 아래 dp 루프에서의 계산 편의를 위해서임.
        H,W = y2-y1+1,x2-x1+1
        # 이제 (1,1)에서 (H,W)로 가는 경로 수 구하는 문제로 간략화 되었음

        log("---- (%d,%d) (%d,%d)  %d x %d", y1, x1, y2, x2, H, W)

        # 현재 관심있는 영역 안에 있는 장애물 만 추출.
        # blks = [ (y-y1+1,x-x1+1) for y,x in blks if y1<=y<=y2 and x1<=x<=x2 ]
        # 블럭의 개수가 최대 1만개 인데, in 연산자의 느린 속도를 고려하면 리스트가 아닌 다른 방식으로 구현해야 할 것 같음.
        # -> 2d list 로..
        blkmap = [ [0]*(W+1) for _ in range(H+1) ]
        for y,x in blks:
            if y1<=y<=y2 and x1<=x<=x2:
                blkmap[y-y1+1][x-x1+1] = 1

        # 제대로 변환 되었는지 로그로 확인
        log("blks: (rel)\n%s", map2str2d(blkmap, ['.','X'], (1,1), ' '*4))

        # dp 테이블의 크기는 (H+1) x (W+1) 이다. (0,0) 부터 (H,W)가 양 끝점.
        dp = [ [0]*(W+1) for _ in range(H+1) ]
        dp[1][1] = 1  # 시작위치

        for y in range(1, H+1):  # y: 1 ~ H
            for x in range(1, W+1): # x: 1 ~ W
                if x==1 and y==1: continue
                if blkmap[y][x]: continue
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

        return dp[H][W]

    items = sorted(items)
    num_path = 1
    pos = (1,1)
    items.append((N,M)) # add final goal

    for y,x in items:
        r = get_num_paths(*pos, y, x)
        num_path *= r
        log("(%d,%d)->(%d,%d): %d paths, total %d", *pos, y, x, r, num_path)
        pos = (y, x)

    return num_path


if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
5 8 4 4
1 2
2 5
3 5
4 7
1 5
2 2
2 7
3 6
예제 출력 1
4

----
run=(python3 a2411.py)

echo '5 8 4 4\n1 2\n2 5\n3 5\n4 7\n1 5\n2 2\n2 7\n3 6' | $run
# 4
#     SO..X...
#     .X..O.X.
#     ....OX..
#     ......O.
#     .......E

echo '2 4 1 0\n1 1' | $run
# 4
#     O...
#     ....

echo '2 4 1 0\n1 2' | $run
# 3
#    .O..
#    ....

echo '2 4 2 0\n1 2\n2 3' | $run
# 2
#     .O..
#     ..O.

echo '4 4 1 2\n2 2\n1 2\n2 1' | $run
# 0
#     .X..
#     XO..
#     ....
#     ....

'''
