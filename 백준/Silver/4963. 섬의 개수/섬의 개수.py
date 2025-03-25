
MAX_WH = 50

def solve(mp:list[list[int]]):
    # count the number of island.
    W,H = len(mp[0]),len(mp)

    visited = [ [0]*W for _ in range(H) ]

    def mark_island(y, x):
        stack = [(y,x)]
        visited[y][x] = 1
        delta = [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1) ]

        while stack:
            y,x = stack.pop()

            for dy,dx in delta:
                y2, x2 = y+dy, x+dx
                if (not 0 <= y2 < H) or (not 0 <= x2 < W):
                    continue
                if not mp[y2][x2] or visited[y2][x2]:
                    continue
                stack.append((y2, x2))
                visited[y2][x2] = 1
        return

    num_island = 0
    for y in range(H):
        for x in range(W):
            if mp[y][x] and not visited[y][x]:
                mark_island(y, x)
                num_island += 1
    return num_island

while True:
    W,H = map(int, input().split())
    if W == 0 or H == 0:
        break
    if (not 0 < W <= MAX_WH) or (not 0 < H <= MAX_WH):
        break
    mp = []
    for _ in range(H):
        mp.append(list(map(int, input().split())))
    print(solve(mp))
