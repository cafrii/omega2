'''
14728번
벼락치기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	8179	4492	3696	54.747%

문제
ChAOS(Chung-ang Algorithm Organization and Study) 회장이 되어 일이 많아진 준석이는
시험기간에도 일 때문에 공부를 하지 못하다가 시험 전 날이 되어버리고 말았다.
다행히도 친절하신 교수님께서 아래와 같은 힌트를 시험 전에 공지해 주셨다. 내용은 아래와 같다.

여러 단원을 융합한 문제는 출제하지 않는다.
한 단원에 한 문제를 출제한다. 단, 그 단원에 모든 내용을 알고 있어야 풀 수 있는 문제를 낼 것이다.
이런
두가지 힌트와 함께 각 단원 별 배점을 적어 놓으셨다.
어떤 단원의 문제를 맞추기 위해서는 그 단원의 예상 공부 시간만큼, 혹은 그보다 더 많이 공부하면 맞출 수 있다고 가정하자.
이때, ChAOS 회장 일로 인해 힘든 준석이를 위하여 남은 시간 동안 공부해서 얻을 수 있는 최대 점수를 구하는 프로그램을 만들어 주도록 하자.

입력
첫째 줄에는 이번 시험의 단원 개수 N(1 ≤ N ≤ 100)과 시험까지 공부 할 수 있는
총 시간 T(1 ≤ T ≤ 10000)가 공백을 사이에 두고 주어진다.

둘째 줄부터 N 줄에 걸쳐서 각 단원 별 예상 공부 시간 K(1 ≤ K ≤ 1000)와
그 단원 문제의 배점 S(1 ≤ S ≤ 1000)가 공백을 사이에 두고 주어진다.

출력
첫째 줄에 준석이가 얻을 수 있는 최대 점수를 출력한다.


--------

9:45~10:08


--------
14728.py

14728b.py
처음 2d dp로 풀이했던 것.


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,T = map(int, input().split())
    A = []
    for _ in range(N):
        k,s = map(int, input().split())
        A.append((k, s)) # required study time, score
    return N,T,A


def solve_dp(N:int, T:int, A:list[tuple[int,int]])->int:
    '''
        N: 시험 단원 수
        T: 주어진 총 공부 시간 (budget)
        A: 과목 정보 [ (reqt, score), .. ]
            reqt: required study time
            score:
    '''
    dp = [0] * (T+1)
    # dp[t] 는 공부시간 t가 주어졌을 때의 얻을 수 있는 최고 점수

    for reqt,score in A:
        # 각 과목 별로 하나씩 검토.
        if reqt > T: continue

        dp2 = dp[:] # clone

        for t in range(reqt, T+1):
            dp2[t] = max(
                dp[t], # 이 과목을 공부하지 않는 경우. 그냥 이전 점수 유지.
                dp[t-reqt] + score, # 이 과목을 선택
            )
        # log("dp: %s", dp2)
        dp = dp2
    return dp[T]


def solve_opt(N:int, T:int, A:list[tuple[int,int]])->int:
    '''
        N: 시험 단원 수
        T: 주어진 총 공부 시간 (budget)
        A: 과목 정보 [ (reqt, score), .. ]
            reqt: required study time
            score:
    '''
    dp = [0] * (T+1)
    # dp[t] 는 공부시간 t가 주어졌을 때의 얻을 수 있는 최고 점수
    for reqt,score in A: # 각 과목 별로 하나씩 검토.
        if reqt > T: continue
        for t in range(T, reqt-1, -1):
            dp[t] = max(
                dp[t], # 이 과목을 공부하지 않는 경우. 그냥 이전 점수 유지.
                dp[t-reqt] + score, # 이 과목을 선택
            )
    return dp[T]


if __name__ == '__main__':
    inp = get_input()
    # r = solve_dp(*inp)
    r = solve_opt(*inp)
    print(r)


'''
예제 입력 1
3 310
50 40
100 70
200 150

예제 출력 1
220

----

run=(python3 14728.py)

echo '3 310\n50 40\n100 70\n200 150' | $run
# 220

echo '1 100\n200 10' | $run
# 0

echo '1 100\n100 10' | $run
# 10

echo '1 100\n90 10' | $run
# 10

echo '2 100\n90 10\n80 20' | $run
# 20

echo '20 100\n2 85\n6 14\n8 59\n5 11\n2 18\n1 32\n5 6\n6 91\n1 36\n3 64\n7 24\n9 48\n9 87\n10 10\n5 31\n6 58\n9 44\n8 78\n9 72\n5 62' | $run
# 906


----
export _N=100
export _T=10000

(python3 <<EOF
import time, os
from random import seed,randint
# seed(time.time())
seed(43)
N = int(os.getenv('_N','10'))
T = int(os.getenv('_T','100'))
print(N,T)
for _ in range(N):
    print(randint(1,max(10,T//10)), randint(1,100) )
    # print(randint(1,100),1)
EOF
) | time $run



'''

