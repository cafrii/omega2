
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

    #log('populate: %d, %s', len_a, A[:len_a])

    max_a = max(A[:len_a]) if len_a > 0 else 0 # A[:len_a] 에서 사용된 숫자 중 최대값

    for k in range(1, N+1):
        # 두 가지 조건을 만족해야 함.
        # 1. 이미 사용된 숫자와 중복되면 안됨.
        # 2. 오름차순이어야 함.
        if k <= max_a or k in A[:len_a]:
            continue
        # 재귀 호출.
        A[len_a] = k
        if len_a + 1 < M:
            populate(A, len_a + 1)
        else:
            print(*A)

populate(A, 0)
