'''
17144번
미세먼지 안녕! 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	47081	26636	18207	55.594%

문제
미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다.
공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다.
구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다.
(r, c)는 r행 c열을 의미한다.

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다.
공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
- (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
- 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
- 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
- (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.

2. 공기청정기가 작동한다.
- 공기청정기에서는 바람이 나온다.
- 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
- 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
- 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

다음은 확산의 예시이다.

왼쪽과 위쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.

인접한 네 방향으로 모두 확산이 일어난다.

공기청정기가 있는 칸으로는 확산이 일어나지 않는다.

공기청정기의 바람은 다음과 같은 방향으로 순환한다.

방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

입력
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.

둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다.
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
-1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

출력
첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.


------

1:44~2:03 일시 중단
2:53~3:27, 일시 중단
5:33~7:51


'''


import sys
input = sys.stdin.readline

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def mapstr(A:list[list[int]], indent='', fmt='%2d ')->str:
    lines = []
    for line in A:
        lines.append(indent + ''.join(
            [ (fmt % e) for e in line ]
        ))
    return '\n'.join(lines)

def solve(A:list[list[int]], aircon:list[int], T:int):
    '''
    '''
    R,C = len(A),len(A[0])

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    aircon_loc = [(aircon[0],0),(aircon[1],0)]

    def diffuse():
        # this function will replace object A
        nonlocal A
        B = [[0]*C for r in range(R)]

        # for all dust in A..
        for r in range(R):
            for c in range(C):
                dust = A[r][c]
                if dust==0: continue # empty
                if dust<0: continue # aircon
                part = dust // 5
                if part == 0:
                    B[r][c] += dust # no diffuse
                    continue
                for dr,dc in neighbors: # delta r/c
                    nr,nc = r+dr,c+dc   # next r/c
                    if not (0<=nr<R and 0<=nc<C): # exceed bound
                        continue
                    if (nr,nc) in aircon_loc: # aircon
                        continue
                    B[nr][nc] += part
                    dust -= part
                B[r][c] += dust
        A = B  # keep B as A
        pass

    def circulate():
        # aircon 위치를 기준으로 두 개의 flow 적용.
        # 1. top flow
        ac = aircon[0]
        # 1-1. downward
        for r in range(ac-2, -1, -1):  # AC-2 ~ 0
            A[r+1][0] = A[r][0]
        # 1-2. left
        for c in range(1, C):  # 1 ~ C-1
            A[0][c-1] = A[0][c]
        # 1-3. upward
        for r in range(1, ac+1): # 1 ~ AC
            A[r-1][C-1] = A[r][C-1]
        # 1-4. right
        for c in range(C-2, 0, -1): # C-2 ~ 1
            A[ac][c+1] = A[ac][c]
        A[ac][1] = 0

        # 2. bottom flow
        ac = aircon[1]
        # 2-1. upward
        for r in range(ac+2, R): # AC+2 ~ R-1
            A[r-1][0] = A[r][0]
        # 2-2. left
        for c in range(1, C):  # 1 ~ C-1
            A[R-1][c-1] = A[R-1][c]
        # 2-3. downward
        for r in range(R-2, ac-1, -1): # R-2 ~ AC
            A[r+1][C-1] = A[r][C-1]
        # 2-4. right
        for c in range(C-2, 0, -1): # C-2 ~ 1
            A[ac][c+1] = A[ac][c]
        A[ac][1] = 0
        pass

    for t in range(1,T+1):
        # log("******** t: %d", t)
        diffuse()
        # log(" after diffuse\n%s", mapstr(A, '  '))
        circulate()
        # log(" after circulate\n%s", mapstr(A, '  '))

    return sum([ sum(k) for k in A ])


R,C,T = map(int, input().split())

aircon = [-1,-1] # row index of air conditioner, [top,bottom]
A = []
for i in range(R):
    A.append(list(map(int, input().split())))
    assert len(A[-1]) == C
    if A[-1][0] == -1:
        if aircon[0]<0: aircon[0] = i
        else: aircon[1] = i

assert aircon[0]>=2 and aircon[1]>=2
# log("input\n%s", mapstr(A, '  '))

print(solve(A,aircon,T))


'''

예제 입력 1
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 1
188


run=(python3 17144.py)

echo '7 8 1\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 188


예제 입력 2
7 8 2
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 2
188

echo '7 8 2\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 188


예제 입력 3
7 8 3
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 3
186

echo '7 8 3\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 186


예제 입력 4
7 8 4
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 4
178

echo '7 8 4\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 178


예제 입력 5
7 8 5
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 5
172

echo '7 8 5\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 172


예제 입력 6
7 8 20
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 6
71

echo '7 8 20\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 71


예제 입력 7
7 8 30
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 7
52

echo '7 8 30\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 52


예제 입력 8
7 8 50
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
예제 출력 8
46


echo '7 8 50\n0 0 0 0 0 0 0 9\n0 0 0 0 3 0 0 8\n-1 0 5 0 0 0 22 0\n-1 8 0 0 0 0 0 0\n0 0 0 0 0 10 43 0\n0 0 5 0 15 0 0 0\n0 0 40 0 0 0 20 0' | $run
-> 46


6 6 1
0 0 0 0 0 5
5 0 0 0 0 0
-1 0 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


'''


