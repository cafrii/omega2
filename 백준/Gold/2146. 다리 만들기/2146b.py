'''

다른 사람이 제출한 답안 중 더 짧은 시간.. 92 ms

https://www.acmicpc.net/source/96835193

알고리즘 적으로 어떤 차이가 있는지 확인할 것!

-> 핵심은 최단 다리 찾는 데 있음!
# 2단계: "만남의 장소" 방식으로 최단 다리 찾기


'''

from collections import deque
import sys

# 입력 속도 개선
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
island_num = 1

# 1단계: BFS로 각 섬에 고유 번호 붙이기 (2, 3, 4...)
def number_islands(x, y):
    global island_num
    q = deque([(x, y)])
    visited[x][y] = True
    arr[x][y] = island_num

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                arr[nx][ny] = island_num
                q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            number_islands(i, j)
            island_num += 1

# 2단계: "만남의 장소" 방식으로 최단 다리 찾기
dist = [[-1] * N for _ in range(N)]
q = deque()

# 모든 육지 칸을 시작점으로 큐에 추가
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            q.append((i, j))
            dist[i][j] = 0

min_bridge = float('inf')

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            # 다른 섬의 영토를 만난 경우 (다리 완성)
            if arr[nx][ny] > 0 and arr[nx][ny] != arr[x][y]:
                bridge_len = dist[x][y] + dist[nx][ny]
                min_bridge = min(min_bridge, bridge_len)

            # 주인이 없는 바다를 만난 경우 (영토 확장)
            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                arr[nx][ny] = arr[x][y] # 바다 채워버려
                q.append((nx, ny))

print(min_bridge)

