
n = int(input())

workers = set()

for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        workers.add(name)
    else:
        if name in workers:
            workers.remove(name)

for worker in sorted(workers, reverse=True):
    print(worker)
