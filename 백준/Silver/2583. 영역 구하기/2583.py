'''
2583번

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	56794	32943	25308	58.030%

문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다.
이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때,
이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면,
그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때,
K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지,
그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다.
M, N, K는 모두 100 이하의 자연수이다.
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과
오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다.
입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다.
둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
'''

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
예제 입력 1
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

예제 출력 1
3X22222
XXXX222
XXXX222
1X11XX2
1111XX2
3
1 7 13

3 3 1
1 0 2 2
1
7

4 4 1
0 0 3 3
1
7

'''

