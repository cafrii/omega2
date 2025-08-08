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

