
import sys
input = sys.stdin.readline

MAX_NODE = 100
MAX_LINK_COST = 100_000
MAX_COST = (MAX_NODE * MAX_LINK_COST) + 1


def solve(N, M, cost:list[list]):
    '''
    플로이드-워셜 알고리즘의 기본 형태.
    i 에서 j 노드로 이동 할 때, k 를 경유해서 갈 수 있는지를 하나씩 검사.
    '''
    # 문제에 명시되어 있진 않지만, 예제를 보면 자신 노드로의 비용은 0으로 간주하는 것으로 보인다.
    for k in range(1,N+1):
        cost[k][k] = 0

    # 3중 루프로 최소 비용 모두 검사.
    # i 에서 출발하여, k 를 거쳐, j 에 도착하는 경로.
    # 루핑 순서 주의. 경유지 k가 최외곽 루프.
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return


N = int(input().strip())
M = int(input().strip())

cost = [ [MAX_COST for c in range(N+1)] for r in range(N+1) ]
# cost: 이동 비용 테이블
#   cost[i][j]는 노드-i 에서 노드-j 로 가는 비용.
#   초기값은 이론적 최대 비용.
#   노드-0 은 미사용. 즉, cost[0], cost[*][0] 은 사용되지 않음.
#
for _ in range(M):
    s,e,c = map(int, input().split())
    cost[s][e] = min(cost[s][e], c)

solve(N,M,cost)
# cost 테이블이 최소 바용으로 업데이트 됨.

for i in range(1,N+1):
    a = [ (0 if cost[i][j]==MAX_COST else cost[i][j]) for j in range(1,N+1) ]
    print(' '.join(map(str, a)))
