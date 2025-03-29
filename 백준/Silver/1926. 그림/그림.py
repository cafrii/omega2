
def solve(map1:list[list[int]]):
    #
    N,M = len(map1),len(map1[0])
    visited = [ [0]*M for _ in range(N) ]

    def mark_group(sy, sx):
        stack = [(sy, sx)]
        visited[sy][sx] = 1
        extent = 1
        deltas = [(0,-1),(0,1),(-1,0),(1,0)]

        while stack:
            y2,x2 = stack.pop()
            for d in deltas:
                ny,nx = y2+d[0],x2+d[1]
                if not (0<=ny<N and 0<=nx<M):
                    continue
                if visited[ny][nx] or map1[ny][nx] == 0:
                    continue
                stack.append((ny,nx))
                visited[ny][nx] = 1
                extent += 1
            #
        return extent

    num_group = 0
    max_extent = 0

    for y in range(N):
        for x in range(M):
            if not map1[y][x] or visited[y][x]:
                continue
            group_extent = mark_group(y,x)
            num_group += 1
            max_extent = max(max_extent, group_extent)

    return num_group, max_extent

N,M = map(int, input().split())
map1 = []
for _ in range(N):
    map1.append(list(map(int, input().split())))

num, extent = solve(map1)
print(num)
print(extent)
