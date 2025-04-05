'''
7662

이중 우선순위 큐 다국어

Python3 로 처음 제출할 때 시간 초과. 그런데 서버 부하와도 관련 있어 보임.
T=1 으로 최대 항목 수 시뮬레이션 해도 2초가 넘지 않는데, 아마 T가 좀 큰 값인 것으로 보임.

서버 부하가 크지 않을 때, PyPy3 로 시도해 보자.
아, input = sys.stdin.readline 도 빠뜨렸음.


시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
6 초	256 MB	83090	19203	14104	22.279%

문제

이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다.
전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라
우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다.
이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고
다른 하나는 데이터를 삭제하는 연산이다.
데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고
다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.

정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.

Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.

입력
입력 데이터는 표준입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 Q에 적용할 연산의 개수를 나타내는 정수 k (k ≤ 1,000,000)가 주어진다.
이어지는 k 줄 각각엔 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n이 주어진다.
‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다.
‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다.
최댓값(최솟값)을 삭제하는 연산에서 최댓값(최솟값)이 둘 이상인 경우, 하나만 삭제됨을 유념하기 바란다.

만약 Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시해도 좋다. Q에 저장될 모든 정수는 -231 이상 231 미만인 정수이다.

출력
출력은 표준출력을 사용한다. 각 테스트 데이터에 대해, 모든 연산을 처리한 후 Q에 남아 있는 값 중 최댓값과 최솟값을 출력하라.
두 값은 한 줄에 출력하되 하나의 공백으로 구분하라. 만약 Q가 비어있다면 ‘EMPTY’를 출력하라.
'''


'''
from sortedcontainers import SortedSet

class DoublePriorityQueue:
    def __init__(self):
        self.data = SortedSet()

    def insert(self, value):
        self.data.add(value)

    def remove_min(self):
        if not self.data:
            return None
        min_val = self.data[0]
        self.data.remove(min_val)
        return min_val

    def remove_max(self):
        if not self.data:
            return None
        max_val = self.data[-1]
        self.data.remove(max_val)
        return max_val

    def get_min(self):
        return self.data[0] if self.data else None

    def get_max(self):
        return self.data[-1] if self.data else None
'''


import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

class DualHeapQue:
    def __init__(self):
        self.min_hq = []  # 최소 힙
        self.max_hq = []  # 최대 힙
        self.valid = defaultdict(int)  # 삭제 여부 추적용. 중복을 고려하여 개수를 저장함.
        self.size = 0 # 유효한 요소의 개수. cleanup 하기 전에 개수를 알고 있으면 더 효율적임.

    def empty(self):
        return self.size <= 0

    def insert(self, value:int):
        # 주의: value None 은 사용하면 안됨.
        heapq.heappush(self.min_hq, value)
        heapq.heappush(self.max_hq, -value)  # 최대 힙을 위해 음수 사용
        self.valid[value] += 1
        self.size += 1

    # peek methods. cleanup 기능을 포함하고 있음.
    def get_min(self):
        if self.size == 0:
            return None
        while self.min_hq and self.valid[self.min_hq[0]] == 0:
            heapq.heappop(self.min_hq)
        return self.min_hq[0] if self.min_hq else None

    def get_max(self):
        if self.size == 0:
            return None
        while self.max_hq and self.valid[-self.max_hq[0]] == 0:
            heapq.heappop(self.max_hq)
        return -self.max_hq[0] if self.max_hq else None

    # remove methods. cleanup 기능은 get_xx() 메소드에 일임시킨다.
    def remove_min(self):
        if self.get_min() is None:
            return None
        min_val = heapq.heappop(self.min_hq)
        self.valid[min_val] -= 1
        self.size -= 1
        return min_val

    def remove_max(self):
        if self.get_max() is None:
            return None
        max_val = -heapq.heappop(self.max_hq)
        self.valid[max_val] -= 1
        self.size -= 1
        return max_val

    def __str__(self): # 시간제한 있는 경우는 사용 금지!
        return f'{str(self.min_hq)} {str(self.max_hq)}'


class SlowQue:
    def __init__(self):
        self.a = []
    def empty(self):
        return len(self.a) == 0
    def insert(self, value:int):
        self.a.append(val); self.a.sort()
    def get_min(self):
        return self.a[0] if self.a else None
    def get_max(self):
        return self.a[-1] if self.a else None
    def remove_min(self):
        return self.a.pop(0) if self.a else None
    def remove_max(self):
        return self.a.pop() if self.a else None
    def __str__(self):
        return str(self.a)



T = int(input().rstrip())
for _ in range(T):

    dq = DualHeapQue()
    # sq = SlowQue() # for verification

    K = int(input().rstrip())
    for k in range(K):
        a = input().split()
        val = int(a[1])
        if a[0] == 'D':
            if val == 1:
                dq.remove_max()
                # sq.remove_max()
            else:
                dq.remove_min()
                # sq.remove_min()
        else: # a[0] == 'I':
            dq.insert(val)
            # sq.insert(val)
        # print(dq, file=sys.stderr)

    # print min, max values of que
    if dq.empty():
        print('EMPTY')
    else:
        print(dq.get_max(), dq.get_min())

    # if sq.empty():
    #     print('EMPTY')
    # else:
    #     print(sq.get_max(), sq.get_min())




'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333

예제 출력 1
EMPTY
333 -45


2
1
I 1
1
I 2
-> 1 1, 2 2


1
7
I 1
I 2
I 3
D -1
D 1
I 4
D -1


시간제한 시뮬레이션

(python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
T,K = 1,int(os.getenv('K','1000')) #100
print(T)
for _ in range(T):
    print(K)
    for _ in range(K):
        if randint(1,100) <= 50:
            print(f'I {randint(-9,9)}')
        else:
            print(f'D {randint(0,1)*2-1}')
EOF
) | time python3 7662.py

'''