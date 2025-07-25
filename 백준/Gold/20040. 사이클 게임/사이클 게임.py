
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    lines = []
    for _ in range(M):
        a,b = map(int, input().split())
        lines.append((a,b))
    return (N,lines)


def solve(N:int, lines:list[tuple[int,int]]):
    '''
    '''
    parent = [ k for k in range(N) ]
    # parent[k] 는 노드 k 의 parent.
    # 자기 자신이 parent 라면 그 트리는 단독 노드 상태. (single node tree)

    depth = [0] * N
    # depth[k] 는 node-k 를 root로 하는 트리의 깊이 (높이)
    # 단독 노드 트리는 깊이 0 이라고 정의하자.

    def find_root(node:int)->int:
        # 지정한 노드가 속한 트리의 root 를 찾아서 리턴.
        while node != parent[node]:
            node = parent[node]
        return node

    for idx,(a,b) in enumerate(lines):
        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            # return (1-based) index when cycle is first detected
            return idx+1

        # 그냥 두 트리를 연결하면 되는데 depth를 최소화 하면 find_root 속도가 개선됨.
        # 작은 트리를 큰 트리의 서브로 이으면 크기가 더 커지지 않음.
        if depth[root_a] > depth[root_b]:
            # a 가 더 큰 트리
            parent[root_b] = root_a
        elif depth[root_a] < depth[root_b]:
            parent[root_a] = root_b
        else: # 두 트리의 크기가 같으면 아무 쪽이나 연결하고, 대신 트리 크기 갱신 필요함.
            parent[root_b] = root_a # a 아래에 b를 추가.
            depth[root_a] += 1

    # if cycle not detected, return 0
    return 0


if __name__ == '__main__':
    inp = get_input()
    print(solve(*inp))
