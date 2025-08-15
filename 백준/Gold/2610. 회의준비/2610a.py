'''

flyod-warshall 대신 dfs 만으로 시도

'''


import sys
from collections import defaultdict

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    M = int(input().rstrip())
    links = []
    for _ in range(M):
        links.append(tuple(map(int, input().split())))
    return N,links

def solve(N:int, links:list[tuple[int,int]])->list[int]:
    '''
    union set 으로 위원회 그룹 구성. 이때 graph 정보도 같이 유지되어야 함.
    구성이 완료되면 각 그룹별로 최소 깊이를 갖는 트리를 구성하고 root 선택.
    '''

    # 재귀 호출 깊이.
    lm = sys.getrecursionlimit() # 보통은 1000 인데 특수한 런타임 대비
    # log("recursion limit: %d", lm)
    sys.setrecursionlimit(max(lm, N+50))

    INF = 999 # >N+1 이기만 하면 됨

    graph = [ [] for _ in range(N+1) ]
    groups = defaultdict(list)

    def organize():
        '''
        멤버 연결 정보 (links)를 이용하여 group 을 구성. 동시에 link graph 도 재구성.
        disjoint set union 사용.
        Result:
            groups:
            graph: graph[a] 는 [ b,c,d,.. ], a-b, a-c, a-d, .. 이웃 관계
        '''
        roots = list(range(N+1))

        def find_root(a:int)->int:
            if a == roots[a]: return a
            roots[a] = find_root(roots[a])
            return roots[a]

        for a,b in links:
            # 중복 여부는 걸러내면 좋긴 하겠으나, 있어도 치명적이진 않으니 skip
            graph[a].append(b); graph[b].append(a)

            ra,rb = find_root(a),find_root(b)
            if ra == rb: continue
            roots[rb] = roots[b] = ra

        # 그룹 구성. dsu 의 root 가 일단 임시 대표.
        for a in range(1,N+1):
            ra = find_root(a)
            groups[ra].append(a)
        return

    organize()
    # log("roots: %s", groups.keys())
    # log("groups: %s", groups)

    # 각 노드 별로 소속 그룹 내 순회를 통해 최장 거리 계산
    def find_dist_dfs(start:int)->int:
        '''
        Args:
            start
        Returns:
            이 그룹의 대표자 노드
        '''
        dists = [ INF ] * (N+1) # distance from start. visited 목적으로도 활용
        stack = [ start ]
        dists[start] = 0
        while stack:
            cur = stack.pop()
            d = dists[cur]
            for nxt in graph[cur]:
                if nxt == cur: continue
                if dists[nxt] <= d+1: continue
                stack.append(nxt)
                dists[nxt] = d+1

        maxdist = max(d for d in dists if d < INF)
        return maxdist

    chieves = [ ] # 그룹 대표 목록

    for k,members in groups.items():
        dists = [ (find_dist_dfs(m),m) for m in members ]
        min_dist,m = min(dists)
        ###log("group: root %d, %s", k, members)
        ###log("       dist %s, min %d", list(zip(*dists))[0], min_dist)
        chieves.append(m)

    # 제출용 간단한 코드
    # for members in groups.values():
    #     _,m = min([ (find_dist_dfs(m),m) for m in members ])
    #     chieves.append(m)

    return [ len(groups) ] + sorted(chieves)


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print('\n'.join(map(str, r)))

