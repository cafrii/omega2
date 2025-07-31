
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    roads = []
    for _ in range(M):
        x,y,z,w = map(int, input().split())
        roads.append((x,y,z,w)) # x-y 길, 표지판 z, 통행료 w
    return N,roads

def solve(N:int, roads:list[tuple[int,int,int,int]])->tuple[str,str]:
    '''
    mst 트리 구성. kruscal 알고리즘.
    '''
    root = [ k for k in range(N+1) ] # 자신이 root 이면 single node tree.

    def find_root(a:int)->int:
        if root[a] == a:
            return a
        root[a] = ra = find_root(root[a])
        return ra

    # 표지판 z 기준 정렬. 그 다음 w.
    roads.sort(key = lambda r: (r[2],r[3]))

    sum_costs = 0 # sum of w
    signs = [] # z

    for a,b,z,w in roads:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: # a,b are already in same tree. skip this road to avoid cycle
            continue
        signs.append(z)
        sum_costs += w
        # rank 신경쓰지 말고 그냥 이어 붙인다.
        root[rb] = root[b] = ra  # b,rb 를 ra 밑으로.
        if len(signs) == N-1: # 길 개수가 N-1 개 사용되면 모두 다 이어진 것임.
            break
    if len(signs) != N-1:
        return '',''  # 솔루션 없음!

    signs.sort()
    min_signs = ''.join(map(str, signs))
    return min_signs,str(sum_costs)


if __name__ == '__main__':
    inp = get_input()
    z,w = solve(*inp)
    if z: print(z,w)
    else: print(-1)
