'''
28473번
도로 위의 표지판 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	1024 MB	289	165	139	54.724%

문제

외판원이 된 우현이는 1번부터 N번까지 번호가 매겨진 마을을 전부 방문하기 위해, 현재 1번 마을에 도착했다.
이곳에는 서로 다른 두 마을을 잇는 M개의 도로가 있으며, 두 마을 사이에는 최대 한 개의 도로가 존재한다.
이 도로들에는 몇 가지 특이한 점이 있었는데, 하나는 도로마다 중간에 1 이상 9 이하의 숫자가 하나 적힌 표지판이 있었다는 것이고,
하나는 도로마다 통행료를 지불해야 하는데 도로를 처음 지날 때 한 번만 돈을 지불하면 된다는 것이었다.
즉, 같은 도로를 두 번 이상 지날 때는 처음 한 번만 돈을 지불해도 되는 것이다.

숫자가 적힌 표지판이 흥미로웠던 우현이는 도로를 지날 때마다 그 숫자를 핸드폰에 적어 두려고 한다.
핸드폰에 숫자를 적을 때는 커서를 원하는 곳에 두고 적을 수 있다.
즉, 현재 “321”을 써 두었고 표지판에 ‘4’가 써 있는 도로를 지났다면 “3421”, “3214” 등의 수를 만들 수 있다.
그러나 이미 지난 적이 있는 도로의 표지판 숫자는 다시 적지 않기로 했다.

그리고 돈이 많은 우현이는 통행료를 내지 못하는 경우는 없었지만, 당연히 불필요하게 돈을 더 지불하고 싶지는 않았다.
하지만 우현이는 핸드폰에 적을 수 있는 수의 최솟값이 얼마인지 궁금해졌고,
돈을 조금 더 지불하더라도 최대한 작은 수를 적고 싶었다.
우현이가 N개의 마을을 전부 방문하는 동안 핸드폰에 적을 수 있는 수의 최솟값을 구하고,
그 수를 만들기 위해서 들어가는 비용의 최솟값을 구하는 프로그램을 작성하자.

입력
첫째 줄에 마을의 수 N과 도로의 수 M이 공백으로 구분되어 주어진다.
(1 <= N <= 200,000; 1 <= M <= 500,000)

다음 M개의 줄에는 도로의 정보 x, y, z, w가 공백으로 구분되어 주어진다.
이는 x번 마을과 y번 마을이 도로로 연결되어 있고, 그 도로에는 z가 적힌 표지판이 있으며 통행료가 w원임을 의미한다.
(1 <= x, y <= N; x != y; 1 <= z <= 9; 0 <= w <= 10^6)

출력
만약 마을 N개를 전부 방문하는 것이 불가능하다면 첫째 줄에 -1을 출력한다.

만약 마을 N개를 전부 방문하는 것이 가능하다면, 첫째 줄에 마을 N개를 전부 방문할 때 핸드폰에 적을 수 있는 수의 최솟값과,
그때 지불해야 하는 비용의 최솟값을 공백으로 구분하여 출력한다.


------
5:14~6:09

문제를 두 번 풀어야 한다.

첫번째는 그냥 표지판 만 생각한다.
표지판 숫자의 총합이 최소가 되도록, 사이클 없는 트리를 만들면 된다.
트리 하나로 만들어지지 못하면 그냥 종료.
사용된 숫자들을 오름차순 정렬하면 그 수가 최소 숫자다.

두번째는 위에서 만들어진 트리를 순회하는 방법 중에서 통행료를 최소화 하는 순회 방법을 찾아야 한다.
노드간 이동 횟수는 문제가 아니다. 이건 뭔가 재귀로 풀어야 할 것 같긴 한데..
아, 통행료는 한번만 받는 다고 했으니, 트리 깊이랑 관련 있다.
아니다. 그냥 간선의 w 총합이다.

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MAX_W = int(1e6)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    roads = []
    for _ in range(M):
        # x,y,z,w = map(int, input().split())
        roads.append(tuple(map(int, input().split()))) # x 에서 y 로의 길, 표지판 z, 통행료 w
    return N,roads

def solve(N:int, roads:list[tuple[int,int,int,int]])->tuple[str,str]:
    '''
    mst 트리 구성. kruscal 알고리즘.
    '''

    # 1단계: mst 트리 생성
    # root = [ k for k in range(N+1) ]
    root = list(range(N+1))
    # 자신이 root 이면 single node tree.

    def find_root(a:int)->int:
        if root[a] == a:
            return a
        root[a] = ra = find_root(root[a])
        return ra

    # 표지판 z 기준 정렬. 만약 z가 동일할 경우 w가 작은 것 우선.
    # roads.sort(key = lambda r: (r[2],r[3]))
    roads.sort(key=lambda r: r[2]*int(1e7) + r[3])

    # log("sorted roads: %s", roads)

    sum_costs = 0 # w
    signs = [] # z

    for a,b,z,w in roads:
        ra,rb = find_root(a),find_root(b)
        if ra == rb:
            continue  # a,b are already in same tree. skip this road!
        # 이 길을 사용.
        signs.append(z)
        sum_costs += w
        # rank 신경쓰지 말고 그냥 이어 붙인다.
        root[rb] = root[b] = ra  # b,rb 를 ra 밑으로.
        if len(signs) == N-1: # 길 개수가 N-1 개 사용되면 모두 다 이어진 것임.
            break
    if len(signs) != N-1:
        return '',''  # 솔루션 없음!

    # log("signs: %s", signs)
    # signs.sort() # 이미 sort 된 z list 로 만들었으니, 굳이 필요 없을 듯.
    min_signs = ''.join(map(str, signs))

    return min_signs,str(sum_costs)


if __name__ == '__main__':
    inp = get_input()
    z,w = solve(*inp)
    if z: print(z,w)
    else: print(-1)


'''
예제 입력 1
5 7
2 3 7 10
1 2 5 20
3 1 4 30
3 5 1 15
4 2 9 50
4 5 9 35
2 5 2 40
예제 출력 1
1249 120

예제 입력 2
5 4
1 2 1 1000
2 3 2 1000
3 1 3 1000
4 5 4 1000
예제 출력 2
-1

run=(python3 28473.py)

echo '5 7\n2 3 7 10\n1 2 5 20\n3 1 4 30\n3 5 1 15\n4 2 9 50\n4 5 9 35\n2 5 2 40' | $run
echo '5 4\n1 2 1 1000\n2 3 2 1000\n3 1 3 1000\n4 5 4 1000' | $run
->
1249 120
-1


echo '2 1\n1 2 3 4' | $run
-> 3 4


# worst case 시뮬레이션

python3 28473t.py | time $run
->
-1
$run  1.03s user 0.03s system 52% cpu 2.024 total

...9999999999999 95119668
$run  0.99s user 0.03s system 54% cpu 1.895 total

아슬아슬 한데..

'''
