'''
1865번

웜홀

시간이 4.7초 나 소요되었어도 통과. 이는 총 소요 시간일거 같고, 각 TC는 조건을 준수했는지도..
내 제줄
    제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
    93081566	cafrii	1865	맞았습니다!!	36520	4732	Python 3 / 수정	2710	25초 전

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	66003	15660	9638	20.941%

문제
때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다.
(단 도로는 방향이 없으며 웜홀은 방향이 있다.)
웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다.
웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다.
한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때,
출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다.
여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

입력
첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데 각 테스트케이스의 첫 번째 줄에는 지점의 수 N(1 ≤ N ≤ 500),
도로의 개수 M(1 ≤ M ≤ 2500), 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다.
그리고 두 번째 줄부터 M+1번째 줄에 도로의 정보가 주어지는데 각 도로의 정보는 S, E, T 세 정수로 주어진다.
S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다.
그리고 M+2번째 줄부터 M+W+1번째 줄까지 웜홀의 정보가 S, E, T 세 정수로 주어지는데 S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다.
T는 10,000보다 작거나 같은 자연수 또는 0이다.

두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

출력
TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.


'''

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

INFINITY = int(1e8)
# max edge cost = 10_000, max N = 500
# max total costs ~= 500 * 10_000 = 5e6


def solve(N:int, edges:list[tuple[int,int,int]]):
    # N: number of node
    # edges: list of (start,end,cost)
    #        1<=start,end<=N
    #        cost can be negative

    # 출발 위치가 명시되어 있지 않음. 즉, 어느 노드에서도 출발 할 수 있다는 말임.
    # 모든 노드를 출발 노드로 해서 다 확인 필요. 단, 이미 방문한 노드는 skip 가능함.
    visited = [0] * (N+1)
    visited[0] = 1  # 노드 0은 사용하지 않을 것이고, 그래서 방문으로 체크.

    for S in range(N+1):
        if visited[S]: continue

        mc = [INFINITY]*(N+1) # minimum cost
        mc[S] = 0
        visited[S] = 1

        for i in range(N): # 노드 개수 횟수. 마지막 루프는 음의 사이클 검사용.
            for s,e,c in edges:
                if mc[s] == INFINITY: continue
                if mc[s]+c >= mc[e]: continue
                # update 필요
                visited[e] = 1
                if i < N-1:
                    mc[e] = mc[s] + c
                else: # 음의 cycle!
                    log('negative cycle! S:%d, cycle:%d,%d', S, s,e)
                    return 'YES'
        log('no cycle from S:%d', S)
    return 'NO'


TC = int(input().strip())
for _ in range(TC):
    N,M,W = map(int, input().split())
    # N(1 ≤ N ≤ 500), M(1 ≤ M ≤ 2500), W(1 ≤ W ≤ 200)

    graph = [ [ INFINITY for x in range(N+1) ] for y in range(N+1) ]
    # graph[k][j]: k -> j 간선의 cost
    for m in range(M):
        S,E,T = map(int, input().split())
        # 두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. -> cost 가 작은 것 하나만 선택
        # 도로는 양방향이므로 두 곳에 업데이트
        if graph[S][E] == INFINITY:
            graph[E][S] = graph[S][E] = T
        else:
            graph[E][S] = graph[S][E] = min(graph[S][E], T)

    for w in range(W):
        S,E,T = map(int, input().split())
        # 웜홀은 단방향.
        # 도로와 웜홀이 동일한 시작/끝 노드로 존재하는지는 명확하지 않지만, 있다고 하더라도 웜홀만 의미가 있음.
        if graph[S][E] == INFINITY:
            graph[S][E] = -T
        else:
            graph[S][E] = min(graph[S][E], -T)

    # 간선 정보로 취합
    edges = []
    for a in range(1, N+1): # 1~N
        for b in range(1, N+1):
            if graph[a][b] < INFINITY:
                edges.append((a,b,graph[a][b]))

    log("%s", edges)
    print(solve(N,edges))


'''
예제 입력 1
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8
예제 출력 1
NO
YES

echo '1\n3 3 1\n1 2 2\n1 3 4\n2 3 1\n3 1 3\n3 2 1\n1 2 3' | python3 1865.py
->
echo '1\n3 2 1\n1 2 3\n2 3 4\n3 1 8' | python3 1865.py
->


1
1 0 0
-> NO

1
1 1 0
1 1 0
-> NO

1
1 1 1
1 1 1
1 1 1
-> YES

1
1 0 1
1 1 0
-> NO

1
1 0 1
1 1 1
-> YES

1
2 0 0
-> NO

1
2 0 2
1 2 0
2 1 1
-> YES


'''
