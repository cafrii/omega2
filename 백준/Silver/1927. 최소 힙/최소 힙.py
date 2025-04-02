import sys,heapq
input = sys.stdin.readline

N = int(input().strip())
heap = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else: # empty
            print(0)
    else:
        heapq.heappush(heap, x)
        