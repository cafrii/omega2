import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split()) # N 이 가로크기
    K = int(input().rstrip())
    Ks = []
    for _ in range(K):
        Ks.append(tuple(map(int, input().split())))
    return N,M,Ks

def solve(W:int, H:int, Ks:list[tuple[int,int,int,int]])->int:
    '''
    Args:
        W: width, x 크기, H: height, y 크기
        Ks: [ (x1,y1,x2,y2), ... ]
    Returns:
        number of shortest cases
    Info:
        이 함수에서 사용하는 2-d array 는 [y][x] 순이다.
    '''
    # path availability at each location for specific (x or y) direction
    ok_x = [ [1]*(W+1) for _ in range(H+1) ]
    ok_y = [ [1]*(W+1) for _ in range(H+1) ]
    # ex:
    #  ok_x[y][x] == 1 이면 (y,x-1) 과 (y,x) 사이의 통행이 가능.
    #  ok_y[y][x] == 1 이면 (y-1,x) 과 (y,x) 사이의 통행이 가능.

    for x1,y1,x2,y2 in Ks:
        if y1 == y2: # this is barrier in x direction
            ok_x[y1][max(x1, x2)] = 0
        elif x1 == x2: # in y direction
            ok_y[max(y1, y2)][x1] = 0

    dp = [ [0]*(W+1) for _ in range(H+1) ]
    # dp[y][x]: 좌표 (x,y) 까지 도달하는 경우의 수
    # 최종 정답은 dp[H][W]
    dp[0][0] = 1

    for y in range(0, H+1):
        for x in range(0, W+1):
            if x==0 and y==0: continue
            if x>0 and ok_x[y][x]:
                dp[y][x] += dp[y][x-1]
            if y>0 and ok_y[y][x]:
                dp[y][x] += dp[y-1][x]

    return dp[H][W]

if __name__ == '__main__':
    print(solve(*get_input()))
