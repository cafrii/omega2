
import itertools
import sys

input = sys.stdin.readline

#def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve(map1:list[list[int]], M:int)->int:
    '''
    '''
    N = len(map1)

    # 가게 정보 수집. 개수 최대값은 문제에 의해 13 이다.
    stores = [ (r,c) for r in range(N) for c in range(N) if map1[r][c]==2 ]
    # 가게의 최대 개수: 13

    homes = [ (r,c) for r in range(N) for c in range(N) if map1[r][c]==1 ]
    # 집의 최대 개수는 2N = 100

    distmap = [ [0]*len(stores) for _ in range(len(homes)) ]
    # ckdist = [0] * len(homes) # 각 집 별 치킨거리 계산

    def dist(loc1:tuple, loc2:tuple)->int:
        return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

    for y,h in enumerate(homes):
        for x,s in enumerate(stores):
            distmap[y][x] = dist(h,s)

    #-----------
    combi_list = list(itertools.combinations(range(len(stores)), M))

    ckdist_city_min = int(1e9)

    # M의 최대는 13이고, combination 의 최대는 6 or 7 일 때 이다.
    # 6C13 = 13x12x11x10x9x8 / 6! = 13!/(7!6!) = 1716
    for comb in combi_list:
        # 현재 가게 조합 comb 의 마스크. 예: M=6 이고 조합이 (2,4) 이라면 [0,0,1,0,1,0]
        mask = [ (1 if k in comb else 0) for k in range(len(stores)) ]
        ckdists = []
        # ckdist_city = 0
        for y in range(len(homes)):
            # 현재 집에서 선택된 일부 가게로의 거리의 합
            ckdist = min([ distmap[y][k] for k in range(len(stores)) if mask[k] ])
            ckdists.append(ckdist)
        # 모든 집의 치킨거리의 총 합 => 도시의 치킨거리
        ckdist_city = sum(ckdists)
        ckdist_city_min = min(ckdist_city_min, ckdist_city)

    return ckdist_city_min


N,M = map(int, input().split())

map1 = []
for _ in range(N):
    map1.append(list(map(int, input().split())))
    assert(len(map1[-1]) == N)

print(solve(map1, M))

