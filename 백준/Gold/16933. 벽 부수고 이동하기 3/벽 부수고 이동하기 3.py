
import sys
from collections import deque

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

def solve(map1:list[str], K:int):
    '''
    벽을 부수는 능력 skill 한번 쓸 때 마다 1씩 소진.
    초기값 K (K번 부술 수 있음), 사용 시 마다 -1 하여 0 까지 가능.
    '''
    N,M = len(map1),len(map1[0])

    que = deque()
    # que 에는 (y,x,walked,skill)가 추가됨
    #    y,x 는 좌표.
    #    walked 는 "이 지점" 까지의 걸음 수 (최초 지점 포함),
    #    skill 는 벽을 부수는 트릭 사용권. 아직 사용 안했으면 K, 모두 다 사용했으면 0

    visited = [ [ [-1,-1] for x in range(M) ] for y in range(N) ]
    # 의미: visited[y][x][day_or_night]
    # visited[y][x][day_or_night] 값의 의미
    #    -1: 방문하지 않음
    #     0: skill을 다 소진한 상태에서 방문했음
    #     k: skill이 k번 남은 상태에서 방문
    #     K: skill을 한번도 쓰지 않은 상태에서 방문
    # day_or_night:
    #     0: 밤에 해당 지점 방문
    #     1: 낮에 해당 지점 방문

    que.append((0, 0, 1, K)) # (0,0)에서 시작. 초기 걸음수 1, 잔여 skill 수 K.
        # 첫 이동 1이 낮 이라고 했으니, 홀수가 낮이다.
    visited[0][0][1] = K  # 처음 이동은 낮.

    def questr(que):
        return ' '.join([ f'{y}/{x}/w{w}/{c}' for y,x,w,c in que ])

    stage = 1
    while que:
        #log('Q: %s', questr(que)) # warning! it may cause timeout.

        y,x,walked,skill = que.popleft()
        if stage != walked:
            stage = walked
            #log('------------------------- stage %d', stage)

        #log(f'  ==> ({y},{x}) w{walked}, s{skill}, visited {visited[y][x]})')

        if (y,x) == (N-1,M-1):
            #log('++++ finished! walked %d, remaining skill %d', walked, skill)
            return walked # chance를 썼던 안썼던 먼저 도달하기만 하면 됨.

        deltas = [(0,1),(1,0),(0,-1),(-1,0)]

        wall_adjacent = False
        for d in deltas:
            y2,x2 = y+d[0],x+d[1]
            if (not 0 <= y2 < N) or (not 0 <= x2 < M):
                continue

            if map1[y2][x2] == '1':
                wall_adjacent = True
                # 벽이지만, 아직 skill을 사용할 수 있다면 사용하도록 시도할 수 있음.
                if skill <= 0: # 남은 skill 이 없다면 불가능
                    continue
                if walked % 2 == 1: # 현재가 낮 일 때만 skill 사용 가능
                    # 더 적은 skill 사용하여 여기에 이미 도달했었다면 skip
                    if visited[y2][x2][0] >= skill-1:
                        continue
                    # skill을 하나 소진한 후 이동 가능.
                    que.append((y2,x2, walked+1, skill-1))
                    visited[y2][x2][0] = skill-1
            else:
                day = (walked+1) % 2 # 다음 지점이 낮이면 1, 밤이면 0
                # skill을 더 적게 사용하여 이미 방문을 했다면 더 이상 볼 필요 없음.
                if visited[y2][x2][day] >= skill:
                    continue
                que.append((y2,x2,walked+1,skill))
                visited[y2][x2][day] = skill

        # 제자리에 머무르는 가능성이 추가되었음.
        if wall_adjacent and (walked % 2 == 0):
            # 오직 벽이 인접해 있을 때, 그리고 현재가 밤이라서 한번 stay하는 것이 의미가 있을 때만 고려.
            # skill을 더 적게 사용하여 이미 방문을 했다면 더 이상 볼 필요 없음.
            # 한번 stay 한 후에도 walked 는 +1 되고 밤낮은 바뀜. 따라서 stay 후에는 낮.
            if visited[y][x][1] >= skill:
                continue
            que.append((y,x,walked+1,skill))
            visited[y][x][1] = skill

    return -1


input = sys.stdin.readline

N,M,K = map(int, input().rstrip().split())
map1 = [] # map
for _ in range(N):
    map1.append(input().rstrip()) # string with length M

# log('--------\n%s', '\n'.join(map1))
print(solve(map1,K))

