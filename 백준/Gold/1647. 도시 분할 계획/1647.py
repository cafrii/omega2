'''
1647번
도시 분할 계획 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	38580	18408	13368	49.254%

문제
동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다.
그러다가 평화로운 마을에 가게 되었는데, 그곳에서는 알 수 없는 일이 벌어지고 있었다.

마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
길은 어느 방향으로든지 다닐 수 있는 편리한 길이다.
그리고 각 길마다 길을 유지하는데 드는 유지비가 있다.
임의의 두 집 사이에 경로가 항상 존재한다.

마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있다.
마을이 너무 커서 혼자서는 관리할 수 없기 때문이다.
마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다.
마을에는 집이 하나 이상 있어야 한다.

그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다.
일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다.
그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.
마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.
이것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다.
N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수이다.
그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수로 주어지는데
A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻이다.

임의의 두 집 사이에 경로가 항상 존재하는 입력만 주어진다.

출력
첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력한다.

-----

4:06~


일단 먼저 bf 로..
실패.
흔적은 1647a.py 에..


이게 결국 MST 문제임을 나중에 알게 됨.
20040, 사이클 게임에서 disjoint set 을 구현했었음.
각 노드들을 각각의 set 으로 한 후 하나씩 이어 가면서 키움.

kruscal 이라고 부르는 방식: 간선을 하나씩 그려가기 (각 트리를 키워가기)
prim 방식: 하나의 정점에서 mst를 키워가는 방식.

그런데 나중에는 결국, 다시 트리를 두 조각으로 분할을 해야 한다.
kruscal 은 간선을 N-2 개 까지만 이으면 된다.
prim 은 일단 mst 를 완성한 후, 다시 최대 비용 간선 하나를 제거해야 한다.
결국, 이 문제에 대해서는 prim 보다는 kruscal 이 적절하다.

'''

import sys

# def log(fmt, *args): print(fmt % args, file=sys.stderr)


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
    root = [ k for k in range(N+1) ]
    # root[k] 는 노드 k 의 root. root[0] 은 미사용.

    links.sort(key = lambda x: x[2]) # sort by cost

    num_links = 0
    sum_costs = 0

    def find_root(node:int)->int:
        # 지정한 노드가 속한 트리의 root 를 찾아서 리턴.
        if node != root[node]:
            root[node] = find_root(root[node])
            # 한번 찾아 둔 root는 root[]에 저장해 둠.
        return root[node]

    for a,b,c in links:
        if num_links >= N-2: # 두 덩어리 까지 남게 되면 종료
            break
        root_a = find_root(a)
        root_b = find_root(b)
        if root_a == root_b: # same root! it will create cycle!
            continue
        root[b] = root[root_b] = root_a  # b 를 a 밑으로. 사실 위 아래 관계는 의미 없음.
        num_links += 1
        sum_costs += c

    return sum_costs


if __name__ == '__main__':
    inp = get_input()
    print(solve_kruscal(*inp))



'''
예제 입력 1
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
예제 출력 1
8

run=(python3 1647.py)

echo '7 12\n1 2 3\n1 3 2\n3 2 1\n2 5 2\n3 4 4\n7 3 6\n5 1 5\n1 6 2\n6 4 1\n6 5 3\n4 5 3\n6 7 4' | $run
-> 8

echo '2 1\n1 2 10' | $run
-> 0

echo '3 2\n1 2 10\n2 3 100' | $run
-> 10




'''