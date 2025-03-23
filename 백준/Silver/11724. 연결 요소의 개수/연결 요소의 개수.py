
'''
이 문제 자체가 오해의 소지가 다분하다.

연결 요소의 개수를 구하라고 했으나, 간선이 연결 안된 정점도 "연결 요소" 라고 카운팅을 해야만 정답으로 인정된다.
많은 사람들이 풀이를 했음에도, 연결이 안된 단독 정점을 연결 요소로 간주한다는 표현에 별로 이의가 없는 것 같다.

찾아보면, 내가 보기엔 적절한 문제 제기가 있긴 했는데, 그냥 무시된것으로 보임.
https://www.acmicpc.net/board/view/54255

이 BOJ에 익숙한 다수의 사람들은 이런 표현에 익숙하다는 말로 해석할 수 밖에 없고,
일단은 맘에 들진 않지만 이 관례(?)에 익숙해 질 수 밖에..
'''

# 시간 초과 조건이 있으니 조금이라도 시간을 아껴야 함.
import sys
readline = sys.stdin.readline

MAX_N = 1000

def solve(graph:list[list], N:int):
    visited = [0]*(N+1) # index 0은 쓰지 않고 비워둠.

    def mark_group(start):
        # DFS 로 시도. start 를 seed 로 해서 연결된 그룹을 마킹.
        stack = [start]
        visited[start] = 1

        while stack:
            u = stack.pop()
            for k in graph[u]:
                if k == u or visited[k]:
                    continue
                stack.append(k)
                visited[k] = 1

    num_group = 0
    for j in range(1, N+1):
        if visited[j]:
            continue
        if not graph[j]:
            # 간선이 없는 정점. 이걸 count 해야만 정답이 나옴.
            num_group += 1
        else:
            mark_group(j)
            num_group += 1

    return num_group

N,M = map(int, readline().rstrip().split())
graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    s,e = map(int, readline().rstrip().split())
    # according to condition, no redundant links are provided.
    # so, we don't need to check duplication.
    graph[s].append(e) #if e not in graph[s] else None
    graph[e].append(s) #if s not in graph[e] else None

print(solve(graph, N))
