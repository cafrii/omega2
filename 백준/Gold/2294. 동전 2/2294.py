'''
2294 번

제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
강의
질문 게시판
동전 2
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	128 MB	84498	26584	18851	30.258%
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
'''

from typing import List,Tuple

MAX_K = 10_000
NONE = MAX_K + 1


def solve_greedy(K:int, V:list):
    # K 를 맞추기 위해 V[] 가치의 동전을 몇 개를 사용할 것인지 계산
    V.sort(reverse=True)

    def find(sum:int):
        # sum 을 맞추기 위한 최대 동전 개수를 찾는다.
        # 찾지 못하면 NONE 리턴
        # 각 동전 종류 별로 모두 시도해 보면서, 최대 동전 개수 값을 찾는다.
        count = NONE

        for v in V:
            if v > sum:
                continue
            if v == sum:
                # return 1
                count = 1
                break

            # 이 동전을 사용한다고 하고, 남은 sum-v 의 부분 문제 솔루션으로 답을 결정.
            count = min(count, 1 + find(sum - v))
            # 주의: 최대 MAX_K 회 호출 깊이가 발생 가능함. 이 정도면 문제 없을 듯.

        print(f"sum: {sum}, count: {count}")
        return count if count < NONE else NONE

    result = find(K)
    return result if result < NONE else -1



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
        # print(f"sum: {i}, count: {min_counts[i] if min_counts[i]<NONE else -1}")

    return min_counts[K] if min_counts[K] < NONE else -1



def solve_dp_kind(K:int, V:list):
    # 어떤 조합으로 답을 냈는지 궁금해서, 해의 구성 과정 추적
    V.sort(reverse=True)

    min_counts = [NONE] * (K + 1)
    min_cases = [ [] for _ in range(K+1) ]

    def find(sum:int) -> Tuple[int, List[int]]:
        count = NONE
        cases:List[int] = []

        for v in V:
            if v > sum:
                continue
            if v == sum:
                # return 1
                count = 1
                cases = [v]
                break

            if count > 1 + min_counts[sum - v]:
                count = 1 + min_counts[sum - v]
                cases = [v] + min_cases[sum - v]

        if count < NONE:
            return (count, cases)
        else:
            return (NONE, [])

    for i in range(1, K+1):
        (min_counts[i], min_cases[i]) = find(i)
        print(f"  sum: {i}, count: {min_counts[i] if min_counts[i]<NONE else -1}, {min_cases[i]}")

    return min_counts[K] if min_counts[K] < NONE else -1



N,K = map(int, input().split())
V = [ int(input().strip()) for v in range(N) ]

# 내림차순으로 정렬. 큰 가치의 동전 부터 채우는 것이 당연해 보이므로.
V.sort(reverse=True)

print(N, K, V)
# print(solve_dp(K, V))
print(solve_dp_kind(K, V))



'''
예제 입력 1
3 15
1
5
12

예제 출력 1
3

echo "3 15\n1\n5\n12\n" | python3 a.py
echo "3 15\n3\n7\n12\n" | python3 a.py

echo "1 15\n100\n" | python3 a.py
echo "1 15\n1\n" | python3 a.py
echo "2 16\n2\n16\n" | python3 a.py

시간초과 시뮬레이션
echo "1 10000\n1\n" | time python3 a.py

랜덤 시험
(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,K = 100,10_000
print(N, K)
for _ in range(N):
    print(randint(randint(K*3//2,K), 10_000))
EOF
) | time python3 a.py


'''