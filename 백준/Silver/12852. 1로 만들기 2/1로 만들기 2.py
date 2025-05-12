
import sys
input = sys.stdin.readline

def solve(N) -> tuple[int,list]:

    dp = [ None ] * (N+1)
    # dp[k] 는 (cnt,prev_dp_idx)
    #   cnt 는 k를 1로 만드는데 필요한 연산 횟수
    #   prev_dp_idx 는 참조한 직전 dp 요소 인덱스
    dp[1] = (0, 0) # prev_dp_idx 값은 반드시 <1 이어야 함.

    for k in range(2, N+1):
        candidates = []  # (cnt, prev_dp_index)
        kd2 = kd3 = -1
        if k % 3 == 0:
            kd3 = k // 3
            if kd3 >= 1:
                candidates.append((dp[kd3][0] + 1, kd3))
        if k % 2 == 0:
            kd2 = k // 2
            if kd2 != kd3 and kd2 >= 1:
                candidates.append((dp[kd2][0] + 1, kd2))
        km1 = k-1
        candidates.append((dp[km1][0] + 1, km1))

        cnt,prev_idx = min(candidates, key = lambda x: x[0])
        dp[k] = (cnt, prev_idx)

    # construct nums list, tracking dp, starting from dp[N]
    idx = N
    nums = []
    while idx >= 1:
        nums.append(idx)
        idx = dp[idx][1]

    return dp[N][0], nums


N = int(input().strip())

cnt,nums = solve(N)
print(cnt)
print(' '.join([ str(x) for x in nums ]))
