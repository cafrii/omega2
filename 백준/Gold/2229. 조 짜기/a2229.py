'''
2229번
조 짜기, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	4865	3095	2417	64.730%

문제
알고스팟 캠프에 N(1 ≤ N ≤ 1,000)명의 학생들이 참여하였다.
학생들은 열심히 공부를 하고 있었는데, 어느 날 조별 수업을 진행하기로 하였다.
조별 수업의 목적은 잘 하는 학생들과 덜 잘 하는 학생들을 같은 조로 묶어서
서로 자극을 받으며 공부하도록 만들기 위함이다.
따라서 가급적이면 실력 차이가 많이 나도록 조를 편성하는 것이 유리하다.

하지만 조를 편성할 때 같은 조에 속하게 된 학생들의 나이 차이가 많이 날 경우에는
오히려 부정적인 효과가 나타날 수도 있다.
따라서 선생님들은 우선 학생들을 나이 순서대로 정렬한 다음에,
적당히 학생들을 나누는 방식으로 조를 짜기로 하였다. 조의 개수는 상관이 없다.

각각의 조가 잘 짜여진 정도는 그 조에 속해있는 가장 점수가 높은 학생의 점수와
가장 점수가 낮은 학생의 점수의 차이가 된다.
또한 전체적으로 조가 잘 짜여진 정도는, 각각의 조가 잘 짜여진 정도의 합으로 나타난다.
한 명으로 조가 구성되는 경우에는 그 조의 잘 짜여진 정도가 0이 된다.
(가장 높은 점수와 가장 낮은 점수가 같으므로).

학생들의 점수가 주어졌을 때, 조가 잘 짜여진 정도의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 다음 줄에는 N명의 학생들의 점수가 나이 순서대로 주어진다.
각 학생의 점수는 0 이상 10,000 이하의 정수이다.

출력
첫째 줄에 답을 출력한다.

-----


1차: 9/9, 10:46~
9/10 상태: 구현한 코드가 답은 제대로 내는 듯 한데, worst case 시간 초과가 됨.
너무 늦으니, 이 구현으로는 안될 듯 함.


---


A1 A2 A3 .. Ak-1 Ak Ak+1 Ak+2

A1 A2 A3 .. Ak-2 Ak-1 까지의 최대 점수: X
거기에 새롭게 Ak 를 추가한 경우,
Ak-1 을 Ak 와 묶는 경우
Ak-2 Ak-1 Ak 와 묶는 경우
Ak-3 Ak-2 Ak-1 Ak 와 묶는 경우
...


A1 A2
      A3 추가 할 때..
(A1 A2) (A3) 기존과 동일
(A1) (A2 A3)
(A1 A2 A3)

A1 A2 A3
         A4 추가
(A1 A2 A3) (A4)
A1 A2  (A3 A4)
A1 (A2 A3 A4)
(A1 A2 A3 A4)

dp[1][4] 를 구하려면
dp[1][3], dp[1][2] 를 알아야 하고,
동시에
dp[3][4], dp[2][4] 도 알아야 한다.

  1  2  3  4  5
1 o  o  o  o  o
2    o        o
3       o     o
4          o  o
5             o

2차원 dp 이다.

----
## 9/14 개선 작업

분할점으로서의 의미가 없는 경우를 제거하는 작업에 집중하기로 한다.
dp[k][k+j]: 학생 k부터 k+j까지만 고려했을 때의 최대 점수

3 5 7 9 라면
    (3 5 7 9)
    (3) (5 7 9)
    (3 5) (7 9)
    (3 5 7) (9)
(3) 이나 (9) 와 같이 단독 구성하면 그냥 0점 이므로 그냥 버려지는 것과 동일.
따라서 양 끝은 항상 조를 구성하는 것이 유리해 보일 수 있다. 하지만..

3 2 9 8 인 경우
    (3 2 9 8) -> 5점
    (3 2) (9 8) -> 2점
    (3) (2 9) (8) -> 7점
    ...
경우에 따라서는 양쪽 끝을 버리는 것이 최적일 수도 있다. 즉, 앞의 가설은 틀림.

증가, 감소 형태로 구분해 보자.
계속 증가하는 형태라면 항상 양 끝을 포함한 하나의 조 구성이 유리.
2 4 5 8 이라면 6점이 최고.

단조 증가라면?
2 4 4 4 4 7 -> 5점. 역시 마찬가지로 하나의 조 구성이 유리.

자, 이제 증가 + 감소 형태를 보자.
2 3 5 4 1
당연히 한 조 구성은 정답은 아니다. 증가 부분과 감소 부분을 분리. 증감 전환점을 어느 쪽에 포함시킬지 선택 필요.
    (2 3 5) (4 1) -> 3+3=6
    (2 3) (5 4 1) -> 1+4=5
전환점을 어느쪽에 포함시키느냐에 따라 점수가 달라진다.

### 전략
주어진 점수들의 증감 추이를 검사. 전환점을 기준으로 조 분리.
전환점을 좌/우 어느 조에 포함시킬지는 직접 계산을 해 본 후 결정.
항상 두 가지 계산을 하게 됨.

하나의 후보 조가 i 부터 j 까지이고, j 가 전환점
또 하나의 후보 조가 j 부터 k 까지.
이런 경우, 다음 두 가지 계산중에 선택해야 함.
    score(i, j) + score(j+1, k)    # 전환점을 A조에 포함
    score(i, j-1) + score(j, k)    # 전환점 k를 미포함

만약 k 이후에도 더 학생이 있는 경우, k 역시 전환점이고, 두 가지 선택지가 생김.

전환점의 수가 m 이라면 2^m 가지 경우의 수가 발생.

최대 학생 수 N 이면 전환점의 최대 수는 N-2. 2^(N-2)번의 계산. 대략 O(2^N)
이것이 O(N^3) 과 비교하면 더 빠른가? -> NO!

----
9/14 2차 시도.

score() 함수가 bottleneck?
    - 호출할 때 원래 리스트의 슬라이싱으로 객체 생성시의 부하.
    - 함수 내부에서 min 1번, max 1번, 총 두 번의 내부 루프. (내부 구현이라 느리진 않겠으나..)

모든 범위들의 최대 최소 값을 미리 구해두는 방법을 적용. 나머지 알고리즘은 일단 그대로.
결과:
N=1000 인 경우. 동일한 랜덤 입력데이터에 대해:
export _N=1000
# 2084599
# $run  19.26s user 0.07s system 99% cpu 19.420 total  <- solve()  bottom-up

# 2051263
# $run  16.52s user 0.08s system 99% cpu 16.681 total  <- solve3()

수행 시간은 15% 정도 단축. 하지만 답이 다름. 최대 최소를 제외한 나머지 로직은 그대로 유지했는데 왜 달라짐?

solve1(), solve2() 는 a2229_slow.py 로 이동.

-------
9/14 3차 시도

증가 구간, 감소 구간으로 나눈다. 전환점은 두 번 포함이 되는데..
예: [8, 6, 1, 4, 7, 5, 3, 2]
-> (8 6 1) (1 4 7) (7 5 3 2)
전환점을 어느 그룹에 소속 시킬지에 따라, 각 그룹은 1씩 더 작을 수도 있다.

이 그룹(조)의 개수를 M 이라고 하자. 각 조는 0, 1, .., M-1 로 번호를 매긴다.
이 그룹을 하나씩 늘려가면서 dp 로 푼다.

실패.
greedy 로는 최적 해가 나오지 않음.
예:
    echo '5\n3 9 2 6 5' | $run
    # 10 <- 정답 (dp)
    A: [3, 9, 2, 6, 5]
    *** chunk(0, 4)
        inc [0~0] (3 .. 3), +0 -> 0
    *** chunk(1, 4)
        dec [1~2] (9 .. 2), +7 -> 0
    *** chunk(3, 4)
        [3~4] (6 .. 5), +1 -> 7
    8 # <- 오답 (greedy)

위 예에서는 두번째 9가 뒤쪽 조에 붙게 됨. (9-2 가 9-3 보다 점수가 더 크기 때문).
하지만 이것은 최적 해가 아니다.

----
9/14,
greedy 대신 모든 분할점의 경우를 다 검토하도록 구현함.
결과: 시간 내 수행 완료됨.

-> solve5(), solve6()

---
9/15
제출 후 다른 답안들 참고하여 가장 최적이라고 생각되는 방식으로 재구현.
순수 1차원 dp 로만 풀이 가능. 훨씬 코드가 간결해짐.
결국 이 코드를 염두하여 골드5 등급이 매겨진 듯 함.

-> solve7()


'''




import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return A,


def solve6(A:list[int])->int:
    '''
    solve6:
    solve5 에서 인덱싱 방법만 조정.

    solve5:
    solve4 의 방식을 쓰되 모든 경우의 전환점 경우를 다 고려.
    전환점의 개수는 최대 N-2 개 이므로 경우의 수가 2^(N-2) 가지로 보이지만
    memoization을 적용하면 그 보다는 적어지지 않을까?
        -> a2229_slow.py 참고.
    '''
    N = len(A)
    INF = 10_001

    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, N+50))

    dp = [ [-1]*(N) for _ in range(N) ]
    # dp[j][k] 는 Aj 부터 Ak 까지 범위에서 조 구성의 모든 경우 중 최대 점수.
    # 우리가 최종적으로 구하고자 하는 값은 dp[0][N-1]
    # dp[][] 값이 <0 이면 아직 계산이 안된 경우.
    # 주의: 우리는 모든 dp 값을 다 구하려고 시도하지 않는다.

    mins = [ [INF]*(N) for _ in range(N) ] # min score
    maxs = [ [0]*(N) for _ in range(N) ] # max score

    # min, max 미리 계산.  O(N^2)
    # 이 계산만 수행하는 데 대략 90ms 정도 소요됨. (내 macbook 기준)
    for j in range(0, N):  # 0 ~ N-1
        for k in range(j, N):  # j ~ N-1
            # j 부터 k 까지의 범위 중 단순 최대, 최소 값. (j <= k)
            if j == k:
                mins[j][k] = maxs[j][k] = A[k]
            else:
                mins[j][k] = min(mins[j][k-1], A[k])
                maxs[j][k] = max(maxs[j][k-1], A[k])

    if N == 1: return 0

    def memoize_score(start, end):
        # [start 와 end] 가 단일 조로 구성되었음.
        sc = maxs[start][end] - mins[start][end]
        dp[start][end] = sc
        return sc

    def get_max_score(start:int, end:int)->int:
        '''
            start, end 는 A[] 의 인덱스.
            A[start] 부터 A[end] 범위 (inclusive)에서 조 구성 경우 중 최대 점수를 리턴.
            start <= end
        '''
        if start > end: return 0 # 비정상 호출.

        if dp[start][end] >= 0:  # memoized
            return dp[start][end]

        length = end - start + 1
        if length == 1: # start == end
            dp[start][end] = 0; return 0

        if length == 2:
            return memoize_score(start, end)

        # assert length >= 3
        delta0 = A[start+1] - A[start] # 초기 방향. { 음수, 0, 양수 } 중 한가지.

        # 증감 방향이 바뀌는 부분을 찾는다.
        #  A[i-1] ↑ A[i] ↓ A[i+1] : up -> down
        #  A[i-1] ↓ A[i] ↑ A[i+1] : down -> up

        for i in range(start+1, end): # i: start+1 ~ end-1
            delta = A[i+1] - A[i]
            # 초기 방향이 없었던 경우라면, 지금 초기 방향을 설정
            if delta0 == 0 and delta != 0:
                delta0 = delta
            # 방향이 같으면 계속 탐색.
            if delta0 == 0 or (delta0 < 0 and delta <= 0) or (delta0 > 0 and delta >= 0):
                continue

            # A[i]를 앞 조에 포함시키는 경우.
            sc1 = memoize_score(start, i) + get_max_score(i+1, end)
            # A[i]를 뒷 조에 포함시키는 경우.
            sc2 = memoize_score(start, i-1) + get_max_score(i, end)

            sc = max(sc1, sc2) # 두 가지 경우 중 최대값
            dp[start][end] = sc
            return sc

        # 방향 전환 없이 루프 종료 한 경우
        sc = memoize_score(start, end)
        dp[start][end] = sc
        return sc

    # log("A: %s", A)
    return get_max_score(0, N-1)


def solve7(A:list[int])->int:
    '''
    가장 최적화 된 알고리즘 같음.

    출처:
    https://www.acmicpc.net/source/94375518

    '''

    N = len(A)
    dp = [0] * N
    # dp[k] 는 학생 0 부터 학생 k 만을 대상으로 조짜기 했을 때의 최대 점수.

    # dp[0] = 0  # 1인 조는 점수 0

    for i in range(1, N):
        # (0 ~ i-1) 까지의 최적 해가 구해진 상태에서 (dp[i-1]에 저장)
        # 새롭게 A[i] 가 추가되었을 때 늘어난 인원에 대해 조짜기의 최대 점수를 계산.
        #
        # 즉, dp[0] ~ dp[i-1] 을 아는 상태에서 dp[i] 구하기.

        mx, mn = A[i], A[i]
        dp[i] = dp[i-1]

        # 분할점 j를 한칸씩 앞으로 이동시켜 가며,
        # 새로 추가된 A[i] 조를 어느 조에 포함시켜야 최대 점수가 갱신되는지 확인.
        # j==0 인 경우는 모두 다 하나의 조로 구성하는 것.

        for j in range(i-1, -1, -1):  # j: i-1 ~ 0

            mx, mn = max(mx, A[j]), min(mn, A[j])
            #
            #  { (0, ..) (.., j-1) } (j, ..., i-1, i)
            #       dp[j-1]              mx, mn

            dp[i] = max(dp[i], mx-mn) if j==0 else \
                    max(dp[i], dp[j-1]+mx-mn)


    return dp[N-1]



if __name__ == '__main__':
    r = get_input()
    # print(solve6(*r))
    print(solve7(*r))




#----------------

import time,os
from random import seed,randint,shuffle
from a2229_slow import solve3_minmax, solve5

def fake_input():
    seed(time.time())
    # seed(43)
    N = int(os.getenv('_N', '100'))
    A = [ randint(0,10000) for _ in range(N) ]
    return N,A

def zigzag_input():
    import time,os
    from random import seed,randint,shuffle
    seed(time.time())
    # seed(43)
    N = int(os.getenv('_N', '100'))
    MAX_V = 100
    A = [randint(0,MAX_V)]
    for _ in range(1,N):
        if len(A)%2: A.append(randint(A[-1],MAX_V))  # inc
        else: A.append(randint(0,A[-1])) # dec
    return N,A

def gen_input():
    N,A = fake_input()
    print(N); print(' '.join(map(str, A)))

def test_1():
    # solve5 의 정답이 맞는지 검증용.
    T = int(os.getenv('_T', '3'))
    for t in range(T):
        log("******** test %d/%d", t, T)
        # N,A = fake_input()
        N,A = zigzag_input()
        # log("A: %s", A)

        out1 = solve5(A)
        log("out1: %s", out1)
        # out2 = solve3_minmax(A)
        # log("out2: %s", out2)
        out3 = solve6(A)
        log("out3: %s", out3)
        # if out1 != out2 or out1 != out3:
        if out1 != out3:
            assert False, "mismatch"
    log("done")


'''
예제 입력 1
10
2 5 7 1 3 4 8 6 9 3
예제 출력 1
20

----
run=(python3 a2229.py)


echo '10\n2 5 7 1 3 4 8 6 9 3' | $run
# 20


echo '1\n7' | $run
# 0
echo '2\n0 7' | $run
# 7
echo '3\n2 9 4' | $run
# 7
echo '3\n2 9 13' | $run
# 11
echo '4\n1 3 5 7' | $run
# 6
echo '4\n1 5 3 7' | $run
# 8
echo '4\n1 3 9 8' | $run
# 8
echo '5\n3 9 2 6 5' | $run
# 10

-------

_T=10 _N=100 python3 -c "__import__('a2229').test_1()"

(python3 <<EOF
import time,os
from random import seed,randint,shuffle
# seed(time.time())
seed(43)
N = int(os.getenv('_N', '100'))
A = [ randint(0,10000) for _ in range(N) ]
print(N)
print(' '.join(map(str, A)))
EOF
) | time $run

N=1000 인 경우.
export _N=1000
# 2084599
# $run  19.26s user 0.07s system 99% cpu 19.420 total  <- solve()  bottom-up
# $run  38.72s user 6.70s system 99% cpu 45.555 total  <- solve2() top-down
# $run  16.39s user 0.07s system 99% cpu 16.509 total  <- solve3() pre scored
# $run  0.09s user 0.01s system 96% cpu 0.102 total  <- solve5()

solve5()의 경우, 전환점이 몇 개냐에 따라 수행 시간이 극과 극으로 차이가 날 수 있다.
worst case 는 입력 점수가 지그재그 형태인 경우. 즉, 모든 곳이 전환점.

(python3 <<EOF
import time,os
from random import seed,randint,shuffle
# seed(time.time())
seed(43)
N = int(os.getenv('_N', '100'))
A = [randint(10,10000-10)]
for k in range(1,N):
    if len(A)%2: A.append(randint(A[-1],10000))  # inc
    else: A.append(randint(0,A[-1])) # dec
print(N)
print(' '.join(map(str, A)))
EOF
) | time $run

export _N=1000
# $run  0.09s user 0.01s system 98% cpu 0.105 total  <- solve5()

'''

