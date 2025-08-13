'''
30797번
가희와 여행가요

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1.5 초	512 MB	497	181	151	37.376%

문제
가희는 도시 시뮬레이션 게임을 하고 있습니다.
이 게임은 나의 도시와 다른 도시들을 연합하여, 나의 도시를 키우는 게임입니다.
가희의 도시에 사는 사람들은 철도만 이용하여 이동합니다.
건설된 철도 노선들을 적절히 이용하여 가희의 도시에서 도시 $a$로 이동하지 못하면,
사람들은 도시 $a$와 교류를 하지 못하게 되고, 가희의 도시는 도시 $a$와 연합할 수 없습니다.

가희는 월드에 있는 도시 $n-1$개와 가희의 도시를 연합하여 세력을 확장하려고 합니다.
이 게임은 철도 노선 $Q$개를 구매할 수 있습니다.
가희는 이 철도 노선들을 적절하게 구매하여 총 건설 비용을 최소로 하려고 합니다.
그러면서 가희의 도시와 $n-1$개의 도시들을 빠르게 연합하려고 합니다.
가희가 건설할 수 있는 철도 노선들에 대한 정보가 주어졌을 때,
총 건설 비용과 언제 $n-1$개의 도시들과 가희의 도시가 연합하는지 구해주세요.
목표를 달성하는 것이 불가능하다면 첫 줄에 -1을 출력해 주세요.

입력
첫 번째 줄에 $n$과 $Q$가 공백으로 구분되어 주어집니다.
월드에 $1$번 도시부터 $n$번 도시까지 있음을 의미하며, 가희의 도시는 $1$번 도시입니다.
또한 건설할 수 있는 노선은 $Q$개가 있음을 의미합니다.

다음
$Q$개의 줄에 건설할 수 있는 철도 노선의 정보가 아래와 같이 주어집니다.

$from\ to\ cost\ time$

이는 월드에 있는 두 도시, $from$번 도시에서 $to$번 도시를 경유하는 도시 없이,
양방향으로 연결하는 철도를 비용 $cost$를 들여 시각 $time$에 지을 수 있음을 의미합니다.
$\left( 1 \le from \le n,1 \le to \le n, from \ne to \right)$
철도 노선들은 구매하는 즉시 지어지며, 같은 시각에 여러 철도 노선을 건설할 수 있습니다.

출력
가희의 도시와 $n-1$개의 도시가 연합을 하는 시점과 총 건설 비용을 공백으로 구분하여 출력해 주세요.
만약, $n-1$개의 도시와 가희의 도시가 연합할 수 없다면, 첫 줄에 -1을 출력해 주세요.

제한
$2 \le n \le 2 \cdot 10^5$
$1 \le Q \le 2 \cdot 10^5$
$1 \le time \le 10^9$
$1 \le cost \le 10^9$


--------

3:27~3:58, 휴식
4:05~


어떤 MST 알고리즘을 사용할지 결정한 후에야 적당한 입력 데이터 포맷이 결정된다.

N: ~ 2*10^5
edges: ~ 2*10^5

경로 수가 노드 수 보다 많이 크지 않으므로, kruscal 이 적당하다.
아예 처음부터 heapq 로 받자.

건설 비용을 최소화. 건설 시간에 대한 제약은 없음.

그런데 특정 시각에만 건설이 가능한 듯 함. 그 시각이 지나면 건설이 불가능.
-> 해석 오류!
   아래 solve_kruscal() 의 코멘트 참고.


'''



import sys
from collections import defaultdict
from heapq import heappush, heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def get_input_prim():
    input = sys.stdin.readline
    N,Q = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(Q):
        a,b,c,t = map(int, input().split())
        edges[a].append((b,c,t))
        edges[b].append((a,c,t))
    return N,edges

def get_input_kruscal():
    input = sys.stdin.readline
    N,Q = map(int, input().split())
    edges = []
    for _ in range(Q):
        a,b,c,t = map(int, input().split())
        heappush(edges, (c,t,a,b))
    return N,edges



def solve_wrong(N:int, edges:dict)->tuple[int,int]:
    '''
    edge들을 단순하게 cost 기준 정렬하여 사용. 과거 시각 정보는 skip하는 방식.
    -> fail to pass!
       무조건 빠른 시각 정보를 선택하는 것이 최적의 해가 아님!

    Arguments:
        edges: dict of key:value where value is edge list from node key.
            edges[u] = [ (v,cost,time), (v2,cost,time), ..]
    Returns:
        tuple(finish_time, total_cost)
        or  tuple(-1,-1) if failed to finish construct
    '''
    total_cost = 0
    num_links = 0  # 건설된 노선 개수
    now = 0

    visited = [0]*(N+1)

    # starting from node 1.
    start = 1
    hq = [ (0, 0, 0, start) ] # cost, time, a, b

    while hq:
        c,t,prev,cur = heappop(hq)
        # prev 에서 cur 로 연결하는 노선
        log("(%d, %d) c %d, at %d", prev, cur, c, t)

        # cur 가 이미 건설 되어 있는 상태인지 확인
        if visited[cur]: continue # skip it

        # 건설 시각 가능여부 체크
        if t < now: continue # expired edge

        # 건설!
        now = t
        visited[cur] = 1
        if cur != start:
            total_cost += c
            num_links += 1
        log("  -> at %d, %d links, total c %d", now, num_links, total_cost)
        log("     %s", visited[1:])

        if num_links >= N-1:
            return now,total_cost

        # 가능한 edge 후보 추가
        for nx,nx_c,nx_t in edges[cur]:
            if visited[nx]: continue
            if nx_t < now: continue # already past

            # we cannot prune to-be-pended edges,
            # because we cannot judge edge validity (because of time-expiry)

            log("    push (%d,%d, c %d at %d)", cur, nx, nx_c, nx_t)
            heappush(hq, (nx_c, nx_t, cur, nx))

    return -1,-1


def solve_wrong2(N:int, edges:dict)->tuple[int,int]:
    '''
    edge 를 시간 순서로 정렬하여 처리하도록 변경.
    이렇게 하면 최소 비용의 mst 가 구해지지 않게 됨.
    따라서, 이미 활용된 노선이라도 더 최소 비용의 새 edge가 발견되면 업데이트 하도록 함.
    즉, 더 이상 kruscal 알고리즘이라고 부르긴 어렵고, 약간 dijkstra 방식도 섞인 구조임.

    종료 조건이 따로 없음. 그냥 heapq 가 비게 되면 종료.
    지속적으로 edge 가 갱신되므로, total cost 계산을 incremental 하게 하기 어려움.
    일단 탐색이 완료된 후, 따로 cost 계산을 위한 2차 탐색을 수행.

    -> 하지만 이 방식으로도 fail!
    아무래도 문제 출제자의 의도는 내가 이해한 것과 다른 것으로 보인다.


    Arguments:
        edges: dict of key:value where value is edge list from node key.
            edges[u] = [ (v,cost,time), (v2,cost,time), ..]
    Returns:
        tuple(finish_time, total_cost)
        or  tuple(-1,-1) if failed to finish construct
    '''
    total_cost = 0
    num_links = 0  # 건설된 노선 개수
    now = 0

    INF = int(1e9) * 2 * int(1e5)

    visited = [0]*(N+1)
    # timecost = [ [0,INF] for k in range(N+1) ]
    mincosts = [ [INF, 0] for k in range(N+1) ]
    mincosts[0][:] = [0,0]

    # starting from node 1.
    cur = 1
    hq = [ (0, 0, 0, cur) ] # time, cost, a, b

    while hq:
        t,lc,prev,cur = heappop(hq)
        # prev 에서 cur 로 연결하는 노선, time, link cost
        log("(%d, %d) c %d, at %d", prev, cur, lc, t)

        cost = mincosts[prev][0] + lc
        if cost >= mincosts[cur][0]:
            continue

        now = t
        visited[cur] = 1
        mincosts[cur][:] = [cost,lc]

        log("   -> link! (%d -> %d) lc %d whole %d", prev, cur, lc, cost)

        # 가능한 edge 후보 추가
        for nx,nx_c,nx_t in edges[cur]:
            # if visited[nx]: continue
            if nx_t < now: continue # already past

            if mincosts[nx][0] <= cost:
                log("    skip (%d,%d, c %d at %d)", cur, nx, nx_c, nx_t)
            else:
                log("    push (%d,%d, c %d at %d)", cur, nx, nx_c, nx_t)
                heappush(hq, (nx_t, nx_c, cur, nx))

    # 탐색이 끝났으면, 이제 total cost 를 재계산.
    log("1st search ended.")

    num_visited = sum(visited)
    if num_visited < N:
        log("failed, visited # %d", num_visited)
        return -1,-1

    log("end time: %d", now)
    log("link costs: %s", [mincosts[k][1] for k in range(1,N+1)])
    return now, sum( mincosts[k][1] for k in range(1,N+1) )


'''
그냥 cost 기준으로 edge 정렬 후 처리함. 시간은 무시!
탐색이 완료된 후, 그냥 최대 시간을 finish 시간으로 간주하도록 함.

-> pass!
이렇게 하니 pass가 됨. 즉, time 정보는 사실 문제에서 그닥 중요한 요소가 아니었음.
문제에서의 설명이 오해의 소지가 매우 큼.

또한, 도시가 확장한다는 표현 자체도 문제가 있음.
도시가 처음에 1에서 시작하는데, 1과 전혀 무관한 2-3 노선을 바로 건설할 수 있다는게 말은 안됨.
하지만 이게 가능하다고 하고 풀어야 정답으로 통과가 됨.

주의:
find_root() 의 재귀호출 버전은 디폴트 런타임 환경에서 수행 시 Recursion 에러 발생.
따라서 이 코드를 쓸 거면 recursion limit 을 충분히 늘려야 함.

경로 압축하는 코드가 존재함에도 불구하고 recursion depth 가 커질 수 있는 경우에 대해서는
30797e.py 의 코드와 주석을 참고한다.


'''
def solve_kruscal(N:int, edges:list):

    roots = list(range(N+1))

    def find_root(a:int)->int:
        if roots[a] == a: return a
        roots[a] = find_root(roots[a])
        return roots[a]

    num_links,total_cost = 0,0
    finished_at = 0
    while edges:
        c,t,a,b = heappop(edges)
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue  # cycle!

        roots[rb] = roots[b] = ra
        total_cost += c
        num_links += 1
        finished_at = max(finished_at, t)

        if num_links >= N-1:
            return finished_at,total_cost
    return -1,-1


if __name__ == '__main__':
    # inp = get_input_prim()
    # t,c = solve_prim(*inp)
    inp = get_input_kruscal()
    t,c = solve_kruscal(*inp)
    if t < 0: print(-1)
    else: print(t, c)




'''

예제 입력 1
4 5
1 4 1 5
2 3 1 1000000000
1 4 1 13
3 2 1 117
2 4 1 10
예제 출력 1
117 3

예제 입력 2
2 2
1 2 5 1
2 1 3 2
예제 출력 2
2 3

예제 입력 3
5 1
1 4 5 7
예제 출력 3
-1


run=(python3 30797.py)

echo '4 5\n1 4 1 5\n2 3 1 1000000000\n1 4 1 13\n3 2 1 117\n2 4 1 10' | $run
# -> 117 3
echo '2 2\n1 2 5 1\n2 1 3 2' | $run
# -> 2 3
echo '5 1\n1 4 5 7' | $run
# -> -1


2 3
1 2 10 3
1 2 10 2
1 2 10 1
# -> 1 10
echo '2 3\n1 2 10 3\n1 2 10 2\n1 2 10 1' | $run

3 3
1 2 1 1
2 3 1 100
1 3 1 2
-> 2 2
echo '3 3\n1 2 1 1\n2 3 1 100\n1 3 1 2' | $run


게시판에 소개된 그 문제

3 3
1 2 3 10
1 2 1 15
2 3 4 12
-> -1 (fail)
-> 15 5
echo '3 3\n1 2 3 10\n1 2 1 15\n2 3 4 12' | $run

일단 -1 이 나오면 틀림. 최소 비용이 아닐지라도 일단 finish 하는 경우가 있다면 그거라도 선택해야 하는 것임.
1 2 3 을 선택하지 않고, 2 3 4, 1 2 1 을 선택해야 함.
그런데 문제가 있는데, 1 만 있는 상태에서 과연 2 3 4 가 가능한 것인가 임. 1에 인접하지 않은 edge를 사용할 수 있는가?


단순히 cost가 작다는 이유 만으로 1 2 1 15 edge 를 선택하면 안되는 것이었음!!
-1 이 나오면 정렬 순서를 바꿔서 다시 시도하게 하면 되나? NO!

----------
3 4
1 2 3 10
1 2 1 15
2 3 4 12
2 3 100 16

echo '3 4\n1 2 3 10\n1 2 1 15\n2 3 4 12\n2 3 100 16' | $run

-> 16 101 (fail)  cost 우선
-> 12 7   (fail)  time 우선
-> 15 5   (ok)    최적

# 위 결과를 보면, -1 이 아닌 경우로도 반례를 만들 수 있다. time 또는 cost 우선으로만 하면 안된다는 것.

3 4
1 2 2 5
1 3 5 1
2 3 3 2
2 3 100 6
-> 6 102 (fail)   cost 우선
-> 5 7   (1에서부터 확장하는 조건)
-> 5 5

echo '3 4\n1 2 2 5\n1 3 5 1\n2 3 3 2\n2 3 100 6' | $run
-> 5 5


# 그럼 아예 time 우선으로만 하면 어떤가?

3 4
1 3 5 1
2 3 3 2
1 2 1 5
2 3 1 6
-> 2 8 (fail)   time 우선
-> 6 2
echo '3 4\n1 3 5 1\n2 3 3 2\n1 2 1 5\n2 3 1 6' | $run

이걸 보면 무조건 time 우선으로 하라고 할 수도 없다!
time 으로 탐색, cost 로 탐색 이렇게 두 번 수행한 후 더 적은 cost 선택??

dijkstra 로 풀어야 할 것으로 보인다.
대신 총 누적 비용은 탐색이 다 마무리 된 후 나중에 계산해야 한다.
역추적을 하기 위해 직전 노드도 같이 저장해 두어야 한다.

5 6
1 4 7 1
4 5 2 2
4 3 4 3
1 2 1 5
2 3 1 6
4 3 4 7

echo '5 6\n1 4 7 1\n4 5 2 2\n4 3 4 3\n1 2 1 5\n2 3 1 6\n4 3 4 7' | $run
-> 7 8 (잘못 해석)
-> 6 8

'''


