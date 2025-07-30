'''

여러가지 시도의 흔적들..

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

NO_LINK = 1001

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    # N: 2~100,000  M:1~1,000,000
    links = []
    links2d = [ [] for k in range(N+1) ]
    grid = [ [NO_LINK]*(N+1) for k in range(N+1) ]
    for _ in range(M):
        a,b,c = map(int, input().split())
        links.append((a,b,c))
        links2d[a].append((b,c))
        links2d[b].append((a,c))
        grid[a][b] = c
        grid[b][a] = c
    return N,links,links2d,grid

def solve_bf1(N:int, links, links2d:list[tuple[int,int,int]], grid:list[list[int]])->int:
    '''
    1. 둘 이상의 길을 가지고 있는 집에서 최저 비용 길 하나만 남기고 제거.
    2. cycle 을 제거.
    3. 마을 두 개로 분리.
    '''
    # 고민 하다가 중단.
    return 0


def solve_dp(N:int, links, links2d:list[list[tuple[int,int]]], grid:list[list[int]])->int:
    '''
    1. 이웃 노드를 하나씩 붙여가면서 최소 링크만 유지
    2. 마을 두 개로 분리.
    '''

    merged = [] # list
    merged_bf = [0]*(N+1) # boolean flag

    merged.append(1) # 1번 집을 기본으로 추가
    merged_bf[1] = 1

    for lst in links2d: # list of (b,c)
        lst.sort(key = lambda x: x[1]) # sort by cost

    def choose_next_direct(h:int)->int:
        # 이 집에 직접 연결되어 있으면서 아직 merge 안된 집을 검색
        for b,c in links2d[h]: # links2d 는 cost 로 정렬되어 있음.
            if not merged_bf[b]:
                return b
        return -1

    def choose_next()->tuple[int,int]:
        # 그 다음으로 merge 할 집을 선택.
        h,nxt = 0,0
        for h in reversed(merged):
            # 이미 merge 되어 있는 집들 중에서 하나를 선택하여
            nxt = choose_next_direct(h)
            if nxt > 0:
                break
        assert nxt > 0, f"cannot find next home, merged {merged}"
        return h,nxt

    while len(merged) < N:
        # 그 다음으로 merge 할 집을 선택.
        h,nxt = choose_next()
        merged.append(nxt)
        merged_bf[nxt] = 1

    # 알고 보니, 이게 결국 MST 트리 만드는 방법이다..
    # give up!
    return 0


def solve_kruscal(N:int, links:list[tuple[int,int,int]], links2d, grid)->int:
    '''
    '''
    parent = [ k for k in range(N+1) ]
    # parent[k] 는 노드 k 의 parent. parent[0] 은 미사용.
    # rank = [0] * (N+1)
    # rank[k] 는 node-k 를 root로 하는 트리의 크기 (깊이, 높이)
    # 단독 노드 트리는 rank 0

    links.sort(key = lambda x: x[2]) # sort by cost

    num_links = 0
    sum_costs = 0

    def find_root(node:int)->int:
        # 지정한 노드가 속한 트리의 root 를 찾아서 리턴.
        # while node != parent[node]:
        #     node = parent[node]
        if node != parent[node]:
            parent[node] = find_root(parent[node])
            # 한번 찾아 둔 root는 parent[]에 저장해 둠.
        return parent[node]

    for a,b,c in links:
        if num_links >= N-2:
            break

        root_a = find_root(a)
        root_b = find_root(b)

        if root_a == root_b:
            log("(%d %d), same root %d", a, b, root_a)
            continue

        # 그냥 두 트리를 연결하면 되는데 depth를 최소화 하면 find_root 속도가 개선됨.
        # 작은 트리를 큰 트리의 서브로 이으면 크기가 더 커지지 않음.
        # if rank[root_a] > rank[root_b]: # a 가 더 큰 트리
        #     parent[root_b] = root_a
        # elif rank[root_a] < rank[root_b]:
        #     parent[root_a] = root_b
        # else: # 두 트리의 크기가 같으면 아무 쪽이나 연결하고, 대신 트리 크기 갱신 필요함.
        #     parent[root_b] = root_a # a 아래에 b를 추가.
        #     rank[root_a] += 1

        parent[root_b] = root_a  # b 를 a 밑으로. 사실 위 아래 관계는 의미 없음.
        num_links += 1
        sum_costs += c

    return sum_costs




if __name__ == '__main__':
    inp = get_input()
    # r = solve(*inp)
    r = solve_kruscal(*inp)
    print(r)


