'''
경로 찾기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	55427	34925	25999	62.882%

잘 이해가 안됨.
더 이상 변화가 없을 때까지 반복해야 할 것 같은데, 왜 한번만 더 돌리는지 이해가 안됨.

문제
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
'''


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def solve(graph, N):
    # define fill function
    def fill():
        changed = False
        for i in range(N):
            for j in range(N):
                if graph[i][j]:
                    continue
                # try to find path from i to j indirectly
                for k in range(N):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = 1 # fill the path
                        changed = True
                        break
        return changed

    # repeat call fill() until no change
    while fill():
        pass


# 플로이드-워셜 알고리즘의 기본적인 문제라고 함.
# 플로이드-워셜 알고리즘은 모든 정점에서 모든 정점으로의 최단 경로를 구하는 알고리즘이다.
# 플로이드-워셜 알고리즘은 3중 for문을 사용하여 구현한다.
#
# 1. i에서 j로 가는 경로가 있는지 확인한다.
# 2. i에서 k를 거쳐 j로 가는 경로가 있는지 확인한다.
# 3. 둘 중 하나라도 경로가 있으면 i에서 j로 가는 경로가 있다고 표시한다.
#
# 이렇게 모든 정점에 대해 경로가 있는지 확인하면 된다.
#
def solve2(graph, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

# solve(graph, N)
solve2(graph, N)

[ print(*graph[i]) for i in range(N) ]


'''

예제 입력 1
3
0 1 0
0 0 1
1 0 0
예제 출력 1
1 1 1
1 1 1
1 1 1

예제 입력 2
7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
예제 출력 2
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 0 0 0 0 0
1 0 1 1 1 1 1
1 0 1 1 1 1 1
0 0 1 0 0 0 1
0 0 1 0 0 0 0



'''