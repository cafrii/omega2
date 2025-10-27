'''
14267번
회사 문화 1, 성공, 골드4

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	13155	5125	3875	36.929%

문제
영선회사에는 매우 좋은 문화가 있는데, 바로 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다.
즉, 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.

모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데, 이 수치 또한 부하들에게 똑같이 칭찬 받는다.

직속 상사와 직속 부하관계에 대해 주어지고, 칭찬에 대한 정보가 주어질 때, 각자 얼마의 칭찬을 받았는지 출력하시오,

입력
첫째 줄에는 회사의 직원 수 n명, 최초의 칭찬의 횟수 m이 주어진다.
직원은 1번부터 n번까지 번호가 매겨져 있다. (2 ≤ n, m ≤ 100,000)

둘째 줄에는 직원 n명의 직속 상사의 번호가 주어진다.
직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다.
1번의 경우, 상사가 없으므로 -1이 입력된다.

다음 m줄에는 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w가 주어진다.
(2 ≤ i ≤ n, 1 ≤ w ≤ 1,000)

사장은 상사가 없으므로 칭찬을 받지 않는다.

출력
1번부터 n번의 직원까지 칭찬을 받은 정도를 출력하시오.

----
5:25~

- 1 2 3 4

  1  2  3  4  5
     2
        4
              6
  0  2  6  6 12

너무 쉬워 보이는데? 이게 골드4?

그냥 번호 1번 부터 쭈욱 순서대로 자신이 받은 칭찬을 계산할 수 있는 것으로 보인다.

dp[n] = dp[k] + A[n]
# k는 직원 n의 직속 상사
# A[n]은 직원n 이 상사로부터 최초로 받은 칭찬

worst case 도 검증 완료.

----
제출 후 검증 완료


'''


import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
        if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = list(map(int, input().split())) # 상사-부하 관련 정보
    assert len(A) == N

    B = []
    for _ in range(M):
        n,w = map(int, input().split()) # 직원 n이 상사로부터 w만큼 칭찬을 받음.
        B.append((n, w))

    return N,M,A,B

def solve(N:int, M, A:list[int], B:list[tuple[int,int]])->list[int]:
    '''
        N: 직원 수
        A[k]: 직원 서열. A[k]는 직원 k+1 의 직속 상사의 번호
            A[0]: 직원 1(사장)의 상사는 없음. -1
            A[1]: 직원 2의 상사.
            A[2]: 직원 3의 상사.
            ...
        B: [(n, w), ...],  len(B)=M
            직원 n이 상사로부터 받은 칭찬이 w
    '''
    log("N %d, M %d, A %s, B %s", N, M, A, B)

    pr = [0] * (N+1)  # praise map, 칭찬 매핑 표
    for n,w in B:
        pr[n] += w
        # pr[k]: 직원 k가 받은 칭찬

    dp = [0] * (N+1)

    for j in range(2, N+1):  # j: 2 ~ N. 사장은 제외.
        jboss = A[j-1]  # 직원 j 의 상사
        dp[j] = dp[jboss] + pr[j]

    return dp[1:]


if __name__ == '__main__':
    a = solve(*get_input())
    print(' '.join(map(str, a)))





'''
예제 입력 1
5 3
-1 1 2 3 4
2 2
3 4
5 6
예제 출력 1
0 2 6 6 12
----
pr=14267
run=(python3 a$pr.py)

echo '5 3\n-1 1 2 3 4\n2 2\n3 4\n5 6' | $run
# 0 2 6 6 12


'''


import time,os
from random import seed,randint,shuffle

# 만들고 보니, worst case 가 안됨.
def gen_worstcase_input():
    seed(time.time())
    seed(43)
    N = 100_000
    # N = 10
    M = N

    # 직원 서열 생성. 맨앞은 사장 1.
    C = list(range(2, N+1))  # 2 .. N
    shuffle(C)
    C = [1] + C  # 맨 앞에는 사장을 추가

    A = [0] * (N)
    A[0] = -1

    # 랜덤 서열
    # for i in range(1, N): # i: 1~N-1
    #     A[i] = randint(1, i)
    # 모두 사장 직속
    # for i in range(1, N): A[i] = 1

    # 일원화된 서열 (정렬)
    for i in range(1, N): A[i] = i

    B = [ (k, 1) for k in range(1, N+1) ]

    B[0] = (2, 1) # 사장은 칭찬을 받을 수 없음. 직원2 에게 칭찬을 하나 더 추가.
    # B[0] = (N, 1)  # 마지막 직원에게 칭찬 추가

    return N,M,A,B

def gen():
    N,M,A,B = gen_worstcase_input()
    print(N,M)
    print(' '.join(map(str, A)))
    print('\n'.join([ f'{b} {w}' for b,w in B ]))

'''
python3 -c "from a14267 import gen; gen()" | time $run


'''