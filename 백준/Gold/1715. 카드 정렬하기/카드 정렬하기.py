
import sys
import heapq

def solve_(N:list[int]):
    # N will be modified inside
    hq = N
    heapq.heapify(hq)

    count = 0
    while len(hq) >= 2:
        # print(count, hq, file=sys.stderr)
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        heapq.heappush(hq, a+b)
        count += (a+b)
    # print(count, hq, file=sys.stderr)
    return count

input = sys.stdin.readline
N = int(input().strip())
A = []
for _ in range(N):
    A.append(int(input().strip()))
print(solve_(A))
