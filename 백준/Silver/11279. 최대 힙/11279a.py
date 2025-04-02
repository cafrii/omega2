
'''


'''

import sys, heapq

maxheap = []

N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if maxheap:
            print(-heapq.heappop(maxheap))
        else: # empty
            print(0)
    else: # push
        heapq.heappush(maxheap, -x)

