
import sys

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
        A: subjects list. [ (prio, reqt), ... ]
            prio: priorities of each subject
            reqt: required time to study the subject
    Returns:
        sum of priorities studied with maximal case.
    '''
    K = len(A)
    MAX_TM = 10_000

    dp = [ [0]*(MAX_TM+1) for _ in range(K) ]
    # dp[k][t]:
    #  A[0] 부터 A[k] 과목들만을 고려했을 경우 주어진 시간 t에서 최대 중요도 합
    # memory:
    #  10_000 * 1_000 * sizeof(int) = 10M * sz(int) = 80M

    k = 0
    if True:
        for t in range(1, MAX_TM+1):
            prio,reqt = A[k]
            if t >= reqt:
                dp[k][t] = prio
    # k > 0
    for k in range(1, K): # 1 ~ K-1
        for t in range(1, MAX_TM+1):
            prio,reqt = A[k]
            if t >= reqt:
                dp[k][t] = max(
                    dp[k-1][t],  # 이 A[k] 과목을 선택하지 않는 경우. 중요도합 은 기존과 동일.
                    dp[k-1][t-reqt] + prio, # 과목 선택한 경우.
                )
            else:
                dp[k][t] = dp[k-1][t]
    return dp[K-1][N]

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
