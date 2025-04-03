
'''

1927 - 최소 힙
11279 - 최대 힙
11286 - 절대값 힙

동일한 절대값을 갖는 항목을 리스트로 묶어서 관리할 까 생각해 본 시도인데
완성되지 않았으며 그 기대 이익이 크지 않아서 중단하였음.

heapq 의 경우 임의 노드에 접근하는 것은 비효율적이어서
효율적으로 동작시키기 위해서라면 heapq 아닌 다른 자료구조가 필요함.

'''

import heapq
import sys
input = sys.stdin.readline

hq = []
# element: tuple, ( abs_value, list[int] )

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x != 0:
        # tuple 형태로 저장.
        # 최소 힙으로 동작하면 되므로 그냥 추가하면 됨.
        # 동일한 abs 값을 갖는 여러개의 항목이 추가될 수 있음.
        heapq.heappush(hq, (abs(x), [x]))
        print(f'  que: {hq}', file=sys.stderr)
        continue

    if not hq:
        print(0)
        continue

    # 동일한 abs 값을 갖는 모든 노드를 추출. 둘 이상일 경우 B 형태로 압축시켜 저장.
    min_val = hq[0][0]
    min_list = []

    while hq and hq[0][0] == min_val:
        if type(hq[0][1]) is int:
            min_list.append(hq[0][1])
        else: # list of int
            min_list.extend(hq[0][1])
        heapq.heappop(hq)

    min_list.sort()
    print(f'  popped: val {min_val}, {min_list}', file=sys.stderr)

    print(min_list[0])
    if len(min_list) > 1:
        heapq.heappush(hq, (min_val, min_list[1:]))
    print(f'  que: {hq}', file=sys.stderr)


'''
예제 입력 1
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
예제 출력 1
-1
1
0
-1
-1
1
1
-2
2
0


8
2
-2
0
0
-3
3
0
0
    -> -2 2 -3 3
python3 11286.py > /dev/ttys022


4
-1
-1
0
1





시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 100 #100_000
print(N)
for _ in range(N):
    if randint(0,100) < 40:
        print(0)
    else:
        print(randint(-3, 3))

EOF
) | time python3 11286.py 2> /dev/ttys022



'''