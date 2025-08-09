
import sys

def get_input():
    # return generator
    input = sys.stdin.readline
    T = int(input().rstrip())
    for _ in range(T):
        N = int(input().rstrip())
        parents = [0]*(N+1)  # parent[k] 가 0 이면 node k 는 root
        for _ in range(N-1):
            p,c = map(int, input().split()) # parent, child
            parents[c] = p
        a,b = map(int, input().split())
        yield parents,a,b
    return

def solve_with_set(parents:list[int], a:int, b:int)->int:
    '''
    '''
    a_branch = set() # a 의 브랜치 노드들
    while a:
        a_branch.add(a)
        a = parents[a]
    while b:
        if b in a_branch: return b
        b = parents[b]
    return 0  # 이런 경우는 발생하지 않음.

if __name__ == '__main__':
    it = get_input()
    for inp in it:
        r = solve_with_set(*inp)
        print(r)
