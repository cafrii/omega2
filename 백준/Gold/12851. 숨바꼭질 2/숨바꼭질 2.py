'''
이 문제도 별로 좋은 문제가 아니다.

1에서 출발하는 경우, 1+1 과 1*2 는 둘 다 2 이므로,
사실 경로로 보면 동일하기 때문에 한가지 경우로 카운팅 해야 한다고 생각했음.

그런데 이 문제에서는 채점 결과를 보면
+1 은 걷기, *2 는 순간이동 으로 방법이 서로 다르기 때문에
이를 서로 다르게 간주하고 있다.

이런 모호함은 코딩 문제를 국어 문제로 만들어 버리는 좋지 않은 효과가 있다.
이러한 중복 경우를 미처 생각하지도 못하고 코딩한 사람은 통과했을 것이고
나름 신경써서 이런 edge case를 찾아낸 개발자는 떨어지는...
'''

from collections import deque

MAX_NK = 100_000

def solve(N, K) -> list[int,int]:
    # 0 <= N and K <= MAX_NK
    # N 에서 K에 이르는 최단 경로 및 경우의 수를 구하여 리턴
    # 리턴 값: [walked, cases]

    # 특수 유형 처리
    if K <= N:
        return [ N-K, 1 ]

    que = deque()
    # 큐에는 다음 경유지의 정보를 다음과 같은 튜플로 저장.
    # (node, walked, count)
    #   node 는 이동해야 하는 다음 경유지
    #   walked 는 node 까지 가는 길이
    #   cases 는 node 까지 가는 경로의 경우의 수

    visited = [ [-1,0] for _ in range(MAX_NK + 1) ]
    # visited[u] 는 [walked, count]
    #   u: 노드 번호
    #   walked: N 에서 u 에 이르는 "최단" 경로 길이 (걸음 수)
    #     walked == -1 이면 방문 하지 않은 곳.
    #   cases: u 에 이르는 최단 경로의 경우의 수

    que.append((N, 0, 1))
    visited[N] = [0, 1]  # 자기 자신으로의 경로 길이는 0

    reached = False

    while que:
        u,walked,cases = que.popleft()
        if u == K:
            reached = True

        if visited[u][0] < 0: # u에 처음 방문한 경우
            visited[u] = [ walked, cases ]

        elif visited[u][0] == walked:
            # walked 는 단조 증가만 할 것이므로 값이 같으면 최단 거리임.
            # 기존 경로 가짓수에, 새 가짓수를 더함. 처음 방문인 경우라면
            visited[u][1] += cases

        if reached:  # 새로 추가하지 않고 현재 walked 수준에서 마무리.
            continue

        # 주의:
        #  1+1 과 1*2 는 둘 다 2 이므로, 경로로 보면 동일한 건데, 이 문제에서는
        #  +1 은 걷기, *2 는 순간이동 이라서 이를 서로 다르게 간주하고 있다.
        #
        # for v in set([u-1, u+1, 2*u]):
        for v in [u-1, u+1, 2*u]:
            if not (0 <= v <= MAX_NK):
                continue
            if v == u:
                continue

            # que 에 이미 들어가 있더라도 추가해야 함.
            # 이미 방문한 곳이라고 하더라도, walked 가 같으면 추가.
            if visited[v][0] in (-1, walked+1):
                que.append( (v, walked+1, cases) )

    return visited[K]


N,K = map(int, input().split())
dist,count = solve(N, K)
print(dist)
print(count)

