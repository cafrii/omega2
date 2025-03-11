
from typing import List,Tuple

MAX_K = 10_000
NONE = MAX_K + 1

def solve_dp(K:int, V:list):
    # greedy 로 돌려보니, sum 1, sum 2 와 같은 경우가 너무 많이 반복됨.
    # dp 를 사용하기에 최적.

    V.sort(reverse=True)

    min_counts = [NONE] * (K + 1)
    # min_counts[i] 는 가치 i 를 채우기 위해 필요한 최소 동전 개수.
    # NONE 이면 해 없음.

    def find(sum:int) -> int:
        count = NONE
        for v in V:
            if v > sum:
                continue
            if v == sum:
                return 1

            # 이 동전을 사용한다고 하고, 남은 sum-v 의 부분 문제 솔루션으로 답을 결정.
            count = min(count, 1 + min_counts[sum - v])

        return count if count < NONE else NONE

    for i in range(1, K+1):
        min_counts[i]= find(i)

    return min_counts[K] if min_counts[K] < NONE else -1



N,K = map(int, input().split())
V = [ int(input().strip()) for v in range(N) ]

print(solve_dp(K, V))
# print(solve_dp_kind(K, V))

