import sys
from collections import deque

def solve(map1:list[str], K:int):
    '''
    벽을 부수는 능력 skill 한번 쓸 때 마다 1씩 소진.
    초기값 K (K번 부술 수 있음), 사용 시 마다 -1 하여 0 까지 가능.
    '''
    N,M = len(map1),len(map1[0])

    que = deque()
    # que 에는 (y,x,walked,skill)가 추가됨
    #    y,x 는 좌표. walked 는 이 지점까지의 걸음 수 (시점 포함),
    #    skill 는 벽을 부수는 트릭 사용권. 아직 사용 안했으면 K, 모두 다 사용했으면 0

    visited = [ [ -1 for x in range(M) ] for y in range(N) ]
    # visited[y][x] 의 값:
    #    -1: 방문하지 않음
    #     0: skill을 다 소진한 상태에서 방문했음
    #     k: skill이 k번 남은 상태에서 방문
    #     K: skill을 한번도 쓰지 않은 상태에서 방문

    que.append((0, 0, 1, K))
    # skill = K # initial skill count
    visited[0][0] = K

    while que:
        y,x,walked,skill = que.popleft()

        if (y,x) == (N-1,M-1):
            return walked # chance를 썼던 안썼던 먼저 도달하기만 하면 됨.

        # deltas = [(0,1),(0,-1),(1,0),(-1,0)]
        # 우하단으로 가는 방향을 먼저 que에 넣는게 시간 단축에 도움이 될 확률이 크다.
        deltas = [(0,1),(1,0),(0,-1),(-1,0)]

        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < N) or (not 0 <= x2 < M):
                continue

            if map1[y2][x2] == '1':
                # 벽이지만, 아직 skill을 사용할 수 있다면 사용하도록 시도할 수 있음.
                if skill <= 0: # 남은 skill 이 없다면 불가능
                    continue
                # 더 적은 skill 사용하여 여기에 이미 도달했었다면 skip
                if visited[y2][x2] >= skill-1:
                    continue
                # skill을 하나 소진한 후 이동 가능.
                que.append((y2,x2, walked+1, skill-1))
                visited[y2][x2] = skill-1
            else:
                # skill을 더 적게 사용하여 이미 방문을 했다면 더 이상 볼 필요 없음.
                if visited[y2][x2] >= skill:
                    continue
                que.append((y2,x2,walked+1,skill))
                visited[y2][x2] = skill

    return -1


input = sys.stdin.readline

N,M,K = map(int, input().rstrip().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().rstrip()) # string with length M

print(solve(map1,K))
