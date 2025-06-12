'''
15686번
치킨 배달 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	107662	53841	32593	46.750%

문제
크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다.
도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다.
r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다.
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.

0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2

0은 빈 칸, 1은 집, 2는 치킨집이다.

(2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2,
(5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

(5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6,
(5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다.
오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다.
집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

출력
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

--------

10:27~

'''

# import itertools
import sys

input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve(map1:list[list[int]], M:int)->int:
    '''
    '''
    N = len(map1)

    # 가게 정보 수집. 개수 최대값은 문제에 의해 13 이다.
    stores = [ (r,c) for r in range(N) for c in range(N) if map1[r][c]==2 ]
    S = len(stores) # 가게의 개수
    log('stores: #%d, %s', S, stores)
    # S 최대값: 13

    homes = [ (r,c) for r in range(N) for c in range(N) if map1[r][c]==1 ]
    H = len(homes) # 집의 개수
    log('homes: #%d, %s', H, homes)
    # H 최대값: 2N = 100

    # distmap[h][s] 는 h번째 집과 s번째 가게의 거리
    distmap = [ [0]*S for _ in range(H) ]

    def dist(loc1:tuple, loc2:tuple)->int:
        return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

    for h,loc_h in enumerate(homes):
        for s,loc_s in enumerate(stores):
            distmap[h][s] = dist(loc_h,loc_s)

    log("distmap[h][s]:\n%s", '\n'.join([ str(distmap[h]) for h in range(H) ]) )

    # 가게의 선택 조합. stores의 index로 조합을 구성한다.
    def get_combinations()->list:
        result = []
        selected = [0] * M
        def backtrack(idx_m, from_idx_n):
            if idx_m >= M: # one combination is composed.
                result.append(selected[:]) # copy list and append
                return
            for i in range(from_idx_n, S):
                selected[idx_m] = i
                backtrack(idx_m+1, i+1)
        backtrack(0, 0)
        return result

    # combi_list = list(itertools.combinations(range(S), M))
    combi_list = get_combinations()
    log("combi_list: %s", combi_list)

    ckdist_city_min = int(1e9)  # 도시의 치킨거리, 초기값은 적절하게 큰 값.

    # S의 최대는 13이고, 13Cx 의 최대는 x가 6 또는 7 일때 이다.
    # 13C6 = = 13!/(7!6!) = 1716
    for comb in combi_list:
        # 현재 가게 조합 combi 의 마스크. S 중에서 M 을 선택하는 조합.
        # 예: S=6, M=2 일때, 선택한 조합이 (2,4) 이라면 mask는 [0,0,1,0,1,0]
        mask = [ (1 if s in comb else 0) for s in range(S) ]

        # 도시의 치킨거리는 모든 집의 치킨거리의 총합이므로, 먼저 모든 집의 치킨거리 계산.
        ckdists = [ min([ distmap[h][s] for s in range(S) if mask[s] ])
                    for h in range(H) ]
        ckdist_city = sum(ckdists) # 치킨거리의 합

        # 각 선택 조합(comb) 중에서 도시의 치킨거리가 최소가 되는 값을 찾음.
        ckdist_city_min = min(ckdist_city_min, ckdist_city)

        log("## store %s, mask %s, ckdists %s => %d", comb, mask, ckdists, ckdist_city)

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

