'''
12865 평범한 배낭 문제의 다른 풀이 접근.

dp 대신 백트래킹 방식을 사용.


'''

import sys
def log(fmt, *args): print(fmt % args, file=sys.stderr)

N,W = map(int, input().split()) # num item, bag capacity

weights, profits = [], []
for _ in range(N):
    w,v = map(int, input().split())
    weights.append(w)
    profits.append(v)

# weights = list(map(int, input().split())) # weight
# profits = list(map(int, input().split())) # profit



def solve(N:int, W:int, weights:list, profits:list) -> int:
    '''
    return max profit

    Global:
        N, W, weights, profits
    '''
    assert len(weights) == N and len(profits) == N

    maxprofit = -1  # Maximum profit found
    bestset = []  # Best combination of items

    # global profits, weights

    # 사전 정렬. 가지치기를 하기 위해서 이 과정은 필수이다!
    # 단위 무게 당 이익 (p/w) 기준으로 내림차순 정렬. 즉, 단위 이익이 높은 것 부터.
    pws = sorted(list(zip(profits, weights)), key=lambda x: x[0]/x[1], reverse=True)
    profits, weights = [x[0] for x in pws], [x[1] for x in pws]

    log('w: %s', weights)
    log('p: %s', profits)

    include = [False] * N  # Temporary array to track included items

    def promising(j, profit, weight) -> bool:
        '''
        현재 항목이 최대 이익을 갱신할 가능성이 1% 라도 있는지를 검사.
        남은 모든 항목을 다 고려해도 max profit을 갱신할 수 없다면 가능성 없음.
        Args:
            j: j번째 항목이 현재 검토 중인 항목.
            profit, weight: 현재까지 가방의 누적 상태.
        '''
        if (weight > W): # 무게 초과. 가능성 없음.
            return False

        p, w = profits, weights
        # Calculate upper bound
        p_sum, w_sum = profit, weight
        # Add items greedily while weight allows
        while (j < N and w_sum + w[j] <= W):
            w_sum += w[j]; p_sum += p[j]
            j += 1
        if j < N: # Add fractional part of next item
            p_sum += (W - w_sum) * p[j] / w[j]
        return p_sum > maxprofit


    def knapsack3(i, profit_sum, weight_sum):
        '''
        배낭에 i번째 항목을 넣는 것을 검토.
        profit_sum, weight_sum 는 현재까지 배낭에 들어 있는 이익과 무게.
        '''
        log('(%d) ---- ps %d, ws %d', i, profit_sum, weight_sum)
        nonlocal maxprofit, bestset # 외부 함수 solve의 변수를 갱신할 것임을 명시

        if (weight_sum <= W and profit_sum > maxprofit):
            log('    max profit_sum %d, %s', profit_sum, include)
            maxprofit = profit_sum
            bestset = include[:]

        if i >= N: return

        if promising(i, profit_sum, weight_sum):
            p, w = profits[i], weights[i]

            # case 1: 지금 이 항목을 선택하고 다음 단계로.
            include[i] = True
            log('(%d) pick item (%d,%d)', i, p, w)
            knapsack3(i+1, profit_sum + p, weight_sum + w)

            # case 2: 이 항목 skip.
            include[i] = False
            log('(%d) skip item (%d,%d)', i, p, w)
            knapsack3(i+1, profit_sum, weight_sum)
        else:
            log('(%d) giveup !', i)
        #

    # 배낭에 아무 것도 없는 상태에서 시작.
    knapsack3(0, 0, 0)

    return maxprofit

print(solve(N, W, weights, profits))


'''
4 7
6 13
4 8
3 6
5 12

echo '4 7\n6 13\n4 8\n3 6\n5 12' | python3 12865a.py 2> /dev/null
-> 14



'''