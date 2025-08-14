'''
1976번
여행 가자
골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	58563	23189	16852	37.825%

문제
동혁이는 친구들과 함께 여행을 가려고 한다.
한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다.
동혁이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자.
물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다.
예를 들어 도시가 5개 있고, A-B, B-C, A-D, B-D, E-A의 길이 있고,
동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 여행경로를 통해 목적을 달성할 수 있다.

도시들의 개수와 도시들 간의 연결 여부가 주어져 있고,
동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때 가능한지 여부를 판별하는 프로그램을 작성하시오.
같은 도시를 여러 번 방문하는 것도 가능하다.

입력
첫 줄에 도시의 수 N이 주어진다. N은 200이하이다.
둘째 줄에 여행 계획에 속한 도시들의 수 M이 주어진다. M은 1000이하이다.
다음 N개의 줄에는 N개의 정수가 주어진다. i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미한다.
1이면 연결된 것이고 0이면 연결이 되지 않은 것이다. A와 B가 연결되었으면 B와 A도 연결되어 있다.
마지막 줄에는 여행 계획이 주어진다. 도시의 번호는 1부터 N까지 차례대로 매겨져 있다.

출력
첫 줄에 가능하면 YES 불가능하면 NO를 출력한다.


----------

3:14~3:29

단순한 dsu disjoint set union 문제.


최소 시간: 36 ms

나도 36 나옴.
97465977 cafrii 1976 맞았습니다!! 32412KB 36ms Python 3 1512B

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    M = int(input().rstrip())
    grid = [] # zero-based
    for _ in range(N):
        grid.append(list(map(int, input().split())))
        # assert len(grid[-1]) == N, f"wrong grid[{_}] size"
    plan = list(map(lambda x:int(x)-1, input().split()))
    # 도시 번호를 0-base 로 변경하여 저장
    return grid,plan

def solve(grid:list[list[int]], plan:list[int])->str:
    '''
    city number starts from zero for grid,plan
    Returns:
        'YES' or 'NO' depending on plan
    '''
    N,M = len(grid),len(plan)

    roots = list(range(N))

    def find_root(a:int)->int:
        if a == roots[a]: return a
        stack = []
        while a != roots[a]:
            stack.append(a)
            a = roots[a]
        for s in stack: roots[s] = a
        return a
    # dsu
    for a in range(N):
        # 대각선 위쪽의 upper triangle 만 고려하면 됨.
        for b in range(a+1, N):
            if not grid[a][b]: continue # no way
            # make (a,b) union
            ra,rb = find_root(a),find_root(b)
            if ra == rb: continue # already in set
            roots[b] = roots[rb] = ra
    # check plan
    # 모든 도시가 하나의 set 에 포함되어 있다면 ok.
    a = find_root(plan[0])
    for k in range(1,M):
        if a != find_root(plan[k]):
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)


'''
예제 입력 1
3
3
0 1 0
1 0 1
0 1 0
1 2 3

예제 출력 1
YES


run=(python3 1976.py)

echo '3\n3\n0 1 0\n1 0 1\n0 1 0\n1 2 3' | $run
# -> YES

echo '3\n1\n0 0 0\n0 0 0\n0 0 0\n1' | $run
# -> YES

echo '3\n2\n0 0 0\n0 0 0\n0 0 0\n1 3' | $run
# -> NO


'''
