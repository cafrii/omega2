'''
1655

가운데를 말해요 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초 (하단 참고)	128 MB	75300	22604	16932	30.788%

문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다.
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면,
동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다.
백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다. 정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
'''


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

    # print(*(-x for x in reversed(hq1)), sep=',', end='', file=sys.stderr)
    # print(hq1, file=sys.stderr, end='')
    # print(hq2, file=sys.stderr)
    print(-hq1[0])


'''
예제 입력 1
7
1
5
2
10
-99
7
5

예제 출력 1
1
1
2
2
2
2
5

echo '2\n3\n2\n' | python3 1655.py
-> 3, 2

echo '4\n3\n3\n2\n2\n' | python3 1655.py
-> 3, 3, 3, 2

echo '12\n6\n6\n6\n5\n5\n5\n6\n6\n6\n5\n5\n5' | python3 1655.py 2> /dev/null
-> 6,6,6,6,6, 5, 6,6,6,6,6, 5



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 10000 #100_000
print(N)
for _ in range(N):
    print(randint(-10000, 10000))
EOF
) | time python3 1655.py


'''
