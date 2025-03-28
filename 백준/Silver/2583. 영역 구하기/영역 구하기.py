
import sys
def show_map(map1):
    # show just like diagram on question.
    for y in range(len(map1)-1,-1,-1): # reverse order
        row = map1[y]
        s = [' '] * len(row)
        for i,e in enumerate(row):
            s[i] = ('X' if e == 1 else str(e-1) if e > 1 else '.')
        print(''.join(s), file=sys.stderr)


def solve(sizey:int, sizex:int, walls:list[int]):
    # map1 is 2-d array. map[][] means the point status.
    # let x be the last axis to match list representation.
    #  ie, map1[y][x]
    # dimension of map1 is (sizey * sizex)
    map1 = [ [0]*sizex for y in range(sizey) ]

    # mark walls on map. be careful not be confused by x y order.
    for (y1,x1),(y2,x2) in walls:
        # note that second coordindate component is open-ended (exclusive)
        for y in range(y1,y2): # y1 <= y < y2
            for x in range(x1,x2):
                map1[y][x] = 1

    show_map(map1)

    def mark_area(sy,sx,id=1):
        # find connected free area starting at (sy,sx)
        # calculating the extent of area
        # we can re-use map1 as 'visited' database.
        # use dfs for search
        # id is just for debugging.
        stack = [(sy,sx)]
        map1[sy][sx] = id
            # setting id is just for help debugging.
            # just setting 1 is enough.
        extent = 1

        while stack:
            ey,ex = stack.pop()
            delta = [(-1,0),(1,0),(0,-1),(0,1)]
            for dy,dx in delta:
                ny,nx = ey+dy,ex+dx # new y,x
                if not (0<=ny<sizey and 0<=nx<sizex): # should be "less than" max*
                    continue
                if map1[ny][nx] > 0: # already visited or on wall
                    continue
                stack.append((ny,nx))
                map1[ny][nx] = id
                extent += 1
        return extent

    # find free area
    areas = [] # element: (starting_point), area
    for y in range(sizey):
        for x in range(sizex):
            if map1[y][x] == 0:
                # ok, it can be free area.
                id = len(areas)+2 # 1 is used for wall.
                extent = mark_area(y,x, id)
                areas.append(((y,x), extent))

                print(f'**** ({y},{x}), area {extent}',file=sys.stderr)
                show_map(map1)

    result = [ a for (y,x),a in areas ]
    result.sort()
    return result


M,N,K = map(int, input().split())
# M is height (y axis), N is width (x axis)
walls = []
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    # x1,y1 should be lower left corner.
    # note: walls list element has (y,x) order.
    walls.append([(y1,x1),(y2,x2)])

areas = solve(M,N,walls)
print(len(areas))
print(' '.join(map(str, areas)))

'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

3X22222
XXXX222
XXXX222
1X11XX2
1111XX2
3
1 7 13
'''
