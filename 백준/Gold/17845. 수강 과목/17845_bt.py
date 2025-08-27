'''

백트래킹의 좀 다른 방향으로의 접근.

채우기 방식이 아니라, 선택하기 방식으로 접근한다.
채우기는 O(K!), 선택하기는 O(2**K) 가 될 듯.

결과
기존 백트래킹 보다는 훨씬 빨라짐.
하지만, 제출하면 시간 초과 발생하여 실패.
어떤 입력 시퀀스에서 그런지는 아직 모름.

pypy3 로 해도 14% 채점 중 시간 초과.

promising() 함수 호출 부분을 막으면, 당연히 N=200 만 되어도 시간이 엄청 오래 걸림.
어떤 특정한 조건에서 promising() 이 항상 true처럼 보이는 어떤 조건이 있는 듯 함.

결론
배낭 문제는 백트래킹은 쓰지 말고 무조건 dp로 풀어야 한다.

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

'''
study time: 1 ≤ N ≤ 10_000
subject:    1 ≤ K ≤ 1_000
'''

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    # for each subject
    A = [] # (priority, required_time)
    for _ in range(K):
        p,r = map(int, input().split())
        A.append((p, r))
    return N,A

def solve(N:int, A:list[tuple[int,int]])->int:
    '''
    Args:
        N: max total allowed time to study
        prio: priorities of each subject
        reqt: required time to study the subject
    Returns:
        sum of priorities studied with maximal case.
    '''
    K = len(A)

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, K+20))

    # 단위 시간 당 중요도가 큰 순서로 정렬.
    A.sort(key=lambda x:x[0]/x[1], reverse=True)
    log("sorted: %s", A)

    # sorting 된 상태에서의 A[]에서의 과목 index 그대로 사용.
    # 이 과목의 공부를 할 것인지 여부. 1 이면 study!
    studied = [0] * K

    max_prio_sum = 0

    def promising(index:int, prio:int, budget:int)->bool:
        '''
            index 번째 과목에서부터 가능성 검사. 향후 계속 진행하는 것이 의미 있는지를 체크.
            prio: 지금까지의 누적 중요도 (priority sum)
            budget: 현재 남은 가용 시간
        '''
        if budget < 0: return False
        j = index # 가능한 j 는 0 ~ K-1
        tot_prio = float(prio)
        while j < K and budget - A[j][1] >= 0:
            tot_prio += A[j][0]
            budget -= A[j][1]
            j += 1
        if j < K: # 이론적인 상한 계산
            tot_prio += (budget * A[j][0] / A[j][1])
        return tot_prio > max_prio_sum


    def back(index:int, pr_sum:int, budget:int):
        '''
            backtracking
            decide studied[index] with 0 or 1 (0 <= index < K)
            update max_prio_sum (index <= K)
        Args:
            pr_sum: priority sum from subject[0] until subject[index-1]
            budget: remaining budget (time)
        '''
        nonlocal max_prio_sum
        log("back[%d]: %s", index, studied[:index])
        # log("back[%d]:", index)

        if budget >= 0 and pr_sum > max_prio_sum: # update max_prio
            log("  prio sum: %d -> %d", max_prio_sum, pr_sum)
            max_prio_sum = pr_sum

        if index >= K: return
        # if not promising(index, pr_sum, budget):
        #     # log("  pruned")
        #     return

        studied[index] = 1
        back(index + 1, pr_sum + A[index][0], budget - A[index][1])
        studied[index] = 0
        back(index + 1, pr_sum, budget)
        return

    back(0, 0, N) # starting from subject[0], zero pr_sum, full budget
    return max_prio_sum


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)


'''
예제 입력 1
80 3
650 40
700 60
60 40
예제 출력 1
710


run=(python3 17845_bt.py)

echo '80 3\n650 40\n700 60\n60 40' | $run

----

export _N=10000

(python3 <<EOF
import time, os
from random import seed,randint
# seed(time.time())
seed(43)
N = int(os.getenv('_N','100'))
K = N // 10
print(N,K)
for _ in range(K):
    # print(randint(1,100),randint(1,max(N//K,4)))
    print(randint(1,100),1)
EOF
) | time $run



'''
