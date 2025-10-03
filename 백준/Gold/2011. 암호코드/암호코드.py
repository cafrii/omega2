import sys

MOD = 1_000_000

def get_input():
    input = sys.stdin.readline
    A = input().rstrip()
    return A,

def solve(A:str)->int:
    '''
    Args:  숫자로 이루어진 암호문
    Returns: 해독 가능한 경우의 수
        암호가 잘못되어 암호를 해석할 수 없는 경우에는 0.
    '''
    N = len(A)
    dp = [0] * (N+1)

    dp[0] = 1
    if N >= 1:
        dp[1] = 1 if A[0]!='0' else 0 # 1~9 -> A~J 해독

    for k in range(2, N+1):
        '''
        dp[k] 는 길이 k의 부분 암호문 A[:k] 의 해독 가능한 숫자
        dp[k-1] 에 A[k-1:k] 한 글자 해독의 경우 포함. 0은 유효한 암호 아님.
        dp[k-2] 에 A[k-2:k] 두 글자 해독의 경우 포함. 반드시 두 글자이어야 하므로 10~26 사이의 숫자만 해당.
        '''
        dp[k] = (
            (dp[k-1] if A[k-1]!='0' else 0) # A[k-1]은 0 만 아니라면 A~J 중 하나의 문자로 해독.
            + (dp[k-2] if 10<=int(A[k-2:k])<=26 else 0)
        ) % MOD
    return dp[N]

if __name__ == '__main__':
    print(solve(*get_input()))
