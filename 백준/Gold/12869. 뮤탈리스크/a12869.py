'''
12869번
뮤탈리스크 성공, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	13674	6745	4596	47.676%

문제
수빈이는 강호와 함께 스타크래프트 게임을 하고 있다.
수빈이는 뮤탈리스크 1개가 남아있고, 강호는 SCV N개가 남아있다.

각각의 SCV는 남아있는 체력이 주어져있으며, 뮤탈리스크를 공격할 수는 없다.
즉, 이 게임은 수빈이가 이겼다는 것이다.

뮤탈리스크가 공격을 할 때, 한 번에 세 개의 SCV를 공격할 수 있다.

첫 번째로 공격받는 SCV는 체력 9를 잃는다.
두 번째로 공격받는 SCV는 체력 3을 잃는다.
세 번째로 공격받는 SCV는 체력 1을 잃는다.

SCV의 체력이 0 또는 그 이하가 되어버리면, SCV는 그 즉시 파괴된다.
한 번의 공격에서 같은 SCV를 여러 번 공격할 수는 없다.

남아있는 SCV의 체력이 주어졌을 때, 모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 SCV의 수 N (1 ≤ N ≤ 3)이 주어진다.
둘째 줄에는 SCV N개의 체력이 주어진다.
체력은 60보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 SCV를 파괴하기 위한 공격 횟수의 최솟값을 출력한다.

----
12:27~1:37

----

1. brute-force

931,913,391,319,193,139

0:  (12 10 4)
1:  (3 7 3) (3 9 1) (9 1 3) (9 9 0) (11 1 1) (11 7 0)
2:  위 각각의 경우에 대해서 다시 6가지씩 연산..
...
맨 먼저 (0 0 0) 이 발견되는 단계가 정답.
문제점:
각 단계가 하나 늘어날 때 마다, 추적해야 하는 상태의 수가 6^N 으로 늘어난다.
속도도 문제지만 메모리도 감당이 안될 듯.

----
2. dp

3차원 dp 구조.
scv 가 셋 있는 경우.
dp[i][j][k] 는 scv 각각의 체력이 i, j, k 일때, 필요한 최소 공격 수.

dp[0][0][0] = 0

dp[i][j][k] = min(
    dp[i-9][j-3][k-1],
    dp[i-9][j-1][k-3],
    dp[i-3][j-9][k-1],
    dp[i-3][j-1][k-9],
    dp[i-1][j-9][k-3],
    dp[i-1][j-3][k-9],
) + 1
음의 인덱스에 주의 필요함.

----
결과: 제출 확인.

'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return N,A


def solve(N:int, A:list[int])->int:
    '''
    first impl.
    use 3-d dp
    '''
    # dimension up
    if N < 3:
        if N == 2:
            A = [ *A, 0 ]
        elif N == 1:
            A = [ *A, 0, 0 ]
        N = 3

    MAX_HP = 60
    dp = [[ [0]*(MAX_HP+1) for j in range(MAX_HP+1) ] for k in range(MAX_HP+1) ]

    def safedp(i:int, j:int, k:int)->int:
        if i<0: i=0
        if j<0: j=0
        if k<0: k=0
        return dp[i][j][k]

    dp[0][0][0] = 0
    a0,a1,a2 = A
    log("A: %s", A)
    '''
        * * A *
        * * * *
        B * * *
        * * * C

        A,B 에서 C에 이르는 길은 두 가지.  A->C 와 B->C.
        dp[C]는 dp[A]와 dp[B] 두가지로부터 갱신 되므로 둘 중 최적을 선택해야 한다.
    '''

    for i in range(0, a0+1):
        for j in range(0, a1+1):
            for k in range(0, a2+1):

                if (i,j,k) == (0,0,0): continue

                dp[i][j][k] = min(
                    safedp(i-9, j-3, k-1),
                    safedp(i-9, j-1, k-3),
                    safedp(i-3, j-9, k-1),
                    safedp(i-3, j-1, k-9),
                    safedp(i-1, j-9, k-3),
                    safedp(i-1, j-3, k-9),
                ) + 1
                log("dp[%d,%d,%d] <- %d", i, j, k, dp[i][j][k])

    return dp[a0][a1][a2]


def solve2(N:int, A:list[int])->int:
    '''
    slightly improve solve1()
    remove safedp
    '''
    # make dimension to max 3
    if N < 3: A = A + [0]*(3-N)

    MAX_HP = 60
    dp = [[ [0]*(MAX_HP+1) for j in range(MAX_HP+1) ] for k in range(MAX_HP+1) ]

    dp[0][0][0] = 0
    a0,a1,a2 = A

    for i in range(0, a0+1):
        for j in range(0, a1+1):
            for k in range(0, a2+1):

                if (i,j,k) == (0,0,0): continue

                dp[i][j][k] = min(
                    dp[max(i-9, 0)][max(j-3, 0)][max(k-1, 0)],
                    dp[max(i-9, 0)][max(j-1, 0)][max(k-3, 0)],
                    dp[max(i-3, 0)][max(j-9, 0)][max(k-1, 0)],
                    dp[max(i-3, 0)][max(j-1, 0)][max(k-9, 0)],
                    dp[max(i-1, 0)][max(j-9, 0)][max(k-3, 0)],
                    dp[max(i-1, 0)][max(j-3, 0)][max(k-9, 0)],
                ) + 1
                # log("dp[%d,%d,%d] <- %d", i, j, k, dp[i][j][k])

    return dp[a0][a1][a2]



def solve3(N:int, A:list[int])->int:
    '''
    using recursive call with memoization

    '''

    # dimension up
    if N < 3: A = A + [0]*(3-N)

    MAX_HP = 60
    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, MAX_HP + 10))

    dp = [[ [-1]*(MAX_HP+1) for j in range(MAX_HP+1) ] for k in range(MAX_HP+1) ]
    dp[0][0][0] = 0

    def count(a, b, c):
        dpv = dp[a][b][c]
        if dpv >= 0: return dpv

        ans = min(
                count(max(a-9, 0), max(b-3, 0), max(c-1, 0)),
                count(max(a-9, 0), max(b-1, 0), max(c-3, 0)),
                count(max(a-3, 0), max(b-9, 0), max(c-1, 0)),
                count(max(a-3, 0), max(b-1, 0), max(c-9, 0)),
                count(max(a-1, 0), max(b-3, 0), max(c-9, 0)),
                count(max(a-1, 0), max(b-9, 0), max(c-3, 0)),
            ) + 1
        dp[a][b][c] = ans
        return ans

    return count(*A)


def solve4(N:int, A:list[int])->int:
    '''
    using recursive call with memoization
    dp as a set
    '''

    # dimension up
    if N < 3: A = A + [0]*(3-N)

    MAX_HP = 60
    lm = sys.getrecursionlimit()
    sys.setrecursionlimit(max(lm, MAX_HP + 10))

    dp = {}
    dp[(0, 0, 0)] = 0

    def count(a, b, c):
        if (a, b, c) in dp:
            return dp[(a, b, c)]

        ans = min(
                count(max(a-9, 0), max(b-3, 0), max(c-1, 0)),
                count(max(a-9, 0), max(b-1, 0), max(c-3, 0)),
                count(max(a-3, 0), max(b-9, 0), max(c-1, 0)),
                count(max(a-3, 0), max(b-1, 0), max(c-9, 0)),
                count(max(a-1, 0), max(b-3, 0), max(c-9, 0)),
                count(max(a-1, 0), max(b-9, 0), max(c-3, 0)),
            ) + 1

        dp[(a, b, c)] = ans
        return ans

    return count(*A)


if __name__ == '__main__':
    print(solve3(*get_input()))  # solve3 is fastest





def test():
    import time
    inp = get_input()
    tm = []
    tm.append(time.perf_counter()*1000)
    print(solve(*inp))
    tm.append(time.perf_counter()*1000)
    print(solve2(*inp))
    tm.append(time.perf_counter()*1000)
    print(solve3(*inp))
    tm.append(time.perf_counter()*1000)
    print(solve4(*inp))
    tm.append(time.perf_counter()*1000)
    # tm = [ tm[k]-tm[k-1] for k in range(1,len(tm)) ] # clock to interval (ms)
    tm = [ f'{tm[k]-tm[k-1]:.2f}' for k in range(1,len(tm)) ] # clock to interval
    print("tm:", tm)



'''
예제 입력 1
3
12 10 4
예제 출력 1
2
예제 입력 2
3
54 18 6
예제 출력 2
6
예제 입력 3
1
60
예제 출력 3
7
예제 입력 4
3
1 1 1
예제 출력 4
1
예제 입력 5
2
60 40
예제 출력 5
9

----
run=(python3 a12869.py)

echo '3\n12 10 4' | $run
# 2
echo '3\n54 18 6' | $run
# 6
echo '1\n60' | $run
# 7
echo '3\n1 1 1' | $run
# 1
echo '2\n60 40' | $run
# 9


echo '3\n1 1 4' | $run
# 1
echo '3\n1 1 10' | $run
# 2
echo '3\n1 1 60' | $run
# 7

echo '2\n1 4' | $run
# 1
echo '2\n1 10' | $run
# 2

echo '3\n60 60 60' | $run
# 14

echo '3\n60 60 60' | python3 -c "__import__('a12869').test()"
# tm: ['154.66', '119.56', '5.60', '7.59']
# solve3 이 제일 빠르다.

'''
