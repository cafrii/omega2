'''

6:23~7:09, 코딩 완료

하지만..
백트래킹으로 풀고 worst case 시험 없이 바로 제출했더니, 시간초과 탈락.
게시판 보니 dp 로들 푸는 듯 하여 dp 로 재시도함.
-> 1106.py


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
    return C,N,A

INF = int(1e9)

def solve(T:int, N:int, A:list[tuple[int,int]])->int:
    '''
    T: target profit (number of customer wanted)
    N: number of city
    A: array of (cost, profit) of each city

    cost 와 customer 가 둘 다 c 이니까 헷갈림.
    cost (비용) 과 profit (이윤) 으로 간주. 이윤을 target profit 이상 낼 수 있도록 계산.
    '''

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


if __name__ == '__main__':
    inp = get_input()
    print(solve(*inp))




'''


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
