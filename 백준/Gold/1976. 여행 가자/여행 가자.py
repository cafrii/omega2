
import sys

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
