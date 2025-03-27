
from collections import deque

def solve(map1:list[str]):
    '''
    벽을 한번 부수는 것을 skill 이라고 하자.
    이 skill은 딱 한번만 사용 가능함.
    skill 이라는 변수로, 잔여 (사용 가능한) skill 수를 관리하며, 0 또는 1.
    '''
    N,M = len(map1),len(map1[0])

    que = deque()
    # que 에는 (y,x,walked,skill)가 추가됨
    #    y,x 는 좌표. walked 는 이 지점까지의 걸음 수 (시점 포함),
    #    skill 는 벽을 부수는 트릭 사용권. 아직 사용 안했으면 1, 이미 사용했으면 0

    visited = [ [ [0,0] for x in range(M) ] for y in range(N) ]
    # visited[y][x] 의 값: [ [walked_w_skill, walked_wo_skill]
    #    walked_w_skill: skill 사용한 상태로 방문 (남은 skill 0) 했을 때 walked
    #    walked_wo_skill: skill 사용하지 않고 방문 (skill 1회 남은 상태))

    reached = False
    que.append((0,0, 1, 1))
    skill = 1 # initial skill count
    visited[0][0][1] = 1

    # def questr(que):
    #     return ' '.join([ f'{y}/{x}/w{w}/{c}' for y,x,w,c in que ])

    while que:
        y,x,walked,skill = que.popleft()
        if (y,x) == (N-1,M-1):
            return walked # chance를 썼던 안썼던 먼저 도달하기만 하면 됨.

        deltas = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < N) or (not 0 <= x2 < M):
                continue

            if map1[y2][x2] == '1':
                # 벽이지만, 아직 chance를 사용할 수 있다면 사용하도록 시도할 수 있음.
                if skill <= 0: # 남은 skill 이 없다면 불가능
                    continue
                # skill 사용한 상태로 이미 방문한 경우라면.. skip
                if visited[y2][x2][0]:
                    continue
                # skill을 하나 소진한 후 이동 가능.
                que.append((y2,x2, walked+1, skill-1))
                visited[y2][x2][0] = walked+1
            else:
                # skill 사용하지도 않은 상태에서 이미 방문을 했다면 더 이상 볼 필요 없음.
                if visited[y2][x2][1]:
                    continue
                # skill 소진 상태에서 이미 여기를 방문 한 경우
                if skill <= 0 and visited[y2][x2][0]:
                    continue
                que.append((y2,x2,walked+1,skill))
                visited[y2][x2][skill] = walked+1

    return -1




N,M = map(int, input().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().strip()) # string with length M

print(solve(map1))

