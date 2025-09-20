import sys

def get_input():
    input = sys.stdin.readline
    S = input().rstrip()
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(input().rstrip())
    return S,N,A

def solve_dp(S:str, N:int, A:list[str])->int:
    '''
    Returns: 1 if we can compose S, or 0.
    '''
    A2 = set(A) # A 전처리. 중복 제거, 해싱

    dp = [0] * (len(S)+1)
    # dp[k] 는 길이 k 의 S 부분 문자열, 즉 S[:k] 만 대상으로 할 때의 답.
    # 값: 1 이면 성공 (즉, A로 S[:k] 구성 가능), 0 이면 실패.
    dp[0] = 1  # 길이 0 (빈 문자열) 은 항상 구성이 가능하다고 간주

    for k in range(1, len(S)+1):
        # dp[k] 를 결정하려면 아래 조건 중 "하나라도 맞으면" ok.
        #     dp[k-1] 에 한글자짜리 a 를 붙여 일치 여부 확인되면 ok.
        #     dp[k-2] 에 두 글자짜리 a 찾아서 검사.
        #     ...
        #     dp[0]   ...
        for j in range(k-1, -1, -1): # j: k-1 ~ 0
            if dp[j] == 0: continue
            if S[j:k] not in A2: continue
            dp[k] = 1
            break # 어느 하나만 일치하는게 발견되면 추가 검사는 무의미

    return dp[len(S)]

if __name__ == '__main__':
    print(solve_dp(*get_input()))

