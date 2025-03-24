'''
12851번

숨바꼭질 2 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	69245	19798	13710	25.996%

문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때,
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고,
가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.
'''

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


접근
가장 빠른 시간 내에 갈 수 있는 경로를 찾아야 하니, BFS 로 접근해야 한다.
또한 단순히 몇 초 후 인지만 찾는다면 경로 길이만 알면 되지만
몇 가지 방법인지까지 구해야 하므로, 각 경로마다 경로 가짓수도 같이 저장해야 한다.

5 -> 17
5, 10, 20, 19, 18, 17
5,  6,  7,  8, 16, 17
5,  4,  8, 16, 17
5, 10,  9, 18, 17
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

    def questr(q):
        # return ' '.join([ f'{x[0]}/{x[1]}/{x[2]}' for x in q ])
        a = []
        for x in q:
            sep = ":/"[x[1] % 2]
            a.append(f'{x[0]}{sep}{x[1]}{sep}{x[2]}')
        return ' '.join(a)

    while que:
        # print(questr(que))
        u,walked,cases = que.popleft()
        if u == K:
            reached = True

        if visited[u][0] < 0: # u에 처음 방문한 경우
            visited[u] = [ walked, cases ]

        elif visited[u][0] == walked:
            # walked 는 단조 증가만 할 것이므로 값이 같으면 최단 거리임.
            # 기존 경로 가짓수에, 새 가짓수를 더함. 처음 방문인 경우라면
            visited[u][1] += cases

        # print('---- reached', u, visited[u]) if u == K else None

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


'''
예제 입력 1
5 17
예제 출력 1
4
2

3 3
0
1

0 4
3
2

5 237
10
5

5 100000
19
4

5 1000
11
2

https://www.acmicpc.net/board/view/157373
0 10
0 1 2 4 8 9 10
0 1 2 3 6 12 11 10
0 1 2 4 5 10


echo '0 100000' | time python3 12851.py
22
8

'''

