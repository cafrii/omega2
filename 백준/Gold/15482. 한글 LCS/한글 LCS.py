
def get_input():
    # input = sys.stdin.readline
    # utf-8 자동 변환 기능을 활용하기 위해서는 original input() 함수가 필요.
    A = input().rstrip()
    B = input().rstrip()
    return A,B

def solve(A:str, B:str)->int:
    '''
    '''
    Na,Nb = len(A),len(B)

    # 일반 lcs 풀이와 동일하게 진행.
    dp = [ [0]*(Nb+1) for _ in range(Na+1) ]

    for ka in range(1, Na+1):
        for kb in range(1, Nb+1):
            if A[ka-1] == B[kb-1]:
                dp[ka][kb] = dp[ka-1][kb-1] + 1
            else:
                dp[ka][kb] = max(dp[ka-1][kb], dp[ka][kb-1])

    return dp[Na][Nb]

if __name__ == '__main__':
    print(solve(*get_input()))
