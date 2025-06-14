'''

12:33~1:00


그런데 아마도 100% timeout 이 발생.
N 값이 7000 만 넘어가도 1초를 넘김.

메모이제이션 필요.
빈 강의실 찾는 루프를 없애야 함.
강의실을 end time 기준 정렬 상태를 유지하면, 맨 앞의 강의실 하나만 검사하면 된다.


'''

from heapq import heappush,heappop
import sys
input = sys.stdin.readline


def solve_timeout(timetable:list[tuple])->int:
    # N = len(timetable)

    timetable.sort()
    # sorting 할 때, start time 으로만 정렬 시키면 좀 더 효율적일 것임.
    # timetable.sort(key=lambda t:t[0])

    clsroom:list[int] = []
    # index: room number
    # classroom[k]: [ reserved_time_until ]
    #         -1 means that it is available (free)
    for s,e in timetable:
        # mark class free if already ended
        empty_room = -1
        for idx,t in enumerate(clsroom):
            if t < 0: pass # it is available
            elif t <= s: clsroom[idx] = t = -1
            if t < 0 and empty_room < 0:
                empty_room = idx
        if empty_room < 0: # no free room.
            clsroom.append(e) # reserve this room until time e.
        else:
            clsroom[empty_room] = e
        # print(clsroom)

    return len(clsroom)



def solve(timetable:list[tuple])->int:
    timetable.sort()
    # sorting 할 때, start time 으로만 정렬 시키면 좀 더 효율적일 것임.
    # timetable.sort(key=lambda t:t[0])

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



'''
예제 입력 1
3
1 3
2 4
3 5
예제 출력 1
2

run=(python3 11000.py)
echo '3\n1 3\n2 4\n3 5' | $run
-> 2


export _N=200

(python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
N = int(os.getenv('_N','10')) # 2000 #200_0000
print(N)
for k in range(N):
    print(0, randint(1,int(1e9)))
EOF
) | time $run

-> 0.19s user 0.02s system 69% cpu 0.297 total


'''
