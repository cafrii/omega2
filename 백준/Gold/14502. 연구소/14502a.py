'''

개선 전 코드..


'''



import sys

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
    # combi 목록은 길이 K 3 인 선택한 empty cell의 조합. empty 목록의 인덱스.
    combi = [-1] * K

    def fill_combi(index:int):
        nonlocal max_safe_size
        # combi[index] 를 가능한 값으로 채움.

        if index >= K:  # combi 하나가 모두 채워 졌음.
            check_combi(combi)
            return

        start = combi[index-1]+1 if index>0 else 0
        for i in range(start, len(empty)):
            # 조합을 만들어야 하니, 이미 사용된 cell skip.
            if i in combi[:index]: # 주의! 이 코드는 K가 크면 비효율적인 코드임.
                continue
            combi[index] = i
            fill_combi(index+1)

    fill_combi(0) # index 0 부터 시작



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
