'''
17845번
수강 과목 성공다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	3599	2259	1884	62.863%

문제
유니스트 컴퓨터공학과에 다니는 서윤이는 이번에 어떤 과목을 들을지 고민중이다.
학점을 잘 받을 수 있으면서도 중요한 과목을 듣고 싶은 서윤이는 모든 과목의 중요도와,
일정 이상의 학점을 받기 위해 필요한 공부시간을 다 적었다.

처음에는 모든 과목을 들으려고 했던 서윤이는 자신의 공부 시간에 한계가 있다는 것을 깨달았다.
그래서, 공부 시간의 한계를 초과하지 않으면서 과목의 중요도 합이 최대가 되도록 몇 개만 선택하여 수강하기로 마음먹었다.

중요도가 최대가 되도록 과목을 선택했을 때, 최대가 되는 중요도를 출력하는 프로그램을 작성하시오.

입력
첫줄에 서윤이의 최대 공부시간 N (1 ≤ N ≤ 10,000), 과목 수 K (1 ≤ K ≤ 1,000)이 공백을 사이에 두고 주어진다.

이후 K개의 줄에 중요도 I (1 ≤ I ≤ 100,000), 필요한 공부시간 (1 ≤ T ≤ 10,000)이 공백을 사이에 두고 주어진다.

출력
얻을 수 있는 최대 중요도를 출력한다.

----------

처음에는 backtracking 으로 구현. 채워넣기 방식.
그러나 자체 시뮬레이션 수행하니 N,K가 커질 경우 너무 느려서 사용 불가. 제출 안하고 포기.
-> 17845_bt0.py

같은 backtracking 인데, 채워넣기 대신 자리 선택 (토글) 방식으로 재구현.
자체 시뮬레이션으로는 큰 문제 발견이 안되었음.
그런데 제출했는데 시간 초과 실패.
-> 17845_bt.py

dp 로 구현
처음에는 dp-2d 로 구현 먼저.
제출 후 일단 통과. 수행 시간이 오래 걸렸으나 python 배려로 패스 한 듯.

그 다음 모범 답안들 참고해서 dp 1d 로 개선.
시간 단축은 되는데, 랭크 최고점 과는 약간 차이가 남.

기록
97430260 cube2848    17845 맞았습니다!!  33432 KB   832 ms  Python 3 436B
94030237 qjaxoddl522 17845 맞았습니다!!  35560 KB   864 ms  Python 3 417B
87423709 ssoulistic  17845 맞았습니다!!  33432 KB   688 ms  Python 3 328B   <- 최고 속도.
97879570 cafrii      17845 맞았습니다!!  33432 KB   832 ms  Python 3 1201B
97878001 cafrii      17845 맞았습니다!! 401312 KB  2368 ms  Python 3 1554B


--------
아래는 아이디어 스케치.


dp = [ [0,0] for _ in range(K) ]
dp[k]: [max_prio_sum, study_time]
        A[0] 부터 A[k] 과목들만을 고려했을 경우 최대 중요도 합과 그 때의 누적 공부 시간

dp[k] 는 dp[k-1], dp[k-2], dp[k-3], ... 등 이전 결과들 중에서
여유 시간이 A[k][2] 이상 남아 있는 것들에 대해 모두 A[k]를 적용해 본 후, 최대 중요도가 나온 것을 선택하는 것.

하지만 이런 식으로 dp 구현이 가능할까?
dp[k] 계산 단계에서, dp[j] (j<k) 가 아쉽게 계산 후보에 포함되지 못했다고 해 보자.
dp[i] (i != j) 들에 대해서만 계산을 할 텐데,
어쩌면 최대 중요도는 dp[j] 구성에서 아주 작은 과목 하나만 뺀 것일 수도 있다.
dp[j] 구성에서 과목 하나만 뺀 구성이 dp[i]에 존재한다고 보장할 수는 없다.

뭔가 정렬된 조건 등이 필요해 보인다.
만약 A 가 단위 시간당 중요도 순으로 정렬되어 있다면 어떻게 달라지는가?

-----------
다른 dp 풀이 방안
N 값을 하나씩 늘려가 보기?

-----------
2차원 dp 로 풀어야 할 듯..
dp[k][time]

결국 다시 1차원 dp의 반복 업데이트 형태로 개선됨.
dp[time]

-----------


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


def solve_dp(N:int, A:list[tuple[int,int]])->int:
    '''
    2차원 dp 초기 구현 버전.

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



def solve_dp_sm(T:int, A:list[tuple[int,int]])->int:
    '''
    small memory optimized
        dp[k] 를 계산할 때, dp[k-1] 만 사용하고 그 이전의 dp[k-2].. 등은 사용하지 않음.
        따라서 전체 dp[k][t] 를 다 저장하고 있을 필요가 없음.

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
    # r = solve_dp(*inp)
    r = solve_dp_sm(*inp)
    print(r)


'''
예제 입력 1
80 3
650 40
700 60
60 40
예제 출력 1
710


run=(python3 17845.py)

echo '80 3\n650 40\n700 60\n60 40' | $run
# 710


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

# 49070
$run  1.14s user 0.06s system 99% cpu 1.207 total
# run with dp (original)

# 49070
$run  0.65s user 0.01s system 99% cpu 0.662 total
# run with dp_sm

'''
