
'''
유사 문제
    1927 - 최소 힙
    11279 - 최대 힙
    11286 - 절대값 힙

절댓값 힙 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음) (하단 참고)	256 MB	69523	39723	31220	57.170%

문제

절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다.
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
입력되는 정수는 -231보다 크고, 231보다 작다.

출력
입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
'''


import heapq
import sys
input = sys.stdin.readline

hq = []
# element: tuple, ( abs_value, original_value )

N = int(input().rstrip())
for _ in range(N):
    x = int(input().rstrip())
    if x != 0:
        # tuple 형태로 저장.
        # 최소 힙으로 동작하면 되므로 그냥 추가하면 됨.
        # 동일한 abs 값을 갖는 여러개의 항목이 추가될 수 있음.
        heapq.heappush(hq, (abs(x), x))
        print(f'  que: {hq}', file=sys.stderr)
        continue

    if not hq:
        print(0)
        continue

    print(heapq.heappop(hq)[1])
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



시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 100_000
print(N)
for _ in range(N):
    if randint(0,100) < 50:
        print(0)
    else:
        print(randint(-3, 3))
EOF
) | time python3 11286.py > /dev/ttys022 2> /dev/null

0.28s user 0.11s system 93% cpu 0.415 total

'''