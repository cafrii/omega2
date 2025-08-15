
import sys
from collections import defaultdict

#def log(fmt, *args): print(fmt % args, file=sys.stderr)

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
    sys.setrecursionlimit(max(lm, N+50))

    INF = 999 # >N+1 이기만 하면 됨

    graph2d = [ [INF]*(N+1) for _ in range(N+1) ] # links 의 2x2 grid 타입의 그래프
    groups = defaultdict(list)

    def organize():
        '''
        멤버 연결 정보 (links)를 이용하여 group 을 구성. 동시에 link graph 도 재구성.
        disjoint set union 사용.
        Result:
            groups:
            graph2d: { chief:[members ..] } 형태의 dict. 여기서 chief 는 임시!
        '''
        roots = list(range(N+1))

        def find_root(a:int)->int:
            if a == roots[a]: return a
            roots[a] = find_root(roots[a])
            return roots[a]

        for a,b in links:
            graph2d[a][b] = graph2d[b][a] = 1
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

    #def grid2str(grid:list[list[int]], indent:str='  ', w:int=3)->str:
    #    s = [ (indent + ' '.join(map(lambda x:f'{x:{w}}', ls))) for ls in grid ]
    #    return '\n'.join(s)

    # 각 그룹에 대해서 대표 선택
    def find_chief(gi:int, nodes:list[int])->int:
        '''
        이 그룹 내의 노드로만 구성된 별도의 grid 준비하고 모든 노드 간 거리 계산
        각 노드 별 최대 거리 구하고 이 최대 거리가 최소가 되는 노드를 대표로 선정.
        Args:
            gi: group index (just for debugging)
            nodes: 그룹 소속 노드들
        Returns:
            이 그룹의 대표자 노드
        '''
        n = len(nodes)
        #log("[%d]: %d nodes, %s", gi, n, nodes)

        # 이 그룹에 포함된 인원만 별도로 뽑아서, 그들만의 distance grid 생성.
        dists = [ [INF]*n for _ in range(n) ]
        # dists[i][j] 는 "i번째 노드" 에서 "j번째 노드" 로의 최단 거리.
        # 주의: 노드 i와 노드 j의 거리를 의미하는 것이 아님!

        for i in range(n):
            for j in range(n):
                ii,jj = nodes[i],nodes[j]
                dists[i][j] = graph2d[ii][jj] if i!=j else 0

        # floyd-warshall, 각 노드 간 최단 거리 업데이트
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # i 에서 k 를 거쳐 j 로 가는 경우에 대한 검사
                    if dists[i][j] > dists[i][k] + dists[k][j]:
                        dists[i][j] = dists[i][k] + dists[k][j]

        #log("    dists:\n%s", grid2str(dists, '     '))
        maxdists = [ max(dists[k]) for k in range(n) ]
        #log("    maxdists: %s", maxdists)
        depth = min(maxdists)
        root = maxdists.index(depth)
        #log("    root: [%d] %d, depth: %d", root, nodes[root], depth)

        # root 는 이 그룹 대표의 index 이고, 실제 노드 번호를 리턴해야 함.
        return nodes[root]

    chieves = [ ] # 그룹 대표 목록

    for i,k in enumerate(groups.keys()):
        chief = find_chief(i, groups[k])
        chieves.append(chief)

    return [ len(groups) ] + sorted(chieves)


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print('\n'.join(map(str, r)))
