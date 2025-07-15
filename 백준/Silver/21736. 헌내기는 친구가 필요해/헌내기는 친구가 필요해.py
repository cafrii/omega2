
import sys
input = sys.stdin.readline

def solve(map1:list[str])->int:
    '''
    '''
    N,M = len(map1),len(map1[0])
    visited = [[0]*M for y in range(N)]
    # find location of 'I'
    cy,cx = next(
        ((y, row.index('I')) for y, row in enumerate(map1) if 'I' in row),
        (0, 0)
    ) # current y and x
    if map1[cy][cx] != 'I':
        return 0

    stack = [(cy,cx)]
    visited[cy][cx] = 1
    count = 0

    while stack:
        cy,cx = stack.pop()
        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny,nx = cy+dy,cx+dx
            if not (0<=ny<N and 0<=nx<M):
                continue
            if visited[ny][nx]:
                continue
            if map1[ny][nx] == 'X':
                continue
            # map[][] is now P or O
            if map1[ny][nx] == 'P':
                count += 1
            stack.append((ny,nx))
            visited[ny][nx] = 1

    return count


N,M = map(int, input().split())

map1 = []
for _ in range(N):
    map1.append(input().strip())
    assert len(map1[-1]) == M
count = solve(map1)
print(str(count) if count > 0 else 'TT')
