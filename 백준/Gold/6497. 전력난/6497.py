'''
6497번
전력난 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	22303	8551	6445	35.574%

문제
성진이는 한 도시의 시장인데 거지라서 전력난에 끙끙댄다.
그래서 모든 길마다 원래 켜져 있던 가로등 중 일부를 소등하기로 하였다.
길의 가로등을 켜 두면 하루에 길의 미터 수만큼 돈이 들어가는데, 일부를 소등하여 그만큼의 돈을 절약할 수 있다.

그러나 만약 어떤 두 집을 왕래할 때, 불이 켜져 있지 않은 길을 반드시 지나야 한다면 위험하다.
그래서 도시에 있는 모든 두 집 쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있어야 한다.

위 조건을 지키면서 절약할 수 있는 최대 액수를 구하시오.

입력
입력은 여러 개의 테스트 케이스로 구분되어 있다.

각 테스트 케이스의 첫째 줄에는 집의 수 m과 길의 수 n이 주어진다.
(1 ≤ m ≤ 200000, m-1 ≤ n ≤ 200000)

이어서 n개의 줄에 각 길에 대한 정보 x, y, z가 주어지는데,
이는 x번 집과 y번 집 사이에 양방향 도로가 있으며 그 거리가 z미터라는 뜻이다.
(0 ≤ x, y < m, x ≠ y)

도시는 항상 연결 그래프의 형태이고(즉, 어떤 두 집을 골라도 서로 왕래할 수 있는 경로가 있다),
도시상의 모든 길의 거리 합은 2^31미터보다 작다.

입력의 끝에서는 첫 줄에 0이 2개 주어진다.

출력
각 테스트 케이스마다 한 줄에 걸쳐 절약할 수 있는 최대 비용을 출력한다.

----------

10:15~10:35

알고리즘: 최소 스패닝 트리, kruscal

비용 절감을 최대로 해야 한다.
최소 비용의 그래프를 구하면, 이 그래프에 속하지 않은 간선들은 모두 절감 대상이다.
즉 그래프에 속하지 않은 간선의 cost 의 총합이 곧 최대 비용 절감이 된다.

1. 최소 비용의 그래프 구하기
- minimum spanning tree 문제가 된다.
- 최대 노드 수와 최대 간선의 수가 같으니, kruscal 이 더 유리하다.

2. 절감 비용 구하기
- (1) mst 를 구축해 가면서, 트리에 소속된 간선의 비용(distance) 총합을 구할 수 있다.
- 이 도시 전체의 총 비용을 구한 후 앞서 구한 소속 간선 비용 합을 빼면 절감 비용이 된다.
- (2) 또는, mst 구성이 완성된 이후 loop exit 하지 않고 계속 진행하면서 절감 비용 합을 구할 수도 있다.
- 비교:
  - (1)은 전체 비용 합을 구하기 위해 별도의 for loop을 사용하니, 두 번의 for loop,
  - (2)는 한번의 loop를 쓰지만 loop 안에 조건문이 더 많아진다.

- 다 제출해 보았는데, 예상과 달리 1번이 제일 빨랐음.

97271798 cafrii  6497 맞았습니다!! 86052KB  824ms Python 3 1397B (1)
97272165 cafrii  6497 맞았습니다!! 86052KB 1080ms Python 3 1267B (2)
97283230 cafrii  6497 맞았습니다!! 86052KB 1112ms Python 3 1373B (2) 추가수정


'''



import sys
# from heapq import heappush, heappop

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    # return generator
    input = sys.stdin.readline
    while True:
        m,n = map(int, input().split())
        if m == 0:
            break
        edges = []
        for _ in range(n):
            edges.append(tuple(map(int, input().split())))
        yield m,edges  # number of houses, edges
    return

def solve(m:int, edges:list[tuple[int,int,int]])->int:
    '''
    Arguments:
        m: number of houses
        1 ≤ m ≤ 200_000, m-1 ≤ n ≤ 200_000
        edges: list of tuple(i,j,d) distance d between house i and j.
    Returns:
        max savings possible
    '''

    roots = list(range(m))

    def find_root(a:int)->int:
        if roots[a] == a: return a
        stack = []
        while roots[a] != a:
            stack.append(a)
            a = roots[a]
        for k in stack: roots[k] = a
        return a

    edges.sort(key=lambda x: x[2]) # sort by distance, ascending

    total_cost = sum(k for i,j,k in edges)
    num_roads, opt_cost = 0,0

    for a,b,dist in edges:
        ra,rb = find_root(a),find_root(b)
        if ra == rb: continue

        # make union
        roots[rb] = roots[b] = ra
        num_roads += 1
        opt_cost += dist
        if num_roads >= m-1:
            break
    return total_cost - opt_cost

if __name__ == '__main__':
    it = get_input()
    for m,edges in it:
        r = solve(m, edges)
        print(r)


'''
예제 입력 1
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
0 0
예제 출력 1
51

run=(python3 6497.py)

echo '7 11\n0 1 7\n0 3 5\n1 2 8\n1 3 9\n1 4 7\n2 4 5\n3 4 15\n3 5 6\n4 5 8\n4 6 9\n5 6 11\n0 0' | $run
-> 51

echo '7 11\n0 1 7\n0 3 5\n1 2 8\n1 3 9\n1 4 7\n2 4 5\n3 4 15\n3 5 6\n4 5 8\n4 6 9\n5 6 11\n7 11\n0 1 7\n0 3 5\n1 2 8\n1 3 9\n1 4 7\n2 4 5\n3 4 15\n3 5 6\n4 5 8\n4 6 9\n5 6 11\n0 0' | $run
->
51
51


'''

