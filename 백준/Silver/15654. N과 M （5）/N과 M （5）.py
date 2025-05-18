import sys
input = sys.stdin.readline

N,M = map(int, input().split())
nums = list(sorted(map(int, input().split())))
assert len(nums) == N

arr = [0] * M
used = {}

def back(idx):
    if idx >= M:
        print(*arr)
        return
    for k in nums:
        # check if k is already used.
        if used.get(k, 0): continue
        arr[idx] = k
        used[k] = 1
        back(idx + 1)
        used[k] = 0

back(0)
