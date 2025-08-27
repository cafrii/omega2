'''


10:11~10:51, backtracking with prune

이 방법은 전혀 최적화 되어 있지 않음!
N=800, K=80 만 되어도 벌써 몇 초 이상 시간이 소요됨.

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
    # 단위 시간 당 중요도가 큰 순서로 정렬.
    A.sort(key=lambda x:x[0]/x[1], reverse=True)
    log("sorted: %s", A)

    sub = [-1] * K  # study 진행 한 과목 목록
    max_prio_sum = 0

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, K+20))

    # sorting 된 상태에서의 A[]에서의 과목 index 그대로 사용
    used_flag = [0] * K

    # 백트래킹
    def back(index:int, budget:int):
        # populate sub[index].
        #  0 <= index < K
        nonlocal max_prio_sum
        # log("back[%d]: %s", index, sub[:index])

        # sub[index] 는 이 단계에서 채워야 하는 값이므로 sub[:index] 까지만 현재 유효한 데이터.
        prio_sum = sum((A[sub[k]][0] for k in range(index)), 0)
        if prio_sum > max_prio_sum: log("  prio sum: %d -> %d", max_prio_sum, prio_sum)
        max_prio_sum = max(prio_sum, max_prio_sum)

        if index >= K:
            return
        if budget <= 0:
            return
        for i in range(K):
            if used_flag[i]: continue
            p,r = A[i]

            # pruning
            # p 는 현재 선택 가능한 과목 중 가장 단위 중요도가 높은 것.
            # 이 p 로 달성 가능한 최대 중요도 합이 max 를 넘지 못하면 더 이상 진행 불필요.
            if (p / r) * budget + prio_sum < max_prio_sum:
                # log("  prune: %.2f < %d", (p / r) * budget + prio_sum, max_prio_sum)
                return
            if budget < r: continue

            sub[index] = i; used_flag[i] = 1
            back(index+1, budget - r)
            used_flag[i] = 0; sub[index] = -1
        return

    back(0, N)
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

----

run=(python3 17845.py)

echo '80 3\n650 40\n700 60\n60 40' | $run
# 710



'''
