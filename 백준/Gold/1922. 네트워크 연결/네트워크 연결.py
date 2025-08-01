
import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    M = int(input().rstrip())
    links = []
    for _ in range(M):
        a,b,c = map(int, input().split())
        if a == b: continue
        links.append((a,b,c))
    return N,links

def solve(N:int, links:list[tuple[int,int,int]])->int:
    '''
    computer node: 1 ~ N
    '''
    root = list(range(N+1))
    # initially all nodes are root (single node tree)
    # root[0] is not used

    def find_root(a:int)->int:
        if root[a] == a:
            return a
        root[a] = find_root(root[a])
        return root[a]

    # sort by cost
    links.sort(key = lambda e: e[2])
    costs = 0 # total cost

    for a,b,c in links:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue # skip if they are alredy connected

        root[b] = root[rb] = ra
        costs += c

    # assume all nodes are in one tree
    return costs

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
