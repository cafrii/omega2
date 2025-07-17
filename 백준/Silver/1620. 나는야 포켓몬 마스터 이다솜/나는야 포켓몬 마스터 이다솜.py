
import sys
input = sys.stdin.readline

N,M = map(int, input().split())

id2name = []  # 0-base
name2id = {}

for _ in range(N):
    name = input().strip()
    id2name.append(name)
    name2id[name] = len(id2name)

for _ in range(M):
    name_or_id = input().strip()
    if name_or_id.isdigit():
        print(id2name[int(name_or_id)-1])
    else:
        print(name2id[name_or_id])
