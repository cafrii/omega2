'''
2610번
회의준비 성공스페셜 저지

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	9833	2975	2210	29.530%

문제
KOI 준비를 위해 회의를 개최하려 한다.
주최측에서는 회의에 참석하는 사람의 수와 참석자들 사이의 관계를 따져 하나 이상의 위원회를 구성하려고 한다.
위원회를 구성하는 방식은 다음과 같다.

서로 알고 있는 사람은 반드시 같은 위원회에 속해야 한다.
효율적인 회의 진행을 위해 위원회의 수는 최대가 되어야 한다.
이런 방식으로 위원회를 구성한 후에 각 위원회의 대표를 한 명씩 뽑아야 한다.
각 위원회의 대표만이 회의 시간 중 발언권을 가지며,
따라서 회의 참석자들이 자신의 의견을 말하기 위해서는 자신이 속한 위원회의 대표에게 자신의 의견을 전달해야 한다.
그런데 각 참석자는 자신이 알고 있는 사람에게만 의견을 전달할 수 있어
대표에게 의견을 전달하기 위해서는 때로 여러 사람을 거쳐야 한다.
대표에게 의견을 전달하는 경로가 여러 개 있을 경우에는 가장 적은 사람을 거치는 경로로 의견을 전달하며
이때 거치는 사람의 수를 참석자의 의사전달시간이라고 한다.

위원회에서 모든 참석자들의 의사전달시간 중 최댓값이 최소가 되도록 대표를 정하는 프로그램을 작성하시오.

예를 들어 1번, 2번, 3번 세 사람으로 구성되어 있는 위원회에서
1번과 2번, 2번과 3번이 서로 알고 있다고 하자.
1번이 대표가 되면 3번이 대표인 1번에게 의견을 전달하기 위해서 2번을 거쳐야만 한다.
반대로 3번이 대표가 되어도 1번이 대표인 3번에게 의견을 전달하려면 2번을 거쳐야만 한다.
하지만 2번이 대표가 되면 1번과 3번 둘 다 아무도 거치지 않고 대표에게 직접 의견을 전달 할 수 있다.
따라서 이와 같은 경우 2번이 대표가 되어야 한다.

입력
첫째 줄에 회의에 참석하는 사람의 수 N이 주어진다.
참석자들은 1부터 N까지의 자연수로 표현되며 회의에 참석하는 인원은 100 이하이다.
둘째 줄에는 서로 알고 있는 관계의 수 M이 주어진다.
이어 M개의 각 줄에는 서로 아는 사이인 참석자를 나타내는 두개의 자연수가 주어진다.

출력
첫째 줄에는 구성되는 위원회의 수 K를 출력한다.
다음 K줄에는 각 위원회의 대표 번호를 작은 수부터 차례로 한 줄에 하나씩 출력한다.
한 위원회의 대표가 될 수 있는 사람이 둘 이상일 경우 그중 한 명만 출력하면 된다.

----------


4:16~4:23.
휴식
4:35~4:44
6:10~6:49

--------
개선

N 값이 그리 크지 않은 점 활용.
최단 거리 업데이트 알고리즘을 다른 것들로 교체.

2610: 이 파일. floyd-warshall.
2610a: floyd-warshall 대신 dfs 로.
2610b: dfs 보다는 bfs 가 더 적합함. (그룹내에선 최장 길이 구하는 문제이므로)
2610t: test runner

--------

최단 시간 기록

95860769 jennyeunjin  2610 맞았습니다!! 35044KB  72ms Python 3 2098B
86192381 sjlee25      2610 맞았습니다!! 34132KB  68ms Python 3 1490B  <-- best

97501377 cafrii       2610 맞았습니다!! 35016KB  80ms Python 3 2502B  <-- 2610b.py
97500473 cafrii       2610 맞았습니다!! 35036KB  92ms Python 3 2684B  <-- 2610a.py
97499279 cafrii       2610 맞았습니다!! 35068KB 104ms Python 3 4198B  <-- 2610.py

80ms 가 가장 최고는 아니지만 알고리즘 면에서 거의 유사. 그냥 이 정도에서 마무리.

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
    log("recursion limit: %d", lm)
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

    def grid2str(grid:list[list[int]], indent:str='  ', w:int=3)->str:
        # w: width to print number
        s = [ (indent + ' '.join(map(lambda x:f'{x:{w}}', ls))) for ls in grid ]
        return '\n'.join(s)

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
        log("[%d]: %d nodes, %s", gi, n, nodes)

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

        log("    dists:\n%s", grid2str(dists, '     '))

        maxdists = [ max(dists[k]) for k in range(n) ]
        log("    maxdists: %s", maxdists)

        depth = min(maxdists)
        root = maxdists.index(depth)
        log("    root: [%d] %d, depth: %d", root, nodes[root], depth)

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


'''
예제 입력 1
8
7
1 2
2 3
4 5
5 6
4 6
6 7
7 4
예제 출력 1
3
2
4
8


run=(python3 2610.py)

echo '8\n7\n1 2\n2 3\n4 5\n5 6\n4 6\n6 7\n7 4' | $run
# ->  3  2  4  8

echo '8\n0' | $run
# -> 8  1  2  3  4  5  6  7  8


echo '5\n8\n1 4\n5 3\n3 4\n3 2\n2 1\n4 2\n2 5\n1 4' | $run




------
worst-case simulation
하나의 그룹으로만 구성된 경우


(python3 <<EOF
import time
from random import seed,randint,shuffle
seed(time.time())
# seed(43)
N,M = 100,150
# N,M = 5,7
orders = list(range(1,N+1)) # 1~N
shuffle(orders)
edges = [ (orders[k-1],orders[k]) for k in range(1,len(orders)) ]
while len(edges) < M:
    i,j = randint(1,N),randint(1,N)
    if i == j: continue
    edges.append((i,j))
shuffle(edges)
print(N,M,sep='\n')
for i,j in edges: print(i,j)
EOF
) | time $run





'''

