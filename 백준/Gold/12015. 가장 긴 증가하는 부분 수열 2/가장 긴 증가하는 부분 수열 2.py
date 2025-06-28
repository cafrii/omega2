
import bisect
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve(A:list):
    N = len(A)
    dp = [0] * (N)
    # dp[i] 는 숫자 A[i]를 마지막 숫자로 사용하는 LIS 의 길이
    # i는 zero-base. (0 <= i < N)

    L = []
    # L[k] 는 길이 k LIS 의 맨 끝 숫자.
    # 조건을 만족하는 수가 여럿 존재할 경우는 가장 작은 숫자를 저장함.

    # log("A: %s", A)
    L.append(0)  # LIS 길이가 0 이 될 수는 없음.

    # dp[0] 은 A[0]을 끝자리로 하는 LIS이므로 길이 1의 LIS이다.
    dp[0] = 1
    L.append(A[0])

    # dp[1] 부터 차례로 dp[i]를 채워 나간다.
    for i in range(1,N):
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
            # 기존 L[idx] 에는 A[i]보다 작은 값이 있을 수 없음.
        dp[i] = idx

        # log("A[%d] = %d", i, A[i])
        # log("    D[]: %s", dp[:i+1])
        # log("    L[]: %s", L)

    # return max(dp)
    return len(L)-1


N = int(input().strip())
A = list(map(int, input().split()))
print(solve(A))
