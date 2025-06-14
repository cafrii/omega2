
from heapq import heappush,heappop
import sys
input = sys.stdin.readline


def solve(timetable:list[tuple])->int:
    # N = len(timetable)
    timetable.sort()

    clsroom:list[int] = [] # min heapque
    # element: endtime
    max_room = 0
    for s,e in timetable:
        while clsroom and clsroom[0] <= s:
            heappop(clsroom)
        heappush(clsroom, e)
        max_room = max(max_room, len(clsroom))
    return max_room


N = int(input().strip())
timetable = []
for _ in range(N):
    si,ti = map(int, input().split())
    # assume si < ti
    timetable.append((si,ti))
print(solve(timetable))
