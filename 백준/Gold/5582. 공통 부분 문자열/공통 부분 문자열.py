import sys

def get_input():
    input = sys.stdin.readline
    A = input().rstrip()
    B = input().rstrip()
    return A,B

def solve_memoryfail(A:str, B:str):
    '''
    '''
    Na,Nb = len(A),len(B)
    dp = [ [0]*(Nb+1) for _ in range(Na+1) ]
    # dp[j][k]: A[j-1], B[k-1] 위치에서 "종료"되는 문자열 중 LCS (가장 긴 공통 부분문자열)의 길이
    #           계산 편의를 위해 dp[0][*], dp[*][0]은 0으로 설정후 비워둔다.

    for j in range(1, Na+1):
        a = A[j-1]
        for k in range(1, Nb+1):
            if a == B[k-1]:
                dp[j][k] = dp[j-1][k-1]+1

    # find maximum lcs
    maxlen = 0
    for x in dp:
        maxlen=max(maxlen, max(x))
    return maxlen
    # return max(max(x) for x in dp) # faster?

def solve_fast(A:str, B:str):
    '''
    문제에서 주어진 메모리 제약 조건: 256MB

    dp 배열 크기 추정: 4K * 4K * sizeof(int) = 16M * sz(int 16?) = 256M
    int 저장에 16바이트 이상이라면 딱 맞긴 한데, list 자체의 overhead 등도 감안하면 문제가 될 수 있겠음.
    모든 dp 이력을 다 저장할 필요 없고, 직전 하나만 필요하긴 함.
    또한 iteration 순서를 잘 잡으면 dp row 하나로도 해결 가능할 수도. 그런데 이렇게 까지 할 필요는 없어 보임.
    dp를 두 row 만 사용하는 방식으로 구현.
    dp:  직전 dp
    dpx: 이번에 계산해야 하는 dp
    '''
    Nb = len(B)
    dp = [0] * (Nb+1)
    maxlen = 0
    for a in A:
        dpx = [0] * (Nb+1) # dp for next
        i = -1  # B[0] 부터 검색을 시작하도록 하기 위해.
        while True: # for 대신 find 메소드 사용
            i = B.find(a, i+1)  # 직전 찾은 위치 다음 위치부터 검색.
            if i >= 0:
                dpx[i+1] = dp[i] + 1
                # 이전 구현 기준으로 하면 i+1=k 이다.
            else:
                break
        maxlen = max(maxlen, max(dpx))
        dp = dpx
    return maxlen

if __name__ == '__main__':
    print(solve_fast(*get_input()))
