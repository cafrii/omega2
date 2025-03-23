'''
11724번

연결 요소의 개수 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	512 MB	157663	71598	46798	42.236%

문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v)
같은 간선은 한 번만 주어진다.
'''


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

# print(f'{M} lines input. now solving..', file=sys.stderr)
print(solve(graph, N))


'''
예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1
2

예제 입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
예제 출력 2
1

91 15
10 79
58 64
24 66
12 23
9 82
1 57
10 36
10 11
21 87
19 58
28 65
80 86
39 81
24 63
59 73
-> 76

echo '100 0' | python3 11724.py
100

4 3
4 3
4 2
4 1
-> 1

5 3
1 2
2 3
4 5
-> 2

(python3 <<EOF
import time,sys
N,M = 1000,(1000*999//2)
print(N, M)
count_m = 0
for j in range(1,N+1):
    for k in range(j+1,N+1):
       print(j, k)
       count_m += 1
if count_m != M:
    print('M {M} != count {count_m}', file=sys.stderr)
EOF
) | time python3 11724.py





'''