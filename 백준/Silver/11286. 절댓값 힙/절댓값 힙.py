
import heapq
import sys
input = sys.stdin.readline

hq = []
# element: tuple ( abs_value, original_value )

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
        continue

    if not hq:
        print(0)
        continue

    print(heapq.heappop(hq)[1])
    