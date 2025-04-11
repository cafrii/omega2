'''
11657

타임머신 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	74289	18850	12008	26.256%

문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다.
각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다.
시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다.
둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다.

출력
만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면
첫째 줄에 -1을 출력한다.
그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는
가장 빠른 시간을 순서대로 출력한다. 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.

'''


import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)


MAX_N = 500
# MAX_EDGE = 6_000
# MIN_EC = -10_000  # minimum edge cost
MAX_EC = 10_000

# 비용 (경로 길이)가 음수가 될 수 있으니 -1 과 같은 초기값을 쓸 수 없음.
# 예상되는 최소 비용의 최대값은 1에서 출발하여 모든 정점을 다 거치는 것.
# INFINITY = ((MAX_N-1) * MAX_EC) + 1
INFINITY = (MAX_N * MAX_EC) + 1 # 넉넉하게 더 큰값을..


def solve(N:int, E:list[tuple]) -> tuple[list,list]:
    # N: 노드 (정점) 개수. 노드 번호는 1~N
    # E: 간선 리스트. 간선 형식: (start, end, cost)
    #    1<=start,end<=N,  cost는 음수가 될 수 있음.
    # return (min_cost, in_cycle)
    #    min_cost[k]: 1에서 k에 이르는 최소 비용
    #        min_cost[0]은 사용되지 않음.
    #    in_cycle[k]: k가 음의 cycle 안에 포함된 노드라면 True
    #
    # 벨만 포드 알고리즘 참고
    # https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm#Algorithm
    #

    # step 1: 초기화
    min_costs = [ INFINITY for x in range(N+1) ]
    in_cycle = [ False for x in range(N+1) ]
    # predecessor = [ -1 ] * (N+1) # 음의 사이클 경로 추적용

    min_costs[1] = 0 # starting point

    # step 2: relax edges repeatedly
    for i in range(N):
        for u,v,c in E:
            if min_costs[u] == INFINITY:
                continue

            # 디버깅. 제출 전 제거.
            if min_costs[u] + c >= INFINITY:
                log("! cost %d exceed INF!", min_costs[u] + c)
                log("loop(%d), edge (%d,%d,%d), cost[%d]:%d", i, u,v,c, u, min_costs[u])
                sys.exit(1)

            if min_costs[u] + c >= min_costs[v]:
                continue

            # 더 적은 cost(짧은 경로)가 발견되었으므로 갱신
            if i < N-1:  # N-1 루프는 음의 cycle 검사용
                min_costs[v] = min_costs[u] + c
                # predecessor[v] = u
                continue

            # 음의 cycle 감지됨
            log('edge (%d, %d) in negative cycle!', u, v)
            in_cycle[v] = True

            # 만약 이 음의 cycle 구성 정보를 추출하고 싶다면 predecessor[]를 이용해 역추적.

            # 더 진행 하는 것이 의미가 있는지는 문제 유형에 따름.
            # 모든 음의 사이클 간선을 다 체크하는게 필요하다면 계속 진행하면 됨.
            # 음의 사이클과는 완전히 독립적인 노드가 있을 수 있고, 그 노드까지의 답을 구해야 한다면
            # 끝까지 진행 한 후 결과를 보고 확인하면 된다.

    return min_costs, in_cycle


N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

min_costs, in_cycle = solve(N, edges)

# log("costs: %s,  cycle: %s", min_costs, in_cycle)
# print costs
log(','.join([ ('-' if x >= INFINITY else str(x)) for x in min_costs[1:] ]))
# print cycle
log(''.join([ ('1' if x else '.' ) for x in in_cycle[1:] ]))


# 이 문제에서는, 그래프 어딘가에 음의 사이클이 하나라도 있으면 그냥 -1 하나면 출력하라고 함.
if True in in_cycle:
    print(-1)
else:
    for c in min_costs[2:]:
        print(c if c < INFINITY else -1)



'''
예제 입력 1
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
예제 출력 1
4
3

echo '3 4\n1 2 4\n1 3 3\n2 3 -1\n3 1 -2' | python3 11657.py 2> /dev/null

python3 11657.py 2> /dev/null

예제 입력 2
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2

예제 출력 2
-1



예제 입력 3
3 2
1 2 4
1 2 3

예제 출력 3
3
-1



echo '6 6\n1 2 1\n2 3 1\n1 3 4\n3 6 2\n1 4 1\n4 6 3' | python3 11657.py 2> /dev/null
-> 1 2 1 -1 4

echo '1 1\n1 1 100' | python3 11657.py 2> /dev/null
-> 출력이 없어야 함.

echo '1 1\n1 1 -100' | python3 11657.py 2> /dev/null
-> -1

echo '3 0' | python3 11657.py 2> /dev/null
-> -1 -1

echo '3 1\n2 3 1' | python3 11657.py 2> /dev/null
-> -1 -1

echo '3 1\n1 3 0' | python3 11657.py 2> /dev/null
-> -1 0


# 시간 측정

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 500,6000
print(N, M)
for k in range(M):
    print(randint(1,N), randint(1,N), randint(-1,100))
EOF
) | time python3 11657.py > /dev/ttys016




# 무한대 초과 검사
(python3 <<EOF
N = 500
print(N, N)
for k in range(N): # 0 ~ N-1
    print(k, k+1, 10000)
EOF
) | time python3 11657.py


'''
