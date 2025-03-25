


MAX_WH = 50

def solve(mp:list[list[int]]):
    # count the number of island.
    W,H = len(mp[0]),len(mp)
    # print(f'==== {H} x {W}')
    # print(mp)

    visited = [ [0]*W for _ in range(H) ]

    def mark_island(y, x):
        stack = [(y,x)]
        visited[y][x] = 1
        delta = [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1) ]

        while stack:
            # mark
            # print(stack)
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


'''
예제 입력 1
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
예제 출력 1
0
1
1
3
1
9



시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
W,H = 50,50
print(W,H)
for y in range(H):
    print(' '.join([ str(randint(0,1)) for _ in range(W) ]))
print(0,0)
EOF
) | time python3 4963.py

python3 a.py  0.31s user 0.02s system 99% cpu 0.335 total

'''