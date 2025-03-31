'''
16933
벽 부수고 이동하기 3

유사 문제
- 2206 벽 부수고 이동하기
- 14442 벽 부수고 이동하기 2
- 16933 벽 부수고 이동하기 3
- 16946 벽 부수고 이동하기 4

주의
- 이 문제는 Python3 로는 거의 100% timeout 발생함. PyPy3 로 제출할 것!
- 실제로 제출된 답안 중 Python3 로 성공한 사례 없음.

개선 필요 사항
- visit 의 구조를 개선하면 시간 단축에 도움이 되는 것으로 보임.
- 지금 코드는 visited[y][x][day_or_night] 로 관리. 값은 skill 수.
- 새 방법은 visited[y][x][skill] 로 관리하고 값은 walked.
  - 이렇게 하면 que 에 walked 를 넣지 않아도 됨.



벽 부수고 이동하기 3 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	21746	5298	3468	22.826%


문제

NxM의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
이동하지 않고 같은 칸에 머물러있는 경우도 가능하다.
이 경우도 방문한 칸의 개수가 하나 늘어나는 것으로 생각해야 한다.

이번 문제에서는 낮과 밤이 번갈아가면서 등장한다.
가장 처음에 이동할 때는 낮이고, 한 번 이동할 때마다 낮과 밤이 바뀌게 된다.
이동하지 않고 같은 칸에 머무르는 경우에도 낮과 밤이 바뀌게 된다.

만약에 이동하는 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면,
벽을 K개 까지 부수고 이동하여도 된다. 단, 벽은 낮에만 부술 수 있다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000), K(1 ≤ K ≤ 10)이 주어진다.
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.




'벽은 낮에만 부술 수 있다' 라는 말의 해석
벽을 부수는 작업은 당연히 "이동하기 전에 발생" 해야만 한다. 하지만 이동과 동시에 부순다라고 간주하는 것이 편하다.
일단 낮 상태에서는 벽을 부술 수 있다는 것만 확인한 후,
다음 목적지가 벽 이면 낮 -> 밤으로 바뀔 때 부수고 이동하면 된다.
다음 목적지가 벽 이 아닐 수도 있으므로 미리 부숴버릴 필요 없다.

walk             K
  🌒   0 0 1 0   1
1 ☀️   A 0 1 0   1
2 🌒   0 A 1 0   1 <- 부술 수 없음. stay 해야 함.
3 ☀️   0 A 1 0   1 <- 이제 부술 수 있음.
4 🌒   0 0 A 0   0
5 ☀️   0 0 0 A
# step 2 에서 부수지 못했음. stay 후 step3 가 낮이 되었으니 부술 수 있음.
# 하지만 step3 에서 바로 부수지 않고, 목적지가 정해진 후에 step4 로 이동할 때 부수면 된다.

  🌒   0 1 0 0   1
1 ☀️   A 1 0 0   1
2 🌒   0 A 0 0   0
3 ☀️   0 0 A 0
4 🌒   0 0 0 A
# 위 경우는 벽에 인접한 step1 이 낮이므로 벽을 부술 수 있는 상태가 되었음
# step2 에서 벽을 부수고 (K 감소) 이동했음.
# step1 에서 바로 벽을 부숴버리지 않는 것이 중요함.
'''


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
        log('Q: %s', questr(que)) # warning! it may cause timeout.

        y,x,walked,skill = que.popleft()
        if stage != walked:
            stage = walked
            log('------------------------- stage %d', stage)

        log(f'  ==> ({y},{x}) w{walked}, s{skill}, visited {visited[y][x]})')

        if (y,x) == (N-1,M-1):
            log('++++ finished! walked %d, remaining skill %d', walked, skill)
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



'''
예제 입력 1
1 4 1
0010
예제 출력 1
5


예제 입력 2
1 4 1
0100
예제 출력 2
4

예제 입력 3
6 4 1
0100
1110
1000
0000
0111
0000
예제 출력 3
15

예제 입력 4
6 4 2
0100
1110
1000
0000
0111
0000
예제 출력 4
9

6 4 2
0010
1110
1000
0000
0111
0000
10

3 3 10
011
011
000
5

6 9 1
000000000
111111110
000000000
011110111
111101011
111111000
18

6 4 10
0111
1111
1111
1111
1111
1110
15

5 5 5
00100
11111
11111
11111
00000
11

'''
