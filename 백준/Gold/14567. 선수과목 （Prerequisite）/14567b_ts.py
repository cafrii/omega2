'''

topological sorting 적용

'''


import sys
from collections import deque
from itertools import islice
from typing import Iterable


def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    graph = [ [] for _ in range(N+1) ]
    for _ in range(M):
        a,b = map(int, input().split())
        graph[a].append(b)
    return N,graph

# def solve_ts(N:int, links:list[tuple[int,int]])->Iterable[int]:
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
    # log("incoming: %s", incoming)

    que = deque()
    result = [1] * (N+1) # 기본 차수. 독립 과목일 경우 1학기차에 수강.

    # 진입 차수가 0인 노드 탐색하여 큐에 추가
    for i in range(1,N+1):
        if incoming[i] == 0:
            que.append(i)
    # log("que: %s", que)

    while que:
        a = que.popleft()
        # a 에서 시작하는 모든 간선 정보 제거
        for b in graph[a]:
            incoming[b] -= 1
            result[b] = max(result[b], result[a]+1)
            if incoming[b] == 0:
                que.append(b)
    del result[0]
    return result


if __name__ == '__main__':
    inp = get_input()
    lst = solve_ts(*inp)
    print(*lst)




'''
run=(python3 14567b_ts.py)

echo '3 2\n2 3\n1 2' | $run
# 1 2 3
echo '6 4\n1 2\n1 3\n2 5\n4 5' | $run
# 1 2 2 1 3 1
echo '1 0' | $run
# 1
echo '3 0' | $run
# 1 1 1
echo '3 1\n2 3' | $run
# 1 1 2


'''
