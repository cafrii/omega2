
'''
15650

문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.


입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

15649 와의 차이점:
    - 수열이 오름차순이어야 한다


'''

import sys
input = sys.stdin.readline

def log(fmt, *args):
    print(fmt % args, file=sys.stderr)

N,M = map(int, input().split())

A = [0] * M

# 1부터 N까지의 수를 이용하여 M자리의 수를 생성.
# 앞자리부터 채워나감.

def populate(A, len_a):
    # len_a: A에 현재까지 채워진 숫자의 길이
    # A[len_a] 에 새로운 숫자를 채우면 됨.

    log('populate: %d, %s', len_a, A[:len_a])

    max_a = max(A[:len_a]) if len_a > 0 else 0 # A[:len_a] 에서 사용된 숫자 중 최대값

    for k in range(1, N+1):
        # 두 가지 조건을 만족해야 함.
        # 1. 이미 사용된 숫자와 중복되면 안됨.
        # 2. 오름 차순이어야 함.
        if k <= max_a or k in A[:len_a]:
            continue
        # 재귀 호출.
        A[len_a] = k
        if len_a + 1 < M:
            populate(A, len_a + 1)
        else:
            print(*A)

populate(A, 0)


'''
예제 입력 1
3 1
예제 출력 1
1
2
3

예제 입력 2
4 2
예제 출력 2
1 2
1 3
1 4
2 3
2 4
3 4

예제 입력 3
4 4
예제 출력 3
1 2 3 4
'''
