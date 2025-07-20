'''
14502번
연구소

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	118680	69354	38878	55.783%

문제
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.
다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 NxM인 직사각형으로 나타낼 수 있으며, 직사각형은 1x1 크기의 정사각형으로 나누어져 있다.
연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

출력
첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.


-------


어떤 방식으로 풀어야 할지 감을 잡지 못하겠음.

1.
일단 문제에 시간 개념은 없다.
바이러스 근처 바로 옆이라도 막을수만 있다면 후보지가 되며
아무리 멀리 있는 곳이라도 3개 블럭으로 못 막으면 안전 지대 아님.

2.
바이러스를 하나씩 늘려가면서, 바이러스 전체를 포위할 수 있는지, 가능하다면 몇 개 블럭이 필요한지는 계산하는 방법은?
->
바이러스 퍼지는 방향이 정해져 있지 않다. 어느 방향으로 늘려갈 것인가??

3.
브루트포스 시도해 보기
->
적당한 지점을 안전 영역으로 만든 후 안전 영역이 깨지지 않는 조건 하에 넓혀가기?
일단, 공간이 있다면 한 모퉁이에 최소 3칸 안전 영역 항상 확보 가능하긴 함.
그런데 더 넓히려면 벽이 필요.
어떤 식으로 brute force search 루프를 돌릴 지, 패턴을 못찾겠음.

게다가, 안전 영역은 서로 분리되어 있을 수도 있음! 키워 나가기 방법은 쓰기 어려울 듯.

4.
??? 방법이 없나?

5.
격자의 최대 크기가 8 이다. 생각보다 작은 숫자이다. 모두 다 빈공간이라고 해도 64 칸..
이 정도면 그냥 64C3 으로 모든 가능한 벽 세우기를 다 시도해 볼 수 있는 크기일까?

64*64*62 / 3*2*1 = .. 수만 정도 일듯. 그러면 모든 조합 시도 가능함.


한번 벽을 세운 후 할 일
    - 바이러스 확산 시키기. (dfs)
    - 안전영역 크기 계산하기 (그냥 count)

의미 없는 벽세우기를 건너 뛸 방법이 있는가? (일명 pruning)
이건 방법이 딱히 없어 보이는데..

조합을 생성하는 코드가 백트래킹과 유사한데, pruning 을 안전하게 할 알고리즘은 없는 듯.
그냥 시도해 보고, 그 다음에 개선하자.


----------
개선 포인트

NxM for 루프를 최대한 없애는 것이 목표.

virus 초기 위치는 매 조합 시도 마다 바뀌지 않으니, 한번 계산 후 복제해서 사용하자. virus 초기 개수는 대체로 << 64 일 것임.

순열이 아니라 조합이다! 벽이 1 2 3 이나 2 3 1 이나 결과는 100% 동일.
이걸 깜박하고 빠뜨리면 4배 이상 시간 소요됨!

직접 조합 계산하는 로직 대신 itertools 사용할 수 있는데..
처음엔 수만 경우의 수 목록을 생성하여 메모리 문제가 있을 걸로 예상했는데, 리턴값이 제너레이터니까 괜찮다.
아무래도 python 코드 보다는 빠르지 않을까..
-> 로컬 시험에선 살짝 더 빠른데, 제출한 성적으로는 더 느려졌다! 운빨인듯..

grid -> grid2 deepcopy 를 모듈 라이브러리를 쓰면 개선 되려나?


...


8:42~9:45 구현 및 검사


'''



import sys
import itertools

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def read_quiz():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        assert len(grid[-1]) == M
    return grid


def solve(grid:list[list[int]])->int:
    '''
    grid:
        0: empty cell, 1: wall, 2: virus
    '''
    N,M = len(grid),len(grid[0])

    # 문제 조건에 의해, 3 ≤ N, M ≤ 8 이며 최대 크기가 비교적 작은 편이라
    # 모든 가능한 조건을 다 검사하는 것이 가능함.

    empty = [ (y,x) for y in range(N) for x in range(M) if grid[y][x]==0 ]
    log("initial empty %d", len(empty))

    virus = [ (y,x) for y in range(N) for x in range(M) if grid[y][x]==2 ]

    # 바이러스 확산
    def breed_viruses(grid2:list[list[int]]):
        # num_diffused = 0
        # 모든 바이러스 위치에서 확산 시작.
        # 개선: 이 초기 바아러스 위치는 항상 고정이다. 미리 계산해 놓고 복사해서 사용하자.
        stack = virus[:]

        # 간단하게 dfs 로 확산 시키자.
        while stack:
            cy,cx = stack.pop()
            for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                ny, nx = cy+dy, cx+dx
                if not (0<=ny<N and 0<=nx<M): # boundness
                    continue
                if grid2[ny][nx] != 0: # empty 가 아니면 skip
                    continue
                grid2[ny][nx] = 2
                stack.append((ny, nx))
                # num_diffused += 1
        # 확산 완료
        return # num_diffused

    # 안전 영역 확인
    def measure_safe_area(grid2:list[list[int]])->int:
        return sum( 1 for y in range(N) for x in range(M) if grid2[y][x]==0 )

    max_safe_size = 0


    def check_combi(combi:list[int]):
        nonlocal max_safe_size
        grid2 = [ e[:] for e in grid ] # deep copy

        for i in combi: # combi 조합대로 벽을 생성
            y,x = empty[i]
            grid2[y][x] = 1 # construct new wall

        breed_viruses(grid2)

        safe_size = measure_safe_area(grid2)
        if safe_size > 0:
            if max_safe_size < safe_size:
                log("%s -> safe %d", combi, safe_size)
                log("  grid %s", grid2)
                max_safe_size = safe_size
        return

    K = 3
    for tpl in itertools.combinations(range(len(empty)), K):
        check_combi(list(tpl))

    return max_safe_size



if __name__ == '__main__':
    grid = read_quiz()
    print(solve(grid))


'''

run=(python3 14502.py)

0 2 0
0 0 0
0 0 0
echo '3 3\n0 2 0\n0 0 0\n0 0 0' | $run
-> 5

echo '3 3\n0 0 0\n0 0 0\n0 0 0' | $run
-> 6
# 벽을 반드시 3개 만들어야만 하는 건가?  "새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다."

echo '7 7\n2 0 0 0 1 1 0\n0 0 1 0 1 2 0\n0 1 1 0 1 0 0\n0 1 0 0 0 0 0\n0 0 0 0 0 1 1\n0 1 0 0 0 0 0\n0 1 0 0 0 0 0' | $run
-> 27
echo '4 6\n0 0 0 0 0 0\n1 0 0 0 0 2\n1 1 1 0 0 2\n0 0 0 0 0 2' | $run
-> 9
echo '8 8\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n2 0 0 0 0 0 0 2\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0' | $run
-> 3



예제 입력 1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
예제 출력 1
27

예제 입력 2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
예제 출력 2
9

예제 입력 3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
예제 출력 3
3

'''
