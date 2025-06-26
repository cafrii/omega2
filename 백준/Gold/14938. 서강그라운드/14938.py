'''
14938번
서강그라운드 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	21172	10898	8786	49.963%

문제
예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다.
서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고 낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다.
서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다.
자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이 없어서라고 생각한 예은이는
낙하산에서 떨어질 때 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만
어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.

각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다.
예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때,
예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.

주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자.
( 원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선 위의 숫자는 거리를 의미한다)
예은이가 2번 지역에 떨어지게 되면 1번,2번(자기 지역), 3번, 5번 지역에 도달할 수 있다.
(4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.)
이렇게 되면 예은이는 23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.

입력
첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.
둘째 줄에는 n개의 숫자가 차례대로 각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.
세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.
지역의 번호는 1이상 n이하의 정수이다. 두 지역의 번호가 같은 경우는 없다.

출력
예은이가 얻을 수 있는 최대 아이템 개수를 출력한다.


--------

1:06~47


'''

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


INF = 9999  # max_N(100) x max_t(30) = 3000

def solve(distmap, T, M):
    '''
    Args:
    - distmap: distance map between nodes
    - T: list of scores for each node
    Return:
        maximum score that can be obtained within a radius M.
        All nodes can be starting nodes.
    '''
    N = len(distmap)

    # distmap contains distance for only directly connected nodes.
    # use floyd warshall to populate 2-d map,
    #   which means all distances between any nodes
    for k in range(N):
        for a in range(N):
            for b in range(N):
                # update a -> k -> b path
                distmap[a][b] = min(distmap[a][b], distmap[a][k]+distmap[k][b])

    # log("2d map completed")
    # for a in range(N):
    #     print(' '.join([ f'{distmap[a][b]:2}' for b in range(N) ]))

    visited = [0]*N
    def get_score(start, M):
        # 노드 start 에서 시작하여 반경 M 이내에서 얻을 수 있는 점수.
        if M < 0: return 0
        score = T[start]
        visited[start] = 1
        if M == 0: return score
        for n in range(N):
            if distmap[start][n] > M: continue
            if visited[n]: continue
            score += get_score(n, M-distmap[start][n])
        return score

    # 모든 노드에 대해서, 반경 M 으로 수확 가능한 점수를 계산 한 후 최대 값 리턴.
    scores = []
    for n in range(N):
        visited[:] = [0]*N
        scores.append(get_score(n, M))
        # log("(from node %d) score %d", n, scores[-1])

    # log("scores: %s", scores)
    return max(scores)



N,M,R = map(int, input().split())

T = list(map(int, input().split()))
assert len(T) == N
# T[k]: number of items in node-k.
#       node is zero-based. 0 <= k < N

distmap = [ [INF]*N for k in range(N) ]
# distmap[s][e]: distance from node s to node s.
# if not directly connected, distmap is INF.

for _ in range(R):
    a,b,dist = map(int, input().split())
    distmap[a-1][b-1] = dist
    distmap[b-1][a-1] = dist

print(solve(distmap, T, M))



'''

예제 입력 1
5 5 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3
예제 출력 1
23

run=(python3 14938.py)

echo '5 5 4\n5 7 8 2 3\n1 4 5\n5 2 4\n3 2 3\n1 2 3' | $run


5 5 5
1 2 3 4 5
1 2 2
1 3 4
1 4 2
2 3 4
4 5 2
-> 15


'''
