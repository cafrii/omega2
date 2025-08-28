
import sys

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
        dp = dp2
    return dp[T]

if __name__ == '__main__':
    inp = get_input()
    r = solve_dp(*inp)
    print(r)
