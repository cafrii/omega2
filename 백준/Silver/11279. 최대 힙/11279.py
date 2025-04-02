'''


'''

import sys
input = sys.stdin.readline

bt = [0] # binary tree

N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(bt) < 2:
            print(0)
            continue

        print(bt[1]) # print max
        bt[1] = bt[-1]
        bt.pop()

        # and re-balance tree
        k = 1
        while 2*k < len(bt): # 최소한 하나의 자식은 존재하는 동안은 반복
            if len(bt) <= 2*k+1: # 두 자식은 아닌 경우. 즉 단일 자식
                if bt[k] < bt[2*k]: # 자식이 더 크면 교환
                    bt[k], bt[2*k] = bt[2*k], bt[k]
                break # 더 이상의 자식은 없으니 종료.

            # 두 자식 중 더 큰 자식을 선택
            bigger = 2*k if bt[2*k] > bt[2*k+1] else 2*k+1
            if bt[k] < bt[bigger]: # 큰 자식이 본인보다 더 크면 교환
                bt[k], bt[bigger] = bt[bigger], bt[k]
                k = bigger
            else: # 본인이 자식보다 더 크면 리밸런싱 종료
                break
        print(bt, file=sys.stderr)
    else:
        bt.append(x) # 새 값을 맨 아래에 추가하고
        k = len(bt) - 1
        # 리밸런싱
        while k > 1:
            if bt[k] <= bt[k//2]: # 자식인 내가 부모보다 더 크지 않다면 종료
                break
            bt[k], bt[k//2] = bt[k//2], bt[k]
            k //= 2
        print(bt, file=sys.stderr)


'''
예제 입력 1
13
0
1
2
0
0
3
2
1
0
0
0
0
0
예제 출력 1
0
2
1
3
2
1
0
0


시간초과 시뮬레이션

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
MAX_N,MAX_D = 100_000,10000
N = MAX_N
print(N)
for _ in range(N):
    if randint(0,100) < 60:
        print(0)
    else:
        print(randint(0, MAX_D))
EOF
) | time python3 11279.py > /dev/ttys019 2> /dev/null



'''


