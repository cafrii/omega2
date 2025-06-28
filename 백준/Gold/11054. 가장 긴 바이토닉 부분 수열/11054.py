'''
11054번
가장 긴 바이토닉 부분 수열

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	64129	33284	26019	51.415%

문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면,
그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다.
(1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

--------

7:02~7:14


'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def find_lislen(A:list[int])->list[int]:
    '''
    O(N^2) 시간을 소요하지만 N의 최대 크기가 크지 않으니 사용할 수 있음.
    최적화 알고리즘은 12015 참고.
        https://www.acmicpc.net/problem/12015
    '''
    N = len(A)
    D = [0] * N

    D[0] = 1
    for i in range(1, N):
        # A[i]를 고려.
        # A[:i] 중에서 A[i]보다 작은 것 만을 추출한 후 해당 D[k]의 최대 값 찾음.
        # 그 길이에 +1을 하여 저장.
        D[i] = max((D[k] for k in range(i) if A[k]<A[i]), default=0) + 1

    return D

def solve(A:list[int])->int:
    '''
    A에 대해 LIS (longest increasing subsequence) 계산을 위한 dp[i]를 구하고
    A[::-1] 에 대해서도 dp[i]를 구해 놓은 후 조합하여 판단.

    dpx[i]는 A[i]를 끝자리로 하는 LIS 부분수열의 길이.
    '''
    N = len(A)
    dpf = find_lislen(A)  # forward
    dpr = find_lislen(A[::-1])[::-1] # reversed
    '''
    예시:
        A   = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
        dpf = [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
        dpr = [1, 5, 2, 1, 4, 3, 3, 3, 2, 1]
                           ^
        index 4 을 예로 들어본다. A[4] = 4.
        dpf[4] 는 3
            즉, A[:4] 인 [1, 5, 2, 1, 4, ..] 의 LIS 길이는 3
            (LIS 예시: 1 2 4)
        dpr[4] 는 4
            즉, A[4:] 인 [.. 4, 3, 4, 5, 2, 1] 의 LDS 길이는 4
            (LDS 예시: 4 3 2 1)
        A[4]를 중앙점으로 하는 최장 바이토닉 부분수열의 길이는
            dpf[4] + dpr[4] - 1 이다.
        (A[4]가 양쪽 dpx에서 모두 다 카운트되었으니 -1을 해 주어야 함)
    '''

    log("%s", A)
    log("%s", dpf)
    log("%s", dpr)

    answer = max((a+b-1) for a,b in zip(dpf,dpr))
    return answer



N = int(input().strip())
A = list(map(int, input().split()))
assert len(A) == N

print(solve(A))



'''
예제 입력 1
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1
7
힌트
예제의 경우 {1 5 2 1 4 3 4 5 2 1}이 가장 긴 바이토닉 부분 수열이다.

run=(python3 11054.py)

echo '10\n1 5 2 1 4 3 4 5 2 1' | $run
-> 7

echo '6\n1 5 1 10 1 30' | $run
-> 4

echo '7\n1 6 7 2 3 4 5' | $run
-> 5


시간 제한 검사

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 1000
print(N)
print(' '.join( str(randint(1,N)) for k in range(N) ))
EOF
) | time $run 2> /dev/null

->
$run 2> /dev/null  0.06s user 0.01s system 95% cpu 0.074 total

'''

