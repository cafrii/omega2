
import sys
import heapq

input = sys.stdin.readline
N = int(input().rstrip())

hq1 = [] # first half (which has small numbers). it is maximum que.
hq2 = [] # second half (which has large numbers). it is minimum que.

for k in range(N):
    a = int(input().rstrip())
    heapq.heappush(hq2, a) # always add to hq2

    # make balance. there are only two cases here:
    #  1.  len(hq1) == len(hq2)
    #  2.  len(hq1) < len(hq2) by one
    #
    if len(hq1) == len(hq2):
        # compare the two heads
        if -hq1[0] > hq2[0]:
            v1 = -heapq.heappop(hq1)
            v2 = heapq.heappop(hq2)
            heapq.heappush(hq1, -v2)
            heapq.heappush(hq2, v1)
    else: # len(hq1) < len(hq2)
        # move one item from hq2 to hq1
        a = heapq.heappop(hq2)
        heapq.heappush(hq1, -a)

    # final states are either of
    #    len(hq1) == len(hq2)
    #      or
    #    len(hq1) > len(hq2) by one.
    # in either case, hq1 head is median value

    # print(hq1, file=sys.stderr, end='')
    # print(hq2, file=sys.stderr)
    print(-hq1[0])

