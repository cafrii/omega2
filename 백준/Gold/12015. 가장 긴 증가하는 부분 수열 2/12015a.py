'''

여러가지 시행 착오들.

'''

import bisect
import sys
input = sys.stdin.readline

MAX_N = 1_000_000

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve_timeout(A:list):
    N = len(A)
    A = [0] + A
    # A[0] 은 특별한 용도로 필요하므로 reserve.

    dp = [0] * (N+1)
    # dp[i] 는 i번째 (1<=i<=N) 숫자를 마지막 숫자로 사용하는 LIS 의 길이

    for i in range(1, N+1):
        # num = A[i]  # 이 단계에서 새로 추가할 숫자

        # A[0:i] 중에서 A[i]를 이어 붙일 수 있는 후보 A[k]들을 검색
        #  대응되는 dp[k]의 최대 값 (길이가 가장 긴 LIS)을 찾음.

        # arr = []
        # for k in range(i):
        #     if A[k] < A[i]:
        #         arr.append(dp[k])
        # dp[i] = max(arr) + 1

        dp[i] = max(dp[k] for k in range(i) if A[k]<A[i]) + 1

        log("A[%d]=%d, %s", i, A[i], dp[:i+1])

    return dp[N]


def solve_timeout2(A:list):
    N = len(A)
    dp = [0] * (N)
    # dp[i] 는 i번째 (0<=i<N) 숫자 A[i]를 마지막 숫자로 사용하는 LIS 의 길이

    dp[0] = 1 # A[0]으로 구성된 길이 1짜리 LIS

    for i in range(1, N):
        # A[0:i] 중에서 A[i]를 이어 붙일 수 있는 후보 A[k]들을 검색
        #  대응되는 dp[k]의 최대 값 (길이가 가장 긴 LIS)을 찾음.
        dp[i] = max((dp[k] for k in range(i) if A[k]<A[i]), default=0) + 1
        # 조건에 맞는 부분수열이 없으면 partial 이 empty 이고 그 때 default 값이 사용됨.

        # log("A[%d]=%d, %s", i, A[i], dp[:i+1])
    return max(dp)


def solve2(A:list):
    N = len(A)
    # max_a = max(A)

    dp = [0] * (N)
    # dp[i] 는 숫자 A[i]를 마지막 숫자로 사용하는 LIS 의 길이
    # i는 zero-base. (0 <= i < N)

    L = []
    # L[k] 는 길이 k LIS 의 맨 끝 숫자.
    # 조건을 만족하는 수가 여럿 존재할 경우는 가장 작은 숫자를 저장함.

    # log("A: %s", A)
    L.append(0)  # LIS 길이가 0 이 될 수는 없음.

    # dp[0] 부터 차례로 dp[i]를 채워 나간다.
    for i in range(N):
        if i == 0:
            # dp[0] 은 A[0]을 끝자리로 하는 LIS이므로 길이 1의 LIS이다.
            dp[i] = 1
            # L[1] = A[0]
            L.append(A[0])
        else:
            '''
                dp[i] 구하기: dp[i]는 숫자 A[i]를 마지막 숫자로 사용하는 LIS의 길이
                A[:i] 숫자 중 A[i]보다 작아서 A[i]를 뒤에 더 붙일 수 있는 경우를 찾을 수도 있지만
                L[] 에서 찾는 것이 더 빠르다.
                정렬된 L에서 A[i]보다 작은 최대 A[k]를 찾는다. L은 정렬된 상태이므로 이분탐색 가능.

                예:
                    L = [0, 1, 5, 7, 9, 12] 이고 A[i]가 6 이라고 하자.
                    6 보다 작은 값은 L[2]=5 이다.
                    길이 2의 LIS 끝 값이 5이므로 여기에 6을 덧붙일 수 있다.
                    6을 덧붙이면 LIS 길이는 3이 된다.
                    기존 L[3]은 7인데, 7보다 6이 더 적으므로 L[3]을 6으로 업데이트 한다.
                    L = [0, 1, 5, 6, 9, 12]

                이분탐색을 직접 구현하는 대신 라이브러리를 활용한다.
                위의 예에서 bisect_left(L, 6)은 인덱스 3을 리턴한다.
            '''
            idx = bisect.bisect_left(L, A[i])
            '''
                L[idx]는 A[i]가 들어갈 수 있는 위치.
                즉 L[:idx] 의 모든 요소는 A[i]보다 작고 A[i]를 붙여 IS를 만들수 있는 경우가 됨
                L[:idx] 중 가장 큰 L[idx-1]의 경우에 A[i]를 붙여야 LIS가 됨.
                A[i]를 붙여 새로 만든 IS의 길이는 idx-1 + 1 = idx 가 된다.
            '''

            # 주의: idx 는 L 범위를 넘어설 수 있음.
            if idx >= len(L):
                L.append(A[i])
            else:
                # L[idx] = min(A[i], L[idx])
                L[idx] = A[i]
                # 기존 L[idx] 에는 A[i]보다 작은 값이 있을 수 없으므로
            dp[i] = idx

        # log("A[%d] = %d", i, A[i])
        # log("    D[]: %s", dp[:i+1])
        # log("    L[]: %s", L)

    # return max(dp)
    return len(L)-1



N = int(input().strip())
A = list(map(int, input().split()))

print(solve2(A))



'''
run=(python3 12015.py)

6
10 20 10 30 20 50
-> 4

7
4 5 6 1 2 3 4
-> 4


echo '6\n10 20 10 30 20 50' | $run
echo '7\n4 5 6 1 2 3 4' | $run

->
4  4


A: [4, 5, 6, 1, 2, 3, 4]
A[0]=4
    D[]: [1]
    L[]: [0, 4]
A[1]=5
    D[]: [1, 2]
    L[]: [0, 4, 5]
A[2]=6
    D[]: [1, 2, 3]
    L[]: [0, 4, 5, 6]
A[3]=1
    D[]: [1, 2, 3, 1]
    L[]: [0, 1, 5, 6]
A[4]=2
    D[]: [1, 2, 3, 1, 2]
    L[]: [0, 1, 2, 6]
A[5]=3
    D[]: [1, 2, 3, 1, 2, 3]
    L[]: [0, 1, 2, 3]
A[6]=4
    D[]: [1, 2, 3, 1, 2, 3, 4]
    L[]: [0, 1, 2, 3, 4]
4

echo '9\n3 1 4 1 5 9 2 6 5' | $run
-> 4



run=(python3 12015.py)

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 1_000_000
# N = 10000
print(N)
print(' '.join( str(randint(1,N)) for k in range(N) ))
EOF
) | time $run 2> /dev/null

N 이 10000 인 경우, 4초를 초과함!
$run 2> /dev/null  4.38s user 0.02s system 99% cpu 4.415 total

'''
