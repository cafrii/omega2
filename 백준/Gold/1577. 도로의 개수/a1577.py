'''
1577번
도로의 개수 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	16 MB	5939	1957	1643	35.144%

문제
세준이가 살고 있는 도시는 신기하게 생겼다. 이 도시는 격자형태로 생겼고, 직사각형이다.
도시의 가로 크기는 N이고, 세로 크기는 M이다.
또, 세준이의 집은 (0, 0)에 있고, 세준이의 학교는 (N, M)에 있다.

따라서, 아래 그림과 같이 생겼다.

세준이는 집에서 학교로 가는 길의 경우의 수가 총 몇 개가 있는지 궁금해지기 시작했다.

세준이는 항상 최단거리로만 가기 때문에, 항상 도로를 정확하게 N + M개 거친다.
하지만, 최근 들어 이 도시의 도로가 부실공사 의혹으로 공사중인 곳이 있다.
도로가 공사 중일 때는, 이 도로를 지날 수 없다.

(0, 0)에서 (N, M)까지 가는 서로 다른 경로의 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도로의 가로 크기 N과 세로 크기 M이 주어진다.
N과 M은 100보다 작거나 같은 자연수이고, 둘째 줄에는 공사중인 도로의 개수 K가 주어진다.
K는 0보다 크거나 같고, 50보다 작거나 같은 자연수이다.
셋째 줄부터 K개 줄에는 공사중인 도로의 정보가 a b c d와 같이 주어진다.
a와 c는 0보다 크거나 같고, N보다 작거나 같은 자연수이고,
b와 d는 0보다 크거나 같고, M보다 작거나 같은 자연수이다.
그리고, (a, b)와 (c, d)의 거리는 항상 1이다.

출력
첫째 줄에 (0, 0)에서 (N, M)까지 가는 경우의 수를 출력한다.
이 값은 0보다 크거나 같고, 263-1보다 작거나 같은 자연수이다.

----

9:15~10:00
----
평범한 2차원 dp로 구현. 검증 완료

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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
    # log("dp: %dx%d, Ks: %s", H, W, Ks)

    # path availability at each location for specific (x or y) direction
    ok_x = [ [1]*(W+1) for _ in range(H+1) ]
    ok_y = [ [1]*(W+1) for _ in range(H+1) ]
    # ex:
    #  ok_x[y][x] == 1 이면 (y,x-1) 과 (y,x) 사이의 통행이 가능.
    #  ok_y[y][x] == 1 이면 (y-1,x) 과 (y,x) 사이의 통행이 가능.

    def grid2str(G:list[list[int]], indent:str = '  '):
        return '\n'.join( indent + ' '.join(map(str, gl)) for gl in G )


    for x1,y1,x2,y2 in Ks:
        if y1 == y2: # this is barrier in x direction
            ok_x[y1][max(x1, x2)] = 0
        elif x1 == x2: # in y direction
            ok_y[max(y1, y2)][x1] = 0

    # log("ok x:\n%s", grid2str(ok_x))
    # log("ok y:\n%s", grid2str(ok_y))

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



'''
예제 입력 1
6 6
2
0 0 0 1
6 6 5 6
예제 출력 1
252

예제 입력 2
1 1
0
예제 출력 2
2

예제 입력 3
35 31
0
예제 출력 3
6406484391866534976

예제 입력 4
2 2
3
0 0 1 0
1 2 2 2
1 1 2 1
예제 출력 4
0

----
run=(python3 a1577.py)

echo '6 6\n2\n0 0 0 1\n6 6 5 6' | $run
# 252
echo '1 1\n0' | $run
# 2
echo '35 31\n0' | $run
# 6406484391866534976
echo '2 2\n3\n0 0 1 0\n1 2 2 2\n1 1 2 1' | $run
# 0
echo '4 4\n4\n1 1 2 1\n2 1 3 1\n2 2 2 3\n1 3 2 3' | $run
# 22


'''


