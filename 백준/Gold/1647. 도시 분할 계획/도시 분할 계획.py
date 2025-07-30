
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    links = []
    for _ in range(M):
        a,b,c = map(int, input().split())
        links.append((a,b,c))
    return N,links


def solve_kruscal(N:int, links:list[tuple[int,int,int]])->int:
    '''
    '''
    parent = [ k for k in range(N+1) ]
    # parent[k] 는 노드 k 의 parent. parent[0] 은 미사용.

    links.sort(key = lambda x: x[2]) # sort by cost

    num_links = 0
    sum_costs = 0

    def find_root(node:int)->int:
        # 지정한 노드가 속한 트리의 root 를 찾아서 리턴.
        if node != parent[node]:
            parent[node] = find_root(parent[node])
            # 한번 찾아 둔 root는 parent[]에 저장해 둠.
        return parent[node]

    for a,b,c in links:
        if num_links >= N-2: # 두 덩어리 까지 남게 되면 종료
            break
        root_a = find_root(a)
        root_b = find_root(b)
        if root_a == root_b: # same root! it will create cycle!
            continue
        parent[root_b] = root_a  # b 를 a 밑으로. 사실 위 아래 관계는 의미 없음.
        num_links += 1
        sum_costs += c

    return sum_costs


if __name__ == '__main__':
    inp = get_input()
    print(solve_kruscal(*inp))

