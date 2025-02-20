'''

'''

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


'''
예제 입력 1
4
Baha enter
Askar enter
Baha leave
Artem enter

예제 출력 1
Askar
Artem
'''