import sys
def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

def solve(map1:list[str]):
    #
    N,M = len(map1),len(map1[0])
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    # area map. it stores area id (>= 0)
    map_a = [ [-1 for x in range(M)] for y in range(N) ]

    def mark_area(sy, sx, area_id):
        # starting from (sy,sx), find adjacent free connected areas
        #  and mark area id in the cell.
        # also, calculate the extent of the area and return it.
        # area id should be >= 0
        # area id of -1 means that the cell is not marked yet.

        # log("mark area starting (%d,%d), id %d ..", sy, sx, area_id)
        stack = [(sy,sx)]
        map_a[sy][sx] = area_id
        extent = 1

        while stack:
            y,x = stack.pop()
            for d in neighbors:
                y2,x2 = y+d[0],x+d[1]
                if not (0 <= y2 < N and 0 <= x2 < M):
                    continue
                if map1[y2][x2] == '1' or map_a[y2][x2] >= 0:
                    continue
                map_a[y2][x2] = area_id
                extent += 1
                stack.append((y2,x2))
        return extent

    area_extents = [] # area_extents[k]: extent of area-k
    for y in range(N):
        for x in range(M):
            if map1[y][x] == '1' or map_a[y][x] >= 0:
                continue
            extent = mark_area(y,x, area_id=len(area_extents))
            area_extents.append(extent)
            # save each area's extent

    #log('area map:')
    #for y in range(N):
    #    log('  ' + ''.join( [ (str(x) if x >= 0 else '.') for x in map_a[y] ] ))
    #log('area extents: %s', area_extents)

    # generate answer
    result:list[str] = []

    for y in range(N):
        ls = []
        for x in range(M):
            if map1[y][x] == '0':
                ls.append('0')
                continue
            # map1[y][x] == '1'
            area_ids = set()
            for d in neighbors:
                y2,x2 = y+d[0],x+d[1]
                if not (0 <= y2 < N and 0 <= x2 < M):
                    continue
                if map1[y2][x2] == '1':
                    continue
                if map_a[y2][x2] < 0:
                    log("!!(%d,%d) area_ids %d", y2, x2, map_a[y2][x2])
                    sys.exit(1)
                area_ids.add(map_a[y2][x2])
            merged_extent = 1
            for id in area_ids:
                merged_extent += area_extents[id]
            ls.append(str(merged_extent % 10))
        #
        result.append(''.join(ls))

    return result


N,M = map(int, input().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().strip())

# log('map: %s', str(map1))
map2:list[str] = solve(map1)
for s in map2:
    print(s)
