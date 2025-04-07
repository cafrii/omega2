'''
다른 사람의 풀이.


'''

import sys, queue
from collections import defaultdict

inp = sys.stdin.readlines()

N, M = int(inp[0]), int(inp[1])

# 얼마나 M 이 sparse 할지는 모르겠는데, 만약 N 조합을 가득 채우지 않을 거 같으면
# 또는 N 이 엄청 큰 수 라면 (그리고 상대적으로 M 은 N**2 에 비해 작다면)
# list 대신 아래와 같이 dict 도 메모리 사용량 측면에서는 도움이 된다.
graph = defaultdict(lambda : defaultdict(lambda : -1))
for l in inp[2:-1]:
    s, e, c = list(map(int, l.split()))
    # 아예 그래프에 넣을 때 중복 간선을 제거하고 넣고 있음.
    if graph[s][e] == -1 or graph[s][e] > c:
        graph[s][e] = c

s, e = list(map(int, inp[-1].split()))

q = queue.PriorityQueue()
q.put((0, s))
min_costs = {n : -1 for n in range(1, N + 1)}
min_costs[s] = 0

while not q.empty():
    _, n = q.get()
    # 보통은 이 곳에 다시 한번 더 체크하는게 필요한데, 그게 없어도 되는 모양임.
    for dest, cost in graph[n].items():
        if min_costs[dest] < 0:
            min_costs[dest] = cost + min_costs[n]
            q.put((min_costs[dest], dest))
        elif cost + min_costs[n] < min_costs[dest]:
            min_costs[dest] = cost + min_costs[n]

print(min_costs[e])

