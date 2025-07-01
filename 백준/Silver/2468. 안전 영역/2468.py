'''
2468번
안전 영역 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	130143	49989	32585	35.205%

문제
재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이 정보를 파악한다.
그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다.
이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.

어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다.
예를 들어, 다음은 N=5인 지역의 높이 정보이다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7

이제 위와 같은 지역에 많은 비가 내려서 높이가 4 이하인 모든 지점이 물에 잠겼다고 하자.
이 경우에 물에 잠기는 지점을 회색으로 표시하면 다음과 같다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7

물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며
그 크기가 최대인 영역을 말한다.
위의 경우에서 물에 잠기지 않는 안전한 영역은 5개가 된다(꼭짓점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급한다).

또한 위와 같은 지역에서 높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면 물에 잠기지 않는 안전한 영역은
아래 그림에서와 같이 네 개가 됨을 확인할 수 있다.

6	8	2	6	2
3	2	3	4	6
6	7	3	3	2
7	2	5	3	6
8	9	5	2	7

이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다.
위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면
물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.

어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

입력
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다.
N은 2 이상 100 이하의 정수이다.
둘째 줄부터 N개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다.
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다.
높이는 1이상 100 이하의 정수이다.

출력
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.


----

10:03~43

'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def gridstr(grid:list[list[int]], indent='')->str:
    res = []
    for row in grid:
        res.append(indent + ' '.join( [(f'{c:2}' if c>=0 else '__') for c in row] ))
    return '\n'.join(res)

def solve(grid:list[list[int]])->int:
    '''
    '''
    N = len(grid)
    assert len(grid[0]) == N

    def mark_region(region:list[list[int]], lvl, r, c, rid):
        # use DFS to mark safe region, starting from (r,c)
        stack = [(r,c)]
        region[r][c] = rid
        while stack:
            cr,cc = stack.pop() # current row and column
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = cr+dr,cc+dc # next r/c
                if not (0<=nr<N and 0<=nc<N): continue # exceed bound
                if grid[nr][nc] <= lvl: continue # not safe
                if region[nr][nc] >= 0: continue # already visited
                stack.append((nr,nc))
                region[nr][nc] = rid
        return

    def count_safe_region(lvl:int)->int:
        # 높이가 lvl 이하인 모든 셀이 물에 잠기는 상태에서 안전 지역의 개수 리턴.
        region = [ [-1]*N for k in range(N) ]

        num_region = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] <= lvl: continue # not safe
                if region[r][c] >= 0: continue # already visited
                mark_region(region, lvl, r, c, num_region)
                num_region += 1

        log("level: %d -> num region %d\n%s", lvl, num_region, gridstr(region, '  '))
        return num_region

    log("grid\n%s", gridstr(grid, '  '))

    levels = list(set(grid[r][c] for r in range(N) for c in range(N)))

    counts = [1]
    # for lvl in range(1,101):
    for lvl in sorted(levels):
        c = count_safe_region(lvl)
        if c <= 0: break
        counts.append(c)
    log("counts: %s", counts)
    return max(counts)



N = int(input().strip())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
    assert len(grid[-1]) == N

print(solve(grid))



'''
예제 입력 1
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
예제 출력 1
5

run=(python3 2468.py)

echo '5\n6 8 2 6 2\n3 2 3 4 6\n6 7 3 3 2\n7 2 5 3 6\n8 9 5 2 7' | $run
-> 5

예제 입력 2
7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9
예제 출력 2
6

echo '7\n9 9 9 9 9 9 9\n9 2 1 2 1 2 9\n9 1 8 7 8 1 9\n9 2 7 9 7 2 9\n9 1 8 7 8 1 9\n9 2 1 2 1 2 9\n9 9 9 9 9 9 9' | $run
-> 6

4
2 1 1 1
1 4 3 4
1 3 4 3
1 4 3 4
-> 5

'''
