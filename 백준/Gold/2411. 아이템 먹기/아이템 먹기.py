import sys

def get_input():
    input = sys.stdin.readline
    N,M,A,B = map(int, input().split())
    As,Bs = [],[]  # items, blocks
    for _ in range(A): # items, >= 1
        As.append(tuple(map(int, input().split())))
    for _ in range(B): # blocks, >= 0
        Bs.append(tuple(map(int, input().split())))
    return N,M,As,Bs

def solve(N:int, M:int, items:list[tuple[int,int]], blks:list[tuple[int,int]])->int:
    '''
    Returns: number of available paths
    '''

    def get_num_paths(y1:int, x1:int, y2:int, x2:int)->int:
        '''
        item (y1,x1) 과 item (y2,x2) 를 양 끝단으로 하는 부분 영역에서의 경로 개수를 구한다.
        '''
        #assert y1 <= y2 and x1 <= x2
        if not (y1 <= y2 and x1 <= x2):
            return 0

        # (y1,x1)을 (1,1)로 하는 좌표로 변환한다.
        # 목적지인 (y2,x2)는 (H,W)로 부르자.
        # (0,0)을 비워두는 이유는 아래 dp 루프에서의 계산 편의를 위해서임.
        H,W = y2-y1+1,x2-x1+1
        # 이제 (1,1)에서 (H,W)로 가는 경로 수 구하는 문제로 간략화 되었음

        # 현재 관심있는 영역 안에 있는 장애물 만 추출.
        # blks = [ (y-y1+1,x-x1+1) for y,x in blks if y1<=y<=y2 and x1<=x<=x2 ]
        # 블럭의 개수가 최대 1만개 인데, in 연산자의 느린 속도를 고려하면 리스트가 아닌 다른 방식으로 구현해야 할 것 같음.
        # -> 2d list 로..
        blkmap = [ [0]*(W+1) for _ in range(H+1) ]
        for y,x in blks:
            if y1<=y<=y2 and x1<=x<=x2:
                blkmap[y-y1+1][x-x1+1] = 1

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
        pos = (y, x)
    return num_path

if __name__ == '__main__':
    print(solve(*get_input()))
