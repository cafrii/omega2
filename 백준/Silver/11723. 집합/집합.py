
import sys
input = sys.stdin.readline

S = set()
M = int(input().strip())
for _ in range(M):
    words = input().strip().split()
    cmd = words[0]
    val = int(words[1]) if len(words) > 1 else 0
    # print(cmd, val)
    if cmd == 'add':
        if val not in S:
            S.add(val)
    elif cmd == 'remove':
        if val in S:
            S.remove(val)
    elif cmd == 'check':
        if val in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if val in S:
            S.remove(val)
        else:
            S.add(val)
    elif cmd == 'all':
        S = set(range(1,21))
    elif cmd == 'empty':
        S = set()
