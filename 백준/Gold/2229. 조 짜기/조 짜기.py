import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    return A,

def solve7(A:list[int])->int:

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
    print(solve7(*r))
