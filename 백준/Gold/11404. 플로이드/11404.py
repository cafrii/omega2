'''
11404번

플로이드 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	85335	37365	26327	42.629%

문제
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다.
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다.
버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다.
시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

출력
n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다.
만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.


----

11:51~12:36 채점

'''



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

