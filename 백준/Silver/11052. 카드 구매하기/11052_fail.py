'''
11052


알고리즘이 틀려서 실패!

백트래킹의 효과가 높지 않음.


'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve(P:list[int]) -> int:
    # 단위 카드 당 가격이 높은 것을 먼저 채우는 것이 핵심.
    N = len(P)

    packs = [ (i+1,p) for i,p in enumerate(P) ]
    # [ (1, P1), (2, P2), .. ]
    log('packs: %s', packs)
    # Pi 는 카드 i장 묶음 팩의 가격이다. 단위 카드 당 가격은 Pi/i.
    packs.sort(key = lambda e: e[1]/e[0], reverse=True)
    log('sorted packs: %s', packs)

    # 각 단위의 카드팩을 몇 개씩 구매할지를 단계적으로 결정.
    quantity = [0]*N
    max_price = 0

    def buy(index, target_vol) -> int:
        # index: 계산 할 단계. packs[index] 부터 구매 시작해야 함.
        # target_vol: 더 구매해야 할 카드 수량

        log('#%d: %s, remain %d', index, quantity[:index], target_vol)
        if target_vol == 0:
            return 0 # 성공.
        if index >= N:
            return -1

        pack_vol,pack_price = packs[index] # Pi

        # 이 단계에서 최대로 구매 가능한 팩 개수
        num_pack = target_vol // pack_vol
        for k in range(num_pack, -1, -1):
            quantity[index] = k
            log('    try buying %d packs of (%d,%d)', k, pack_vol, pack_price)
            max_price = buy(index+1, target_vol - k*pack_vol)
            if max_price >= 0:
                return max_price + k*pack_price
            # quantity[index] = 0
        return -1

    return buy(0, N)




N = int(input().strip())
P = list(map(int, input().split()))
assert len(P) == N

print(solve(P))

'''
예제 입력 1
4
1 5 6 7
예제 출력 1
10

echo '4\n1 5 6 7' | python3 11052.py
-> 10

echo '5\n10 9 8 7 6' | python3 11052.py
-> 50

echo '10\n1 1 2 3 5 8 13 21 34 55' | python3 11052.py
-> 55

echo '10\n5 10 11 12 13 30 35 40 45 47' | python3 11052.py
-> 50

echo '4\n5 2 8 10' | python3 11052.py
-> 20

echo '4\n3 5 15 16' | python3 11052.py
-> 18

12
1 1 6 8 11 1 1 1 1 1 1 1
-> 24 틀림! 정답은 25 라고 하는데..
packs: [(1, 1), (2, 1), (3, 6), (4, 8), (5, 11), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1)]
sorted: [(5, 11), (3, 6), (4, 8), (1, 1), (2, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1)]
#0: [], remain 12
    try buying 2 packs of (5,11), 22
#1: [2], remain 2
    try buying 0 packs of (3,6)
#2: [2, 0], remain 2
    try buying 0 packs of (4,8)
#3: [2, 0, 0], remain 2
    try buying 2 packs of (1,1)
#4: [2, 0, 0, 2], remain 0

(5,11)x2 + (1,1)x2 = 24
(5,11)x1 + (3,6)x1 + (4,8)x1 = 25 <- 이게 더 큼.
즉, 단위 가격이 더 높은 것으로 최대치로 채우는 것이 항상 정답은 아니라는 것임!


# 1 3 4 5 6 7 ... 1001

(python3 <<EOF
N = 1000
print(N)
P = [1] * 500 + [ k for k in range(500,N) ]
print(' '.join([ str(e) for e in P ]))
EOF
) | time python3 11052.py


(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 1000
print(N)
unit = 10_000/N
P = [  for k in range(N) ]
print(' '.join([ str(randint(1,10_000)) for k in range(N) ]))
EOF
) | time python3 11052.py
 > /dev/null
/dev/ttys051


'''

