'''
1106번
호텔

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	18175	7073	5339	38.366%

문제

세계적인 호텔인 형택 호텔의 사장인 김형택은 이번에 수입을 조금 늘리기 위해서 홍보를 하려고 한다.

형택이가 홍보를 할 수 있는 도시가 주어지고, 각 도시별로 홍보하는데 드는 비용과,
그 때 몇 명의 호텔 고객이 늘어나는지에 대한 정보가 있다.

예를 들어, “어떤 도시에서 9원을 들여서 홍보하면 3명의 고객이 늘어난다.”와 같은 정보이다.
이때, 이러한 정보에 나타난 돈에 정수배 만큼을 투자할 수 있다.
즉, 9원을 들여서 3명의 고객, 18원을 들여서 6명의 고객, 27원을 들여서 9명의 고객을 늘어나게 할 수 있지만,
3원을 들여서 홍보해서 1명의 고객, 12원을 들여서 4명의 고객을 늘어나게 할 수는 없다.

각 도시에는 무한 명의 잠재적인 고객이 있다.
이때, 호텔의 고객을 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 C와 형택이가 홍보할 수 있는 도시의 개수 N이 주어진다.
C는 1,000보다 작거나 같은 자연수이고, N은 20보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 각 도시에서 홍보할 때 대는 비용과
그 비용으로 얻을 수 있는 고객의 수가 주어진다.
이 값은 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def get_input():
    input = sys.stdin.readline
    C,N = map(int, input().split())
    # C: 1~1000, N:1~20
    A = []
    # A: cost/profit info of all city
    for _ in range(N):
        c,p = map(int, input().split()) # cost, profit
        A.append((c, p))
    return C,A


INF = int(1e9)

def solve_backtrack(T:int, A:list[tuple[int,int]])->int:
    '''
    T: target profit (number of customer wanted)
    N: number of city
    A: array of (cost, profit) of each city

    cost 와 customer 가 둘 다 c 이니까 헷갈림.
    cost (비용) 과 profit (이윤) 으로 간주. 이윤을 target profit 이상 낼 수 있도록 계산.
    '''
    N = len(A)
    min_cost = INF
    # 최소 비용을 투자하려면 cost/profit ratio를 오름차순으로 정렬

    # invest plan
    A1 = [ [c/p,n,c,p] for n,(c,p) in enumerate(A) ]
    #  [ cost_ratio, city, cost, profit ]
    A1.sort()
    log("A1: %s", A1)

    plan = [ [n,0] for r,n,c,p in A1 ]
    #  [ city, invest_unit ]


    def populate(idx:int, target_profit:int):
        nonlocal min_cost

        if target_profit <= 0: # 더 이상 시도 불필요.
            # 지금까지 투자 총액 계산 후 종료
            total_cost = sum([ A1[k][2] * plan[k][1] for k in range(idx) ])
            min_cost = min(min_cost, total_cost)
            log("        [%d] min cost: -> %d, %s", idx, min_cost, plan[:idx])
            return True
        if idx >= N:
            log("        [%d] cannot be an answer, %s", idx, plan[:idx])
            return False

        _,city,c,p = A1[idx]
        # log("[%d] city %d", idx, city)

        # ratio 순으로 투자하고 있으므로, 각 단계에서 할 수 있는 최대한의 투자 시도.
        invest = (target_profit + p-1) // p

        # pruning: optimal cost 가 이미 최소값을 넘어서면 이른 포기.
        opt_cost = target_profit / p * c
        if opt_cost > min_cost:
            log("[%d] early drop", idx)
            return False

        log("[%d] target %d, c %d, p %d, %s", idx, target_profit, c, p, plan[:idx])

        for i in range(invest,-1,-1):

            plan[idx][1] = i
            remain_profit = target_profit - i*p
            if remain_profit < 0:
                remain_profit = 0

            log("  [%d] city %d, invest %d, remain %d", idx, city, i, remain_profit)
            res = populate(idx+1, remain_profit)
            if not res:
                break

        return True

    populate(0, T)

    return min_cost


def solve_dp(T:int, A:list[tuple[int,int]])->int:
    '''
    T: target profit (number of extra customer wanted)
    A: array of (cost, profit) of each city

    cost 와 customer 가 둘 다 c 이니까 헷갈림.
    cost (비용) 과 profit (이윤) 으로 간주. 이윤을 target profit 이상 낼 수 있도록 계산.

    T <= 1000
    N <= 20
    '''
    N = len(A)
    max_profit = max(p for c,p in A)

    log("T %d, maxp %d, %s", T, max_profit, A)

    dp = [ INF ] * (T + max_profit + 1)
    # dp[k]: k 명의 고객 (profit) 을 얻기 위한 최소 비용
    dp[0] = 0

    for i in range(N):
        cost, profit = A[i]
        log("(%d) cost %d, profit %d", i, cost, profit)

        for j in range(profit, T+profit):
            if dp[j-profit] >= INF: continue

            dp[j] = min(dp[j], dp[j-profit] + cost)

            '''
            j == 0
            for k in range(0, T//profit+1):
                dp[k*profit] = min(*, dp[0] + k*cost)
                # dp[]  0, p, 2p, 3p, 4p, .., T
                k==0
                    dp[0] = min(dp[0], dp[0])
                k==1
                    dp[profit] = min(dp[profit], dp[0] + cost)
                k==2
                    dp[2*profit] = min(dp[2*profit], dp[0] + 2*cost)
            j == 1
            '''

        log("    %s", ','.join([ (str(dp[k]) if dp[k]<INF else '-') for k in range(T+profit) ]) )

    return min(dp[T:])




if __name__ == '__main__':
    inp = get_input()
    # print(solve_backtrack(*inp))
    print(solve_dp(*inp))




'''

12 2
3 5  # cost 3, profit 5
1 2

-------------------------- 12

dp[0]  = 0     0
dp[1]  = INF      .
dp[2]  = INF   1
dp[3]  = INF      .
dp[4]  = INF   2
dp[5]  = 3
dp[6]  = INF   3
dp[7]  = INF
dp[8]  = INF   4
dp[9]  = INF
dp[10] = 6     5
dp[11] = INF

dp[12] = INF   6
dp[13] = INF
dp[14] = INF   7
dp[15] = 9


----------

예제 입력 1
12 2
3 5
1 1
예제 출력 1
8

예제 입력 2
10 3
3 1
2 2
1 3
예제 출력 2
4

예제 입력 3
10 10
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
예제 출력 3
10

예제 입력 4
100 6
4 9
9 11
3 4
8 7
1 2
9 8
예제 출력 4
45


run=(python3 1106.py)

echo '12 2\n3 5\n1 1' | $run
echo '10 3\n3 1\n2 2\n1 3' | $run
echo '10 10\n1 1\n2 2\n3 3\n4 4\n5 5\n6 6\n7 7\n8 8\n9 9\n10 10' | $run
echo '100 6\n4 9\n9 11\n3 4\n8 7\n1 2\n9 8' | $run
->
8
4
10
45

'''
