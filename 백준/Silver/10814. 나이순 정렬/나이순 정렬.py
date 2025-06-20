import sys
input = sys.stdin.readline

N = int(input().strip())
members = []
for idx in range(N):
    ln = input().strip()
    k = ln.find(' ')
    assert k > 0
    age = int(ln[:k])
    name = ln[k+1:] # assume only one space is used.
    members.append((age, idx, name))

members.sort()
for e in members:
    print(e[0], e[2])
