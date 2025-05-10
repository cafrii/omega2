'''

백트래킹 변형으로 풀어보려고 했으나,
조기 종료 조건이 거의 효과를 발휘하지 못하여
결국 greedy search 와 비슷하게 동작하게 되어 버림.

N 이 20 만 되어도 수행 시간이 극도로 느려짐. 사용 불가!


-----------

주어진 항목 집합에서, 부분 집합을 선택하는 문제.
- 제한 조건:
    - 선택 항목들의 사용 메모리 mems[k]의 합이 M 이상이어야 함.
    - 선택 항목들의 비용 cost[k]의 합이 최소가 되어야 함.


try 1:
항목을 하나씩 늘려가면서 계산한다. mems 와 cost 합을 계속 기록해야 한다.

dp[i]
    항목이 i개 일 때 까지의 최적의 해. (mem,cost)
...
=>
dp 로 풀려고 하다가 mem cases 가 너무 방대하여, 구현이 불가!

try 2:
배낭 문제를 백트래킹 으로 푸는 것과 유사한 방법으로 시도.

=> 성능이 너무 안좋아서 실패!

'''



import sys
def log(fmt, *args): print(fmt % args, file=sys.stderr)

'''
0-1 배낭 문제를 다음과 같이 변형.
    profit -> cost
    weight -> memory

크기, 방향 등이 반대이다.
    - memory 는 일정 조건 이상이어야 하고
    - cost 는 최소화 해야 함.
'''

def solve(N:int, M:int, mems:list, costs:list) -> int:
    '''
    return minimum total cost

    '''
    assert len(mems) == N and len(costs) == N

    min_cost = 1e8 # 100*100  # minimum cost found
    bestset = []  # Best combination of items

    # global costs, mems

    # 사전 정렬. 가지치기를 하기 위해서 이 과정은 필수이다!
    # 단위 메모리당 비용 (c/m) 기준으로 정렬. 즉, 단위 이익이 높은 것 부터.
    cmr = sorted(list(zip(costs, mems)), key=lambda x: x[0]/x[1])
    costs, mems = [x[0] for x in cmr], [x[1] for x in cmr]

    log('m: %s', mems)
    log('c: %s', costs)

    selection = [False] * N  # temporary array to track selection

    def promising(j, totcost, totmem) -> bool:
        '''
        현재 항목이 최소 비용을 갱신할 가능성이 1% 라도 있는지를 검사.
        남은 모든 항목을 다 고려해도 mem 조건을 맞출 수 없거나,
          min cost 을 갱신할 수 없다면 가능성 없음.
        Args:
            j: j번째 항목이 현재 검토 중인 항목.
            totcost, totmem: 현재까지의 누적 상태.
        '''
        # 현재 조건에서 가장 최소의 비용의 조합으로 구성.
        # 일단 M을 넘지는 않게.
        while (j < N and totmem + mems[j] < M):
            totmem += mems[j]; totcost += costs[j]
            j += 1

        if j >= N: # 남은 항목을 다 더했는데도
            return False # 메모리 조건 자체를 충족하지 못하는 경우

        totcost += (M - totmem) * costs[j] / mems[j]
        return totcost < min_cost


    def step(i, cost_sum, mem_sum):
        '''
        i번째 항목에 대한 검토.
        cost_sum, mem_sum 는 현재까지 선택이 완료된 항목들의 누적 cost, mem
        '''
        log('(%d) ---- cs %d, ms %d', i, cost_sum, mem_sum)
        nonlocal min_cost, bestset # 외부 함수 solve의 변수를 갱신할 것임을 명시

        if (mem_sum >= M and cost_sum < min_cost):
            log('    min cost_sum %d, %s', cost_sum, selection)
            min_cost = cost_sum
            bestset = selection[:]

        if i >= N: return

        if promising(i, cost_sum, mem_sum):
            c, m = costs[i], mems[i]

            # case 1: 지금 이 항목을 선택하고 다음 단계로.
            selection[i] = True
            log('(%d) pick item (%d,%d)', i, c, m)
            step(i+1, cost_sum + c, mem_sum + m)

            # case 2: 이 항목 skip.
            selection[i] = False
            log('(%d) skip item (%d,%d)', i, c, m)
            step(i+1, cost_sum, mem_sum)
        else:
            log('(%d) giveup !', i) # 가지치기
        #

    # 아무 것도 선택 안된 상태에서 시작.
    step(0, 0, 0)

    return min_cost





N,M = map(int, input().split())

mems = list(map(int, input().split()))
cost = list(map(int, input().split()))
# assert len(mems) == N
# assert len(cost) == N

print(solve(N, M, mems, cost))

'''
예제 입력 1
5 60
30 10 20 35 40
3 0 3 5 4

예제 출력 1
6

echo '5 60\n30 10 20 35 40\n3 0 3 5 4' | python3 7579.py


100 100
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 20
mlist = [ randint(1,100_000) for k in range(N) ]
M = randint(1,sum(mlist))
print(N, M)
print(' '.join([ str(m) for m in mlist ]))
print(' '.join([ str(randint(0,100)) for k in range(N) ]))
EOF
) | time python3 7579.py 2> /dev/null



'''
