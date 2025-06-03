
import sys
input = sys.stdin.readline

def solve(pic:list[str])->tuple[int,int]:
    N = len(pic)

    visited = [ [-1 for c in range(N)] for r in range(N)]

    def mark(y0, x0, id, pred):
        # (y0,x0) 에서부터 시작하는 연속 영역을 찾아서 id 로 마킹
        # visited[][] 에 id 기록
        stack = [(y0,x0)]
        visited[y0][x0] = id

        deltas = [(-1,0),(1,0),(0,-1),(0,1)]
        while stack:
            y,x = stack.pop()
            col = pic[y][x]

            for dy,dx in deltas:
                ny,nx = y+dy,x+dx
                if not (0<=ny<N and 0<=nx<N):
                    continue
                if visited[ny][nx] >= 0: # already visited
                    continue
                if not pred(pic[ny][nx], col):
                    continue
                stack.append((ny,nx))
                visited[ny][nx] = id

    def count_regions(pred):
        num = 0 # number of region
        for y in range(N):
            for x in range(N):
                if visited[y][x] >= 0:
                    continue
                mark(y, x, num, pred)
                num += 1
        return num

    # predicate for each cases
    def pred_normal(c1, c2):
        return c1 == c2
    def pred_weak(c1, c2):
        return (c1 == c2 or (c1,c2) == ('R','G') or (c1,c2) == ('G','R'))

    n1 = count_regions(pred_normal)

    # reset visited and check again
    for a in visited:
        a[:] = [-1 for c in range(N)]
    n2 = count_regions(pred_weak)

    return (n1, n2)


N = int(input().strip())
pic = []
for _ in range(N):
    pic.append(input().strip())
    assert len(pic[-1]) == N

print(*solve(pic))
