import sys
input = sys.stdin.readline

set1 = set()

N = int(input().strip())
for _ in map(lambda s: set1.add(int(s)), input().split()): pass

M = int(input().strip())
B = list(map(int, input().split()))
for b in B:
    print(1 if b in set1 else 0)
