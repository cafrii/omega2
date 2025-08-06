'''
이 코드가 일단 실행 속도는 좀 더 빠르다.
https://www.acmicpc.net/source/96880877

아래 코드: 140ms
내  코드: 180ms

그런데 특이하게도 트리의 루트가 발전소 인지를 검사하는 검사하는 코드가 안보인다.
핵심은, 초기 발전소 노드를 가상의 root 노드의 child 로 미리 등록해 놓는 것!

나중에 subtree 가 main tree 와 결합할 때, 이 가상의 root 노드는 항상 root 로 남아야 한다.
아래 코드에서는 가상 root 는 0 으로 할당되었고
tree 이을 때 rank/depth 비교가 아닌 노드 인덱스 크기로 비교하였음.

'''
import heapq as hq
input = open(0).readline
def main():
    N, M, K = map(int, input().split())
    marked = [*map(int, input().split())]
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        hq.heappush(edges, (w, u, v))
    parent = [-1] * (N + 1)
    def find(x):
        if parent[x] < 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        a, b = x, y
        x, y = find(x), find(y)
        print(f'union ({a},{b})->({x},{y})')
        if x == y:
            return False
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
        return True
    for m in marked:
        union(0, m)
    cnt = K
    ans = 0
    while edges and cnt < N:
        w, u, v = hq.heappop(edges)
        if union(u, v):
            ans += w
            cnt += 1
    print(ans)
main()
