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



T = int(input().rstrip())
for _ in range(T):

    dq = DualHeapQue()

    K = int(input().rstrip())
    for k in range(K):
        a = input().split()
        val = int(a[1])
        if a[0] == 'D':
            if val == 1:
                dq.remove_max()
            else:
                dq.remove_min()
        else: # a[0] == 'I':
            dq.insert(val)
        # print(dq, file=sys.stderr)

    # print max, min values of que
    if dq.empty():
        print('EMPTY')
    else:
        print(dq.get_max(), dq.get_min())
