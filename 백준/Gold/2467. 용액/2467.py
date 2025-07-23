'''
2467번
용액 성공스페셜 저지

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	53850	21049	16153	37.668%

문제
KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다.
각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고,
알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

예를 들어, 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는
특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고,
이 용액의 특성값이 0에 가장 가까운 용액이다.
참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로
특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때,
이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

입력
첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하의 정수이다.
둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 오름차순으로 입력되며,
이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다.
N개의 용액들의 특성값은 모두 서로 다르고,
산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

출력
첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다.
출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다.
특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.


----

4:00~



'''


import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().strip())
    # N: 2 ~ 100_000
    A = list(map(int, input().split()))
    assert len(A) == N, "wrong length"
    return A


MAX_SUM = 1_000_000_000*2 + 1

def solve_bruteforce(A:list[int])->tuple[int,int]:
    '''
    N 최대 값이 100,000 으로 꽤 큰 편이고, N2 루프로는 timeout 될 것임.
    '''
    N = len(A)
    min_sum = MAX_SUM
    min_sum_pair:tuple[int,int] = (0,0)
    for j in range(N):
        for k in range(j+1,N):
            sum1 = abs(A[j]+A[k])
            if sum1 <= min_sum:
                min_sum,min_sum_pair = sum1,(A[j],A[k])
    return min_sum_pair


def solve_twopointer(A:list[int])->tuple[int,int]:
    '''
    투 포인터 기법.
    '''
    N = len(A)
    min_sum = MAX_SUM
    min_sum_pair:tuple[int,int] = (0,0)

    s,e = 0,N-1 # two index
    while s < e:
        sum1 = A[s]+A[e]
        if sum1 == 0:
            return (A[s],A[e])
        sum2 = abs(sum1)
        if sum2 < min_sum:
            min_sum,min_sum_pair = sum2,(A[s],A[e])
        if sum1 < 0:
            s += 1
        else:
            e -= 1
    return min_sum_pair


if __name__ == '__main__':
    inp = get_input()
    # print(inp)
    # print(*solve_bruteforce(inp))
    print(*solve_twopointer(inp))




'''
예제 입력 1
5
-99 -2 -1 4 98
예제 출력 1
-99 98
예제 입력 2
4
-100 -2 -1 103
예제 출력 2
-2 -1

run=(python3 2467.py)


echo '5\n-99 -2 -1 4 98' | $run
echo '4\n-100 -2 -1 103' | $run
-> -99 98
-> -2 -1



(python3 <<EOF
import time,os
from random import seed,randint
seed(time.time())
# seed(43)

N,MAXVAL = 100_000, 1_000_000_000
# N,MAXVAL = 10, 100   # for simple test

A = [ randint(-MAXVAL, MAXVAL) for k in range(N) ]
# A = [ randint(-MAXVAL//2, MAXVAL) for k in range(N) ]

A.sort()

print(N)
print(' '.join(map(str, A)))
EOF
) | time $run

bruteforce
->
$run  290.42s user 1.00s system 99% cpu 4:54.08 total

two pointer
->
$run  0.03s user 0.01s system 36% cpu 0.086 total

'''
