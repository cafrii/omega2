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

def solve_dp_sm(T:int, A:list[tuple[int,int]])->int:
    '''
    Args:
        T: max total allowed time to study
        A: subjects list. [ (prio, reqt), ... ]
            prio: priorities of each subject
            reqt: required time to study the subject
    Returns:
        sum of priorities studied with maximal case.
    '''
    K = len(A)
    dp = [0]*(T+1)
    # dp[k]: A[0] 부터 A[k] 과목들만을 고려했을 경우 주어진 시간 t 에서 최대 중요도 합

    for prio,reqt in A:
        if reqt > T: continue
        # iterate reverse way
        for t in range(T, reqt-1, -1):  # T ... reqt
            dp[t] = max(
                dp[t],  # 이 A[k] 과목을 선택하지 않는 경우. 중요도합 은 기존과 동일.
                dp[t-reqt] + prio, # 이 과목 선택한 경우.
            )
    return dp[T]

if __name__ == '__main__':
    inp = get_input()
    r = solve_dp_sm(*inp)
    print(r)

