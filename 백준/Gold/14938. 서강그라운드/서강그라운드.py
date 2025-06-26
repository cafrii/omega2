
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
