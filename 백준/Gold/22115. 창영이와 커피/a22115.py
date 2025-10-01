'''
22115번
창영이와 커피, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	2655	1003	758	37.193%

문제
창영이는 커피를 좋아한다. 회사에 도착한 창영이는 아침 커피를 즐기려고 한다.
회사에는 N개의 커피가 각각 하나씩 준비되어 있고, 각 커피에는 카페인 함유량 Ci가 있다.
창영이는 N개의 커피 중 몇 개를 골라 정확히 K만큼의 카페인을 섭취하려고 한다.
창영이가 정확히 K만큼의 카페인을 섭취하기 위해서는 최소 몇 개의 커피를 마셔야 할까?

입력
첫째 줄에 커피의 개수 N, 창영이가 섭취해야 하는 카페인의 양 K가 주어진다.
둘째 줄에 N개 커피의 카페인 함유량 Ci가 주어진다.

출력
창영이가 K만큼의 카페인을 섭취하기 위해 마셔야 하는 커피의 최소 개수를 출력한다.
만약 정확히 K만큼의 카페인을 마실 수 없으면 -1을 출력한다.

제한
1 ≤ N ≤ 100
0 ≤ K ≤ 100,000
1 ≤ Ci ≤ 1,000

----
8:24~

이것도 배낭 문제로 접근.. 정확하게 목표를 맞춰야 한다.
맞춰야 하는 양: 카페인의 총합.
dp[c]를 관리. 카페인 총량 c를 맞출 수 있는 커피 잔 수.

dp 로 풀어서 검증 완료. 그런데 제출된 다른 풀이에 비해 시간이 꽤 걸림.
K 의 최대 값이 꽤 커서 그런 것으로 보임.

다른 방안?? 백트래킹??
백 트래킹으로 구현 해 보니, 동작을 하긴 하는데, N의 크기가 23 부터 경과 시간이 1초를 초과함.
더 나은 pruning 조건을 못찾겠음. worst case에는 2^N 번의 재귀 호출을 해야 함.

dp를 좀 더 최적화 하는 여러 방법들이 있다.
dp의 앞부분 iteration에서는 대부분의 K루프가 그냥 skip이다.
따라서 해당 c 단계에서의 의미있는 최대 k값을 미리 확인한 후, k 루프 범위를 좁혀볼 수 있다.


많이 하는 실수:
dp 1d 면 상관 없는데, dp 2d 인 경우, 또는 dual dp 인 경우, 기존 값을 복사하는 것을 잊어먹으면 안된다.


'''


import sys
def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    C = list(map(int, input().split()))
    # assert len(C) == N
    return N,K,C

def solve_dp(N:int, K:int, C:list[int])->int:
    '''
    Returns:
        min number of coffee. -1 if no answer
    '''
    MAX_V = N+1

    dp = [MAX_V] * (K+1)
    # dp[k]: 카페인 k를 맞추는 커피 최소 잔 수
    dp[0] = 0

    for c in C:
    # for i,c in enumerate(C):
        # c 만큼의 카페인이 함유된 커피 1잔.
        for k in range(K, c-1, -1):
            if dp[k-c] == MAX_V: continue
            dp[k] = min(dp[k], dp[k-c]+1)

        # log("N %d, C %d, dp %s", i, c, ' '.join(map(lambda d: str(d) if d<MAX_V else '_', dp)))

    return dp[K] if dp[K]<MAX_V else -1


def solve_dp2(N:int, K:int, C:list[int])->int:
    '''
    Returns:
        min number of coffee. -1 if no answer
    '''
    MAX_V = N+1

    dp = [MAX_V] * (K+1)
    # dp = [ [MAX_V] * (K+1) for _ in range(N) ]
    # dp[n][k]: n번째 커피잔 까지만 고려했을 때, 카페인 k를 맞추는 커피 최소 잔 수
    dp[0] = 0
    maxk = 0
    for c in C:
        # c 만큼의 카페인이 함유된 커피 1잔.
        dpx = dp.copy()
        for k in range(0, maxk+1):
            if k+c > K: continue
            dpx[k+c] = min(dp[k+c], dp[k]+1)
        maxk = min(K, maxk + c)
        dp = dpx

    return dp[K] if dp[K]<MAX_V else -1



def solve_dp3(N:int, K:int, C:list[int])->int:
    '''
    Returns:
        min number of coffee. -1 if no answer
    '''
    MAX_V = N+1

    dp = [ [MAX_V] * (K+1) for _ in range(N+1) ]
    # dp[n][k]: n번째 커피잔 까지만 고려했을 때, 카페인 k를 맞추는 커피 최소 잔 수
    maxk = 0
    dp[0][0] = 0

    for i,c in enumerate(C):
        # c 만큼의 카페인이 함유된 커피 1잔.
        dp[i+1][0] = 0
        maxk = min(K, maxk + c)
        for k in range(maxk, -1, -1): # k: maxk ~ c
            if k < c:
                dp[i+1][k] = dp[i][k]
            else:
                dp[i+1][k] = min(dp[i][k], dp[i][k-c]+1)
        # log("N %d, C %d, dp %s", i, c, ' '.join(map(lambda d: str(d) if d<MAX_V else '_', dp[i+1])))

    return dp[N][K] if dp[N][K]<MAX_V else -1


def solve_dp4(N:int, K:int, C:list[int])->int:
    '''
    Returns:
        min number of coffee. -1 if no answer
    '''
    # pre-processing.
    # 계산에 도움이 안되는 것들 제거.
    C = [ c for c in C if c <= K ]
    N = len(C)

    # edge case들 별도 처리
    if sum(C) < K: return -1
    if K == 0: return 0

    MAX_V = N+1

    dp = [MAX_V] * (K+1)
    # dp[k]: 카페인 k를 맞추는 커피 최소 잔 수
    dp[0] = 0
    # c 루프의 초기에는 대부분 k 루프는 공회전. 따라서 k 범위를 최대한 줄여주면 도움이 된다.
    maxk = 0
    for c in C:
        # c 만큼의 카페인이 함유된 커피 1잔.
        maxk = min(K, maxk+c)
        for k in range(maxk, c-1, -1):
            if dp[k-c] == MAX_V: continue
            dp[k] = min(dp[k], dp[k-c]+1)

        # log("N %d, C %d, dp %s", i, c, ' '.join(map(lambda d: str(d) if d<MAX_V else '_', dp)))

    return dp[K] if dp[K]<MAX_V else -1


def solve_dp5(N:int, K:int, C:list[int])->int:
    '''
    Returns:
        min number of coffee. -1 if no answer
    '''
    # pre-processing.
    # 계산에 도움이 안되는 것들 제거.
    C = [ c for c in C if c <= K ]
    N = len(C)

    # edge case들 별도 처리
    if sum(C) < K: return -1
    if K == 0: return 0

    MAX_V = N+1

    dp = [MAX_V] * (K+1)
    # dp[k]: 카페인 k를 맞추는 커피 최소 잔 수
    dp[0] = 0
    # c 루프의 초기에는 대부분 k 루프는 공회전. 따라서 k 범위를 최대한 줄여주면 도움이 된다.
    maxk = 0
    for c in C:
        # c 만큼의 카페인이 함유된 커피 1잔.
        maxk = min(K, maxk+c)
        for k in range(maxk, c-1, -1):
            dp[k] = min(dp[k], dp[k-c]+1)

    return dp[K] if dp[K]<MAX_V else -1



def solve_bt(N:int, K:int, C:list[int])->int:
    '''
    using backtracking
    동작을 하긴 하는데, N의 크기가 23 부터 경과 시간이 1초를 초과함.
    '''
    C.sort(reverse=True)

    MAX_CUPS = N+1
    min_cups = MAX_CUPS

    used = [0]*N

    def back(index:int, num_used:int, caffsum:int)->bool:
        '''
        Args:
            cup index: 0 ~ N-1
            caffsum: total accumulated caffein amount
        '''
        nonlocal min_cups

        if caffsum == K:
            min_cups = min(min_cups, num_used)
            return True

        if index >= N:
            # return True if caffsum == K else False
            return False

        # prunning, early drop
        if num_used >= min_cups:
            return False

        # used case
        if caffsum + C[index] <= K:
            used[index] = 1
            back(index+1, num_used+1, caffsum + C[index])
            used[index] = 0

        # not-used case
        back(index+1, num_used, caffsum)

    back(0, 0, 0)
    return min_cups if min_cups <= N else -1


if __name__ == '__main__':
    # log("sys.argv: %s", sys.argv)
    if len(sys.argv)>=2:
        inp = get_input()
        if sys.argv[1] == 'dp': print(solve_dp3(*inp))
        if sys.argv[1] == 'bt': print(solve_bt(*inp))
        sys.exit(0)

    print(solve_dp4(*get_input()))




'''
예제 입력 1
4 5
1 1 3 2
예제 출력 1
2
예제 입력 2
5 5
1 1 3 2 5
예제 출력 2
1
예제 입력 3
5 7
1 1 1 1 1
예제 출력 3
-1

----
run=(python3 a22115.py)

echo '4 5\n1 1 3 2' | $run
# 2
echo '5 5\n1 1 3 2 5' | $run
# 1
echo '5 7\n1 1 1 1 1' | $run
# -1


echo '1 9\n9' | $run
# 1
echo '1 0\n3' | $run
# 0
echo '1 1\n3' | $run
# -1

echo '100 860\n208 903 160 503 452 462 270 42 202 45 789 888 519 38 111 541 753 268 538 825 770 526 818 968 882 366 785 200 928 728 219 512 340 833 459 962 906 56 255 813 384 468 173 163 199 8 826 67 58 508 784 729 796 496 981 253 810 380 952 209 786 865 490 601 897 145 379 739 795 579 485 44 622 231 519 139 551 520 168 735 393 493 798 160 881 694 476 419 545 461 798 444 189 458 12 351 722 866 908 773' | $run
# 2

'''


import time,os
import subprocess,sys,os
from random import seed,randint,shuffle

# worst-case test
def gen_max_input():
    N = int(os.getenv('_N', '100'))
    K = int(os.getenv('_K', '100000'))
    A = [ randint(1,1000) for n in range(N) ]
    return N,K,A

def test_worst():
    # seed(time.time())
    seed(43)
    inp = gen_max_input()
    print(solve_bt(*inp))


# compare test
def gen_random_input():
    maxN = int(os.getenv('_N', '10'))
    # N = randint(1, maxN)
    N = maxN
    # K = randint(0, int(os.getenv('_K', '100000')))
    max_c = 1000 # max caffein per cup
    A = [ randint(1,max_c) for n in range(N) ]
    sum_c = sum(A)
    K = randint(0, int(sum_c * 1.2))
    K = min(K, 100000)
    return N,K,A

def test_compare():
    # seed(time.time())
    s = os.getenv("_SEED", "43")
    seed(int(s)) if s.isdigit() else seed(time.time())

    T = int(os.getenv("_T", "10"))
    for i in range(T):
        log(f'**** {i}/{T}')
        N,K,A = gen_random_input()
        log("inputs: %d, %d, %s", N, K, A)
        A1,A2 = A.copy(),A.copy() # solve_xx() might modify objects.

        tm = []
        tm.append(time.perf_counter()*1000)
        r1 = solve_dp4(N,K,A1)
        tm.append(time.perf_counter()*1000)
        # r2 = solve_bt(N,K,A2)
        r2 = solve_dp5(N,K,A2)
        tm.append(time.perf_counter()*1000)
        tm = [ tm[k]-tm[k-1] for k in range(1,len(tm)) ] # clock to interval

        if r1 != r2:
            print(f'assert failed!')
            print(f'inp: == {N} {K} {A}==')
            print(f'out1: ** {r1} **')
            print(f'out2: ** {r2} **')
            assert False, "answer mismatch"
        log("==== ok, same.. answer %d, elapsed: %d %d (ms)", r1, tm[0], tm[1])
    log('done')

'''
_N=100 _M=300 python3 -c "from a22115 import test_worst; test_worst()"

_T=1 python3 -c "from a22115 import test_compare; test_compare()"

_SEED=x _N=100 _T=50 python3 -c "from a22115 import test_compare; test_compare()"

'''
