'''
10845번
큐

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	256 MB	155512	74482	58552	49.520%

문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.


----

10:18~32


'''

import sys
from collections import deque
from typing import Deque,Iterator

def get_input():
    input = sys.stdin.readline
    N = int(input().strip())
    for _ in range(N):
        yield input().strip()
    return

def solve(it:Iterator):
    # it: input iterator
    # return generator of answer output
    que:Deque[int] = deque()

    for line in it:
        words = line.split()
        cmd = words[0]
        param = int(words[1]) if len(words)>1 else 0
        if cmd == 'push':
            que.append(param)
        elif cmd == 'pop':
            yield que.popleft() if que else -1
        elif cmd == 'size':
            yield len(que)
        elif cmd == 'empty':
            yield 0 if que else 1
        elif cmd == 'front':
            yield que[0] if que else -1
        elif cmd == 'back':
            yield que[-1] if que else -1
    return


for ln in solve(get_input()):
    print(ln)



'''
run=(python3 10845.py)


'''
