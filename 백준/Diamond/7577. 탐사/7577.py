'''
7577번

탐사

이 문제는 "System of Difference Constraints" 라고들 부르던데,
사실 이를 연립 부등식으로 표현할 수 있다는 게 완전하게 이해 되진 않는다.
그 부분은 제외하고 대략 벨만 포드 알고리즘으로 해를 구할 수 있을 것 같다는 느낌은 듬.
다만 음의 cost를 반드시 추가해야 하는 이유는 아직 명확하게는 모르겠음.

참고
- https://koosaga.com/72
- ...
- https://www.acmicpc.net/workbook/view/18304
  - 단순연립부등식을 벨만포드로 모델링하는 문제들



시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	1516	599	437	45.568%

문제
직선 모양의 도로에 특별한 물체가 묻혀있다. 우리는 직선구간을 탐색할 수 있는 장비를 이용해서 이 물체가 어디에 있는지를 조사하고자 한다.
직선도로를 일차원 배열로 생각해보자. 아래 그림에서 숫자는 단위 구간의 번호이며 그 안에 ▲ 기호로 표시된 것은 우리가 찾아낼 물체이다.

1	2	3	4	5	6	7	8	9	10	11	12
▲			▲	▲	▲	▲			▲
그림 1

그런데 우리는 어떤 연속된 구간에 포함되어 있는 물체의 개수를 Probe[x,y]를 이용하여 확인할 수 있다.
x부터 y까지의 구간에 물체가 r개가 있음은 Probe[x,y]=r 로 표현된다. (단 x ≤ y 이다.)
예를 들어 그림 1과 같은 상황이라면 Probe[2,7]=3, Probe[2,2]=0, Probe[6,9]=4, Probe[5,12]=5 임을 알 수 있다.

여러분은 제시된 탐사작업의 결과가 모두 만족되는 구간을 재구성하는 프로그램을 작성해야 한다.

입력
첫 줄에는 두 개의 정수 K와 N이 주어져 있다. K는 전체 구간의 길이이며, N은 조사한 Probe[x,y]=r 결과의 개수이다.
이어 나타나는 N개의 각 줄에는 하나의 탐사결과 Probe[x,y]=r 를 나타내는 세 개의 숫자 x y r이 공백문자로 분리되어 제시되어 있다.
단 입력변수에 대한 제한 범위는 다음과 같다. 3 ≤ K ≤ 40, 2 ≤ N ≤ 1,000, 1 ≤ x ≤ y ≤ K, 0 ≤ r ≤ 1,000 이다.

출력
여러분은 N개의 탐사결과를 만족하는 전체 구간을 길이 K 인 문자열로 표시해야 한다.
물체가 있는 단위 구간은 문자 ‘#’으로 표시해야 하고, 없는 단위 구간은 마이너스 기호 ‘-’로 표시해야 한다.
답이 여러 개 존재할 때에는 그 중 하나만 출력하면 된다.
만일 탐사결과를 모두 만족하는 답이 존재하지 않을 경우에는 문자열 “NONE"을 출력해야 한다.
'''




import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)



def solve_halted(K, probe:list[tuple]):
    #
    # graph[a][b] 는 a 노드, b 노드 사이의 물체의 개수.
    # 아직 알려지지 않았으면 -1
    graph = [ [-1 for _ in range(K+1)] for x in range(K+1) ]
    for k in range(K+1):
        graph[k][k] = 0
    for a,b,r in edges:
        graph[a][b] = graph[b][a] = r

    def print_graph():
        if True:
            s = f'    '
            for j in range(K+1):
                s += f'{j:2}_'
            log("%s", s)
        for i in range(K+1):
            s = f' {i:2}:'
            for j in range(K+1):
                s += ( '   ' if j<i else '.. ' if graph[i][j]<0 else f'{graph[i][j]:2} ')
            log("%s", s)

    def makeup():
        G = graph # short-cut
        changed = False
        for i in range(K): # 0 ~ K-1
            for j in range(K+1): # i+1 ~ K
                # (i,j) 가 (i,k) (k,j) 로 나뉘어 질 수 있는지 검사
                if G[i][j] < 0: # (i,j)가 아직 미확인 이면 검사 불가
                    continue
                for k in range(i+1, j): # i+1 ~ j-1
                    # if G[i][k] >= 0 and G[k][j] >= 0: # 모두 다 확인된 경우
                    #     continue
                    if G[i][k] < 0 and G[k][j] >= 0:
                        G[k][i] = G[i][k] = G[i][j] - G[k][j]
                        log("A: (%d,%d):%d  (%d,%d):%d -> (%d,%d):%d", i,j,G[i][j], k,j,G[k][j], i,k,G[i][k])
                        changed = True
                    elif G[i][k] >= 0 and G[k][j] < 0:
                        G[k][j] = G[j][k] = G[i][j] - G[i][k]
                        log("B: (%d,%d):%d  (%d,%d):%d -> (%d,%d):%d", i,j,G[i][j], i,k,G[i][k], k,j,G[k][j])
                        changed = True
                    else:
                        continue
                    # 새로 계산 된 값이 <0 이면 뭔가 문제가 발생한 것!
                    if (G[i][k] < 0 or G[k][j] < 0):
                        log("!! something wrong")
                        sys.exit(1)
        return changed

    for cnt in range(10):
        log("------------------------------ loop %d", cnt)
        changed = makeup()
        print_graph()
        if not changed:
            break

    ans = ''
    return ans



INFINITY = int(1e8)

def solve2(K, probe:list[tuple]):
    #
    # 정수 칸 대신 위치와 위치 사이 지점을 노드로 간주한다.
    # 문제에서는 1 ~ K 까지의 숫자 칸으로 설명했지만
    # 우리는 0 ~ K 까지의 노드로 관리. 그래야 그래프를 그리기 편함.
    #
    #          +-----+-----+-----+-----+---------+-----+
    #          |  1  |  2  |  3  |  4  | ...     |  K  |
    #          +-----+-----+-----+-----+---------+-----+
    #  Node   (0)---(1)---(2)---(3)---(4)- .. -(K-1)--(K)
    #
    #  Example       [  #     _  ]     Probe[2,3]=1
    #         (0)---(1)---(2)---(3)---(4)--
    #  edge            \---1---/       edge (1,3), cost 1
    #
    # 그래프로 풀기 위해, 물체의 개수를 간선에 대한 cost로 인식.
    # 방향 그래프이며 역방향은 음의 cost
    edges = []
    for x,y,r in probe:
        edges.append((x-1, y, r))
        edges.append((y, x-1, -r)) # 반드시 필요!

    # 노드 사이에는 최대 1개의 물체만 가능. 즉 최대 cost를 1로 등록
    for i in range(1, K+1): # 1~K
        edges.append((i-1, i, 1))
        edges.append((i, i-1, 0))

    min_cost = [ INFINITY for x in range(K+1) ]
    min_cost[0] = 0

    # 노드 개수가 0 부터 K 까지 총 K+1 이고,
    #  K+1 루프는 음의 사이클 감지용.
    for i in range(K+1):
        for s,e,c in edges: # start, end, cost
            if min_cost[s] == INFINITY: continue
            if min_cost[s] + c >= min_cost[e]: continue
            if i < K:
                min_cost[e] = min_cost[s] + c
            else:
                log("negative cycle!")
                return 'NONE'

    log("min_cost: %s", min_cost)
    ans = []
    for i in range(1, K + 1): # 1~K
        # 차이는 0 아니면 1 이어야 함.
        ans.append('#' if min_cost[i-1] < min_cost[i] else '-')
    return ''.join(ans)




K, N = map(int, input().split())
probe = []
# probe = [ [0] for x in range(N+1) ]  # probe[0] is not used
for _ in range(N):
    x,y,r = map(int, input().split())
    probe.append((x,y,r))
    # probe[x].append(...)

ans = solve2(K, probe)
print(ans)






'''

12 7
1 8 4
6 10 4
2 12 6
9 12 2
4 6 1
1 4 1
11 11 0
->  -#--#-####--   // 다른 그림이 나올 수 있음

echo '12 7\n1 8 4\n6 10 4\n2 12 6\n9 12 2\n4 6 1\n1 4 1\n11 11 0' | python3 7577.py

     0_ 1_ 2_ 3_ 4_ 5_ 6_ 7_ 8_ 9_10_11_12_
  0: 0  0 .. ..  1 .. .. ..  4 .. .. .. ..
  1:    0  1 ..  1 .. .. ..  4 .. .. ..  6
  2:       0  0  0 .. .. ..  3 .. .. ..  5
  3:          0  0 ..  1 ..  3 .. .. .. ..
  4:             0  1  1 ..  3 .. .. ..  5
  5:                0  0 ..  2 ..  4 ..  4
  6:                   0  1  2 ..  4 ..  4
  7:                      0  1 ..  3 ..  3
  8:                         0  1  2 ..  2
  9:                            0  1 ..  1
 10:                               0  0  0
 11:                                  0 ..
 12:                                     0



12 2
1 10 1
4 7 3

echo '12 2\n1 10 1\n4 7 3' | python3 7577.py
-> NONE


'''