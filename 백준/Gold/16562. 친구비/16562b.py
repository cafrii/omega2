'''

초기 구현 버전

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

# 1 ≤ Ai ≤ 10,000, 1 ≤ i ≤ None
MAX_Ai = 10_000

def get_input():
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N, "wrong A size"
    friends = []
    for _ in range(M):
        v,w = map(int, input().split())
        friends.append((v,w))
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

    roots = [ [*t] for t in zip(range(N+1), [0]+A) ]
    # roots[k] 는 tuple(node, money)
    # A 는 index-0 부터 시작하니까 앞에 0을 하나 추가해 주었음.

    def find_root(a:int)->list[int,int]:
        '''
        Returns: tuple (root, cost)
            root 는 이 분리 집합의 대표 (subtree root)
            cost 는 이 집합 내의 최소 비용
        '''
        if roots[a][0] == a: return roots[a]
        stack = []
        min_cost = MAX_Ai
        while a != roots[a][0]:
            stack.append(a)
            min_cost = min(min_cost, roots[a][1])
            a = roots[a][0]
        # now, a is root of dsu
        min_cost = min(min_cost, roots[a][1])
        for k in stack: roots[k][:] = [a, min_cost]
        return roots[a]

    for a,b in friends:
        ra,ca = find_root(a)
        rb,cb = find_root(b)
        if ra == rb: continue
        cost = min(ca, cb)
        roots[b][0] = roots[rb][0] = a # updating node only is ok
        roots[ra][1] = cost

    # 각 집합의 대표 수 카운트하면서 소요 비용 합.
    num_group,total_cost = 0,0
    for a in range(1,N+1):
        ra,ma = roots[a]
        if a != ra: continue # not root
        num_group += 1
        total_cost += ma

    return total_cost if total_cost <= K else -1


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r if r >= 0 else 'Oh no')


