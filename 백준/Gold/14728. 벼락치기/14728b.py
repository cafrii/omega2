'''

2d dp array 로 풀이.


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


def solve_dp2d(N:int, T:int, A:list[tuple[int,int]])->int:
    '''
        N: 시험 단원 수
        T: 주어진 총 공부 시간 (budget)
        A: 과목 정보 [ (reqt, score), .. ]
            reqt: required study time
            score:
    '''
    dp = [ [0] * (T+1) for _ in range(N+1) ]
    # dp[n][t] 는 과목 n개로 공부시간 t가 주어졌을 때의 얻을 수 있는 최고 점수

    for n in range(1, N+1):
        # 각 과목 별로 하나씩 검토.
        reqt, score = A[n-1]
        # if reqt > T: continue

        for t in range(T+1):
            if t < reqt:
                dp[n][t] = dp[n-1][t]
            else:
                dp[n][t] = max(
                    dp[n-1][t], # 이 과목을 공부하지 않는 경우. 그냥 이전 점수 유지.
                    dp[n-1][t-reqt] + score, # 이 과목을 선택
                )
        # log("dp: %s", dp[n])

    return dp[N][T]


if __name__ == '__main__':
    inp = get_input()
    r = solve_dp2d(*inp)
    print(r)


'''

run=(python3 14728b.py)

echo '3 310\n50 40\n100 70\n200 150' | $run
# 220


'''

