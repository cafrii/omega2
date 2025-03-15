'''
2096번

내려가기

2025/3/15, 메모리 초과 1회 실패 후 성공.


시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	4 MB (하단 참고)	53001	20453	16008	36.759%

문제
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데,
이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다.
그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다.
바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다.
이 제약 조건을 그림으로 나타내어 보면 다음과 같다.


별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며,
빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다.
숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오.
점수는 원룡이가 위치한 곳의 수의 합이다.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다.
숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

출력
첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

'''


import sys

MAX_N = 100_000

def solve_memoryoverflow(A: list[list[int]]):
    # 각 step 단계에서:
    #  smax[k]: k 위치에서 마지막으로 끝난 경우 최대 스코어. (k=0 or 1 or 2)
    #  smin[k]: k 위치에서 마지막으로 끝난 경우 최소 스코어.
    #
    # 첫번째 단계는 그냥 입력 값 그 자체.
    smax = A[0].copy()
    smin = A[0].copy()
    # print(f'(0)', smax, smin)

    for k in range(1, len(A)):
        a0, a1, a2 = A[k]
        # update max
        smax = [
            max(smax[0], smax[1]) + a0,
                # 0 위치에서 끝나려면 이전 단계의 0, 또는 1 에서 끝나야 함.
            max(smax) + a1,
                # 1 위치는 이전 단계 어디에서든 올 수 있음.
            max(smax[1], smax[2]) + a2,
        ]
        # update min
        smin = [
            min(smin[0], smin[1]) + a0,
            min(smin) + a1,
            min(smin[1], smin[2]) + a2,
        ]
        # print(f'({k})', smax, smin)

    return max(smax), min(smin)


'''
메모리 제한이 있으므로, A를 미리 받아서 저장하지 않고 입력 받으면서 계산한다.
'''
def solve(N:int):
    # 각 step 단계에서:
    #  smax[k]: k 위치에서 마지막으로 끝난 경우 최대 스코어. (k=0 or 1 or 2)
    #  smin[k]: k 위치에서 마지막으로 끝난 경우 최소 스코어.
    #

    # 첫번째 단계는 그냥 입력 값 그 자체.
    smax = list(map(int, input().strip().split()))
    smin = smax.copy()

    for k in range(1, N):
        # a = list(map(int, input().strip().split()))
        # a0, a1, a2 = a
        a0, a1, a2 = map(int, input().strip().split())

        # update max
        smax = [
            max(smax[0], smax[1]) + a0,
                # 0 위치에서 끝나려면 이전 단계의 0, 또는 1 에서 끝나야 함.
            max(smax) + a1,
                # 1 위치는 이전 단계 어디에서든 올 수 있음.
            max(smax[1], smax[2]) + a2,
        ]
        # update min
        smin = [
            min(smin[0], smin[1]) + a0,
            min(smin) + a1,
            min(smin[1], smin[2]) + a2,
        ]
        # print(f'({k})', smax, smin)

    return max(smax), min(smin)


def main_overflow():
    N = int(input().strip())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().strip().split())))
    m1,m2 = solve_memoryoverflow(A)
    print(m1,m2)

def main():
    N = int(input().strip())
    m1,m2 = solve(N)
    print(m1,m2)


import tracemalloc
tracemalloc.start()
main()
print(tracemalloc.get_traced_memory(), file=sys.stderr) # current, peak
tracemalloc.stop()



'''
예제 입력 1
3
1 2 3
4 5 6
4 9 0
예제 출력 1
18 6

예제 입력 2
3
0 0 0
0 0 0
0 0 0
예제 출력 2
0 0

timeout simulation

(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 10_000
print(N)
for _ in range(N):
    a = [ str(randint(0, 9)) for _ in range(3) ]
    print(' '.join(a))
EOF
) | time python3 a.py

python3 a.py  0.31s user 0.02s system 99% cpu 0.335 total

'''