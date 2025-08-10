
import sys

def get_input():
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    A = list(map(int, input().split()))
    friends = []
    for _ in range(M):
        friends.append(tuple(map(int, input().split())))
    return N,K,A,friends


def solve(N:int, K:int, A:list[int], friends:list[tuple[int,int]])->int:
    '''
    Args:
        A[k]: 노드 k+1 의 cost
        K: budget
    Returns:
        min cost
        or -1 in case of over-budget
    '''
    # A 는 index-0 부터 시작하니까 앞에 0을 하나 추가해 주었음.
    roots, costs = list(range(N+1)), [0]+A

    def find_root(a:int)->int:
        '''
        Returns: root, 이 분리 집합의 대표 (subtree root)
            최소 비용 노드를 root 로 유지함
        '''
        if roots[a] == a: return a
        stack = []
        while a != roots[a]:
            stack.append(a)
            a = roots[a]
        for k in stack: roots[k] = a
        return a

    # dsu 구성
    for a,b in friends:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue
        if costs[ra] > costs[rb]:
            roots[a] = roots[ra] = rb
        else:
            roots[b] = roots[rb] = ra

    # 각 집합의 대표 수 카운트하면서 소요 비용 합.
    total_cost = 0
    for a in range(1,N+1):
        if a != roots[a]: continue # not root
        total_cost += costs[a]
        if total_cost > K: return -1
    return total_cost

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r if r >= 0 else 'Oh no')
