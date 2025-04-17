ns = []
for _ in range(9):
    ns.append(int(input().strip()))
max_n = max(ns)
print(max_n)
print(ns.index(max_n)+1)
