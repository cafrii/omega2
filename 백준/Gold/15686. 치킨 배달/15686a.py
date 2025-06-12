'''
두번째 제출용 정리
itertools 사용하지 않고 직접 구현
미리 모든 조합을 다 만든 후 계산하지 않고 제너레이터 이용

itertools 사용하는 것에 비해 좀 느림.

'''

import sys
input = sys.stdin.readline

from typing import Generator

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(map1:list[list[int]], M:int)->int:
    N = len(map1)

    stores,homes = [],[]
    for r in range(N):
        for c in range(N):
            if map1[r][c] == 1: homes.append((r,c))
            elif map1[r][c] == 2: stores.append((r,c))
    S = len(stores) # 가게의 개수
    H = len(homes) # 집의 개수

    # distmap[h][s] 는 h번째 집과 s번째 가게의 거리
    distmap = [ [0]*S for _ in range(H) ]

    for h,loc_h in enumerate(homes):
        for s,loc_s in enumerate(stores):
            distmap[h][s] = abs(loc_h[0]-loc_s[0]) + abs(loc_h[1]-loc_s[1])

    # 가게의 선택 조합. stores의 index로 조합을 구성한다.
    def combinations()->Generator[list[int]]:
        selected = [0] * M
        def backtrack(idx_m, from_idx_n):
            if idx_m >= M: # one combination is composed.
                yield selected # yield list
                return
            for i in range(from_idx_n, S):
                selected[idx_m] = i
                yield from backtrack(idx_m+1, i+1)
        yield from backtrack(0, 0)

    combi_gen = combinations()
    ckdist_city_min = int(1e9)  # 도시의 치킨거리, 초기값은 적절하게 큰 값.

    for comb in combi_gen:
        # 현재 가게 조합 combi 의 마스크. S 중에서 M 을 선택하는 조합.
        # 예: S=6, M=2 일때, 선택한 조합이 (2,4) 이라면 mask는 [0,0,1,0,1,0]
        mask = [ (1 if s in comb else 0) for s in range(S) ]
        # 도시의 치킨거리는 모든 집의 치킨거리의 총합이므로, 먼저 모든 집의 치킨거리 계산.
        ckdists = [ min([ distmap[h][s] for s in range(S) if mask[s] ])
                    for h in range(H) ]
        ckdist_city = sum(ckdists) # 치킨거리의 합
        # 각 선택 조합(comb) 중에서 도시의 치킨거리가 최소가 되는 값을 찾음.
        ckdist_city_min = min(ckdist_city_min, ckdist_city)

    return ckdist_city_min


N,M = map(int, input().split())
map1 = []
for _ in range(N):
    map1.append(list(map(int, input().split())))
    assert(len(map1[-1]) == N)
print(solve(map1, M))



'''
run=(python3 15686.py)

예제 입력 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
예제 출력 1
5

echo '5 3\n0 0 1 0 0\n0 0 2 0 1\n0 1 2 0 0\n0 0 1 0 0\n0 0 0 0 2' | $run
-> 5
echo '5 2\n0 0 1 0 0\n0 0 2 0 1\n0 1 2 0 0\n0 0 1 0 0\n0 0 0 0 2' | $run
-> 5
echo '5 1\n0 0 1 0 0\n0 0 2 0 1\n0 1 2 0 0\n0 0 1 0 0\n0 0 0 0 2' | $run
-> 7



예제 입력 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
예제 출력 2
10


echo '5 1\n0 2 0 1 0\n1 0 1 0 0\n0 0 0 0 0\n2 0 0 1 1\n2 2 0 1 2' | $run
-> 21
echo '5 2\n0 2 0 1 0\n1 0 1 0 0\n0 0 0 0 0\n2 0 0 1 1\n2 2 0 1 2' | $run
echo '5 3\n0 2 0 1 0\n1 0 1 0 0\n0 0 0 0 0\n2 0 0 1 1\n2 2 0 1 2' | $run
echo '5 4\n0 2 0 1 0\n1 0 1 0 0\n0 0 0 0 0\n2 0 0 1 1\n2 2 0 1 2' | $run
echo '5 5\n0 2 0 1 0\n1 0 1 0 0\n0 0 0 0 0\n2 0 0 1 1\n2 2 0 1 2' | $run
-> 10


예제 입력 3
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
예제 출력 3
11


예제 입력 4
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
예제 출력 4
32


(python3 <<EOF
N,M = 100,5
print(N,M)
map1 = [[0 for c in range(N)] for r in range(N)]
stores = [(0,0),(0,1),(0,2),(1,0),(2,0),(3,0),(1,1),(1,2),(1,3),]
homes = [(-1,-1),(-2,-1),(-3,-1),(-1,-2),(-1,-3),(-1,-4),(-2,-2)]
for r,c in stores: map1[r][c]=2
for r,c in homes: map1[r][c]=1
for r in range(N):
    print(' '.join(map(str, map1[r])))
EOF
) | time $run


export _M=5
export _H=199

(python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
N,M = 100,int(os.getenv('_M','5'))
H,S = int(os.getenv('_H','10')),13
print(N,M)
map1 = [ [0 for c in range(N)] for r in range(N) ]
num_store,num_home = 0,0
while num_store < S:
    r,c = randint(0,N-1),randint(0,N-1)
    if map1[r][c]: continue
    map1[r][c],num_store = 2,num_store+1
while num_home < H:
    r,c = randint(0,N-1),randint(0,N-1)
    if map1[r][c]: continue
    map1[r][c],num_home = 1,num_home+1
for r in range(N):
    print(' '.join(map(str, map1[r])))
EOF
) | time $run


'''

