
import sys
input = sys.stdin.readline

def solve(A:list, M:int):
    N = len(A)
    arr = [0]*M

    def populate(index, digits:list):
        if index >= M:
            print(*arr)
            return
        d2 = sorted(set(digits))
        for k in d2:
            arr[index] = k
            d3 = digits.copy(); d3.remove(k)  # digits 에서 k '하나'만 제거한 것.
            populate(index + 1, d3)
            arr[index] = 0

    populate(0, A)


N,M = map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == N
solve(A, M)
