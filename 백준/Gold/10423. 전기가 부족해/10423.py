'''
10423번
전기가 부족해 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	4812	3311	2541	69.143%

문제
세계에서 GDP가 가장 높은 서강 나라는 소프트웨어와 하드웨어 기술이 모두 최고라서 IT강국이라 불리고,
2015년부터 세상에서 가장 살기 좋은 나라 1등으로 꼽히고 있다.

살기 좋은 나라 1등으로 꼽힌 이후 외국인 방문객들이 많아졌고,
그에 따라 전기 소비율이 증가하여 전기가 많이 부족한 상황이 되었다.
따라서 서강 나라의 대통령은 최근 개발이 완료된 YNY발전소 프로젝트를 진행 하기로 하였다.
발전소를 만들 때 중요한 것은 발전소 건물과 도시로 전기를 공급해 줄 케이블이다.
발전소는 이미 특정 도시에 건설되어 있고, 따라서 추가적으로 드는 비용은 케이블을 설치할 때 드는 비용이 전부이다.
이 프로젝트의 문제는 케이블을 설치할 때 드는 비용이 굉장히 크므로 이를 최소화해서 설치하여 모든 도시에 전기를 공급하는 것이다.
여러분은 N개의 도시가 있고 M개의 두 도시를 연결하는 케이블의 정보와 K개의 YNY발전소가 설치된 도시가 주어지면
케이블 설치 비용을 최소로 사용하여 모든 도시에 전기가 공급할 수 있도록 해결해야 한다.
중요한 점은 어느 한 도시가 두 개의 발전소에서 전기를 공급받으면 낭비가 되므로
케이블이 연결되어있는 도시에는 발전소가 반드시 하나만 존재해야 한다.
아래 Figure 1를 보자. 9개의 도시와 3 개의 YNY발전소(A,B,I)가 있고, 각각의 도시들을 연결할 때 드는 비용이 주어진다.

Figure 1
Figure 2

이 예제에서 모든 도시에 전기를 공급하기 위하여 설치할 케이블의 최소 비용은 22이고, Figure 2의 굵은 간선이 연결한 케이블이다.
B 도시는 연결된 도시가 하나도 없지만, 발전소가 설치된 도시는 전기가 공급될 수 있기 때문에 상관없다.

입력
첫째 줄에는 도시의 개수 N(1 ≤ N ≤ 1,000)과 설치 가능한 케이블의 수 M(1 ≤ M ≤ 100,000)개, 발전소의 개수 K(1 ≤ K ≤ N)개가 주어진다.
둘째 줄에는 발전소가 설치된 도시의 번호가 주어진다.
셋째 줄부터 M개의 두 도시를 연결하는 케이블의 정보가 u, v, w로 주어진다.
이는 u도시와 v도시를 연결하는 케이블을 설치할 때 w의 비용이 드는 것을 의미한다.
w는 10,000보다 작거나 같은 양의 정수이다.

출력
모든 도시에 전기를 공급할 수 있도록 케이블을 설치하는 데 드는 최소비용을 출력한다.


-----

3:37~4:14


kruscal 을 사용해야 할 듯.
단, 종료 조건을 잘 검사해야 한다.

'''



import sys
from heapq import heappush, heappop

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,M,K = map(int, input().split())
    lsk = list(map(int, input().split()))
    assert len(lsk) == K, "wrong k"
    edges = []
    for _ in range(M):
        u,v,w = map(int, input().split())
        heappush(edges, (w,u,v))
    return N,lsk,edges


def solve(N:int, listk:list[int], edges:list[tuple[int,int,int]])->int:
    '''
    edges: list of tuple(u,v,w) where w is cost between u and v
    use kruscal to complete mst.
    '''
    K = len(listk)

    log("edges: %s", edges)
    log("K: %d, %s", K, listk)

    is_k = [0]*(N+1)   # 발전소 여부
    for k in listk:
        is_k[k] = 1

    root = list(range(N+1))
    num_links = 0
    total_cost = 0

    def find_root(a:int)->int:
        if a == root[a]: return a
        root[a] = find_root(root[a])
        return root[a]

    # 발전소를 subtree 의 root 로 하여 확장시켜야 한다.
    while edges:
        w,a,b = heappop(edges)

        # log("(%d, %d, w %d)", a, b, w)
        ra,rb = find_root(a), find_root(b)

        if ra == rb: # skip if a,b is in same tree
            continue
        if is_k[ra] and is_k[rb]: # 두 발전소 tree 를 연결할 수 없음.
            continue
        if is_k[ra]: # a 쪽에 발전소가 있음. rb 를 ra 밑으로 붙이자.
            root[b] = root[rb] = ra
        else: # b 쪽에 발전소. ra 를 rb 밑으로.
            root[a] = root[ra] = rb

        total_cost += w
        num_links += 1
        log("(%d, %d), w%d, root: %s -> tc %d", a, b, w, root[1:], total_cost)
        if num_links >= N - K:
            break

    return total_cost



def solve_fast2(N:int, listk:list[int], edges:list[tuple[int,int,int]])->int:
    '''
    edges: heapque of tuple(w,u,v) where w is cost between u and v
    use kruscal to complete mst.
    '''
    K = len(listk)

    root = list(range(N+1))

    def find_root(a:int)->int:
        if a == root[a]: return a
        root[a] = find_root(root[a])
        return root[a]

    # 발전소 노드는 가상의 root(노드-0) child로 미리 등록.
    for k in listk: root[k] = 0

    num_links = K
    total_cost = 0

    while edges:
        w,a,b = heappop(edges)
        # log("(%d, %d, w %d)", a, b, w)
        ra,rb = find_root(a), find_root(b)

        if ra == rb: # skip if a,b is in same tree
            continue
        if ra == 0: # a 쪽의 subree 가 main
            root[b] = root[rb] = ra
        else:
            root[a] = root[ra] = rb

        total_cost += w
        num_links += 1
        # log("(%d, %d), w%d, root: %s -> tc %d", a, b, w, root[1:], total_cost)
        if num_links >= N:
            break
    return total_cost


if __name__ == '__main__':
    inp = get_input()
    r = solve_fast2(*inp)
    print(r)


'''

예제 입력 1
9 14 3
1 2 9
1 3 3
1 4 8
2 4 10
3 4 11
3 5 6
4 5 4
4 6 10
5 6 5
5 7 4
6 7 7
6 8 4
7 8 5
7 9 2
8 9 5
예제 출력 1
22

예제 입력 2
4 5 1
1
1 2 5
1 3 5
1 4 5
2 3 10
3 4 10
예제 출력 2
15

예제 입력 3
10 9 5
1 4 6 9 10
1 2 3
2 3 8
3 4 5
4 5 1
5 6 2
6 7 6
7 8 3
8 9 4
9 10 1
예제 출력 3
16


run=(python3 10423.py)

echo '9 14 3\n1 2 9\n1 3 3\n1 4 8\n2 4 10\n3 4 11\n3 5 6\n4 5 4\n4 6 10\n5 6 5\n5 7 4\n6 7 7\n6 8 4\n7 8 5\n7 9 2\n8 9 5' | $run
# -> 22

echo '4 5 1\n1\n1 2 5\n1 3 5\n1 4 5\n2 3 10\n3 4 10' | $run
# -> 15

echo '10 9 5\n1 4 6 9 10\n1 2 3\n2 3 8\n3 4 5\n4 5 1\n5 6 2\n6 7 6\n7 8 3\n8 9 4\n9 10 1' | $run
# -> 16


6 5 2
1 6
1 2 1
5 6 1
2 4 2
4 6 3
3 4 100


'''
