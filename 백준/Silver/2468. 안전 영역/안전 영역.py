
import sys
input = sys.stdin.readline

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
                if grid[r][c] <= lvl: continue
                if region[r][c] >= 0: continue # already visited
                mark_region(region, lvl, r, c, num_region)
                num_region += 1
        return num_region

    levels = list(set(grid[r][c] for r in range(N) for c in range(N)))
    counts = [1]
    # for lvl in range(1,101):
    for lvl in sorted(levels):
        c = count_safe_region(lvl)
        if c <= 0: break
        counts.append(c)
    return max(counts)



N = int(input().strip())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
    assert len(grid[-1]) == N

print(solve(grid))
