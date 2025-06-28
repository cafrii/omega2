
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def find_lislen(A:list[int])->list[int]:
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
        index 4 을 예로 들어본다. A[4] = 4
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
    #log("%s", A)
    #log("%s", dpf)
    #log("%s", dpr)

    answer = max((a+b-1) for a,b in zip(dpf,dpr))
    return answer

N = int(input().strip())
A = list(map(int, input().split()))
assert len(A) == N
print(solve(A))
