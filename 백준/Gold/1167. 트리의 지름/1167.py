'''
1167번

트리의 지름

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	69891	24149	17573	34.185%

문제
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

2:10~2:31

'''

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
graph = defaultdict(list)

for _ in range(N):
    arr = list(map(int, input().split()))
    n1 = arr[0]
    # print(f'arr: {arr}')
    for k in range(1, len(arr), 2):
        if arr[k] == -1: break
        n2, w = arr[k], arr[k+1]
        graph[n1].append((n2, w))
        # graph[n2].append((n1, w))

def solve()->int:
    #
    def find_edge(root):
        far_node, max_dist = 0, 0

        stack = [(root,0)]
        visited = set([root])

        while stack:
            n1,dist = stack.pop()
            if dist > max_dist:
                far_node,max_dist = n1,dist
            for n2,w in graph[n1]:
                if n2 in visited: continue
                stack.append((n2, dist+w))
                visited.add(n2)

        return (far_node, max_dist)

    start = 1
    edge1,_ = find_edge(start)
    edge2,dist = find_edge(edge1)

    return dist

if N <= 1:
    print(0)
else:
    print(solve())



'''
예제 입력 1
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
예제 출력 1
11

echo '5\n1 3 2 -1\n2 4 4 -1\n3 1 2 4 3 -1\n4 2 4 3 3 5 6 -1\n5 4 6 -1' | python3 1167.py

2
1 2 8 -1
2 1 8 -1
-> 8

'''




