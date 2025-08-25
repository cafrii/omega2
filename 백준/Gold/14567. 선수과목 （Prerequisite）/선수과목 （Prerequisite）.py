
import sys
from collections import deque
from itertools import islice
from typing import Iterable

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    graph = [ [] for _ in range(N+1) ]
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
    return N,graph

def solve_ts(N:int, graph:list[list[int]])->Iterable[int]:
    '''
    topological sorting
    Kahn 알고리즘
    '''
    # 진입 차수 계산
    incoming = [0] * (N+1)
    for a in range(1,N+1):
        for b in graph[a]:
            incoming[b] += 1

    que = deque()
    result = [1] * (N+1) # 기본 차수. 독립 과목일 경우 1학기차에 수강.

    # 진입 차수가 0인 노드 탐색하여 큐에 추가
    for i in range(1,N+1):
        if incoming[i] == 0:
            que.append(i)

    while que:
        a = que.popleft()
        # a 에서 시작하는 모든 간선 정보 제거
        for b in graph[a]:
            incoming[b] -= 1
            result[b] = max(result[b], result[a]+1)
            if incoming[b] == 0:
                que.append(b)

    return islice(result, 1, None) # result[0]은 제외


if __name__ == '__main__':
    inp = get_input()
    lst = solve_ts(*inp)
    print(' '.join(map(str, lst)))

