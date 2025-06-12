'''


10:16~10:35
문제 이해를 잘못했음.. 포기.




'''



def solve(map1:list[list[int]], M:int)->int:
    '''
    '''
    N = len(map1)

    def dist(loc1:tuple, loc2:tuple)->int:
        return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])

    # ckdist: chicken distance, sum of all distance between home and specific chicken store.

    def find_ckdist(store_loc:tuple[int,int])->int:
        # calculate ckdist of specified store.
        ckdist = 0
        for r in range(N):
            for c in range(N):
                # find all home and get distance
                if map1[r][c] != 1: continue
                ckdist += dist((r,c), store_loc)
        return ckdist

    # search all store, find ckdist of each store.
    dists = []
    for r in range(N):
        for c in range(N):
            if map1[r][c] != 2: continue
            dists.append(find_ckdist((r,c)))

    print(dists)
    dists.sort() # ascending order
    return sum(dists[:M])



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
예제 입력 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
예제 출력 2
10
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
'''

