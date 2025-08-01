'''
1922번
네트워크 연결 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	41769	27348	17801	65.652%

문제
도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다.
하지만 아쉽게도 허브가 있지 않아 컴퓨터와 컴퓨터를 직접 연결하여야 한다.
그런데 모두가 자료를 공유하기 위해서는 모든 컴퓨터가 연결이 되어 있어야 한다.
(a와 b가 연결이 되어 있다는 말은 a에서 b로의 경로가 존재한다는 것을 의미한다.
a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다.)

그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하여야
컴퓨터를 연결하는 비용 외에 다른 곳에 돈을 더 쓸 수 있을 것이다.
이제 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때
모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라.
모든 컴퓨터를 연결할 수 없는 경우는 없다.

입력
첫째 줄에 컴퓨터의 수 N (1 ≤ N ≤ 1000)가 주어진다.

둘째 줄에는 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)가 주어진다.

셋째 줄부터 M+2번째 줄까지 총 M개의 줄에 각 컴퓨터를 연결하는데 드는 비용이 주어진다.
이 비용의 정보는 세 개의 정수로 주어지는데,
만약에 a b c 가 주어져 있다고 하면 a컴퓨터와 b컴퓨터를 연결하는데 비용이 c (1 ≤ c ≤ 10,000) 만큼 든다는 것을 의미한다.
a와 b는 같을 수도 있다.

출력
모든 컴퓨터를 연결하는데 필요한 최소비용을 첫째 줄에 출력한다.


--------

9:13~9:23

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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


'''
예제 입력 1
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
예제 출력 1
23


run=(python3 1922.py)

echo '6\n9\n1 2 5\n1 3 4\n2 3 2\n2 4 7\n3 4 6\n3 5 11\n4 5 3\n4 6 8\n5 6 8' | $run
# -> 23

echo '1\n1\n1 1 10' | $run
# -> 0
echo '1\n2\n1 1 10\n1 1 20' | $run
# -> 0
echo '1\n2\n1 1 10\n1 1 20' | $run

echo '2\n2\n1 2 10\n2 1 20' | $run
# -> 10




'''