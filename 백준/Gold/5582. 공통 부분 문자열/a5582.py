'''
5582번
공통 부분 문자열, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	22970	9598	7579	43.294%

문제
두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.

어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다.
예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다.
하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.

두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다.
이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다.
또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

입력
첫째 줄과 둘째 줄에 문자열이 주어진다. 문자열은 대문자로 구성되어 있으며, 길이는 1 이상 4000 이하이다.

출력
첫째 줄에 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이를 출력한다.

--------
8:59~

메모리 초과 문제가 있음.
문제에서 주어진 메모리 제약 조건: 256MB

dp 배열 크기 추정: 4K * 4K * sizeof(int) = 16M * sz(int 16?) = 256M
int 저장에 16바이트 이상이라면 딱 맞긴 한데, list 자체의 overhead 등도 감안하면 문제가 될 수 있겠음.
모든 dp 이력을 다 저장할 필요 없고, 직전 하나만 필요하긴 함.
또한 iteration 순서를 잘 잡으면 dp row 하나로도 해결 가능할 수도. 그런데 이렇게 까지 할 필요는 없어 보임.

dp를 두 row 까지 사용하는 방식으로 구현 후 pass.

--------
빠른 수행 기록들

98971565 gcn8099     5582 맞았습니다!! 33432KB 1916ms Python 3 487B
95727168 regk040918  5582 맞았습니다!! 32412KB 1540ms Python 3 315B
68503474 line1029    5582 맞았습니다!! 32140KB  132ms Python 3 1319B  <- fastest

가장 빠른 세번째 해는 Manber-Myers Algorithm 이라고 하는 특별한 방법을 사용했다고 주석에 설명됨.

https://www.acmicpc.net/source/68503474

알고리즘에 대한 이해가 없다면 코드를 봐도 무슨 내용인지 이해가 안됨. 그냥 pass.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

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


def solve(A:str, B:str):
    '''
    문제에서 주어진 메모리 제약 조건: 256MB

    dp 배열 크기 추정: 4K * 4K * sizeof(int) = 16M * sz(int 16?) = 256M
    int 저장에 16바이트 이상이라면 딱 맞긴 한데, list 자체의 overhead 등도 감안하면 문제가 될 수 있겠음.
    모든 dp 이력을 다 저장할 필요 없고, 직전 하나만 필요하긴 함.
    또한 iteration 순서를 잘 잡으면 dp row 하나로도 해결 가능할 수도. 그런데 이렇게 까지 할 필요는 없어 보임.
    dp를 두 row 까지 사용하는 방식으로 구현.
    dp:  직전 dp
    dpx: 이번에 계산해야 하는 dp

    '''
    Nb = len(B)
    dp = [0] * (Nb+1)
    # dp 에 대한 설명은 앞 코드 참고.

    maxlen = 0

    for a in A:
        dpx = [0] * (Nb+1) # dp for next

        for k in range(1, Nb+1): # k: 1 ~ Nb
            if a == B[k-1]:
                dpx[k] = dp[k-1]+1

        maxlen = max(maxlen, max(dpx))
        dp = dpx

    return maxlen


def solve_fast(A:str, B:str):
    '''
    '''
    Nb = len(B)
    dp = [0] * (Nb+1)
    # dp 에 대한 설명은 앞 코드 참고.

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
    # r = solve(*get_input())
    # print(r)
    # print(solve(*get_input()))
    print(solve_fast(*get_input()))


'''
예제 입력 1
ABRACADABRA
ECADADABRBCRDARA
예제 출력 1
5
예제 입력 2
UPWJCIRUCAXIIRGL
SBQNYBSBZDFNEV
예제 출력 2
0

----
run=(python3 a5582.py)

echo 'ABRACADABRA\nECADADABRBCRDARA' | $run
# 5
echo 'UPWJCIRUCAXIIRGL\nSBQNYBSBZDFNEV' | $run
# 0

echo 'ajsdfjywefakjhsdfgkauywgdakhjgkawegdkawyegdkajhgdkywgde\nsdfagsjfytwejfhagdfjawygdfkuayewgdkasjhfgkwayegfkajhdf' | $run
# 4

'''

#-------------------------

import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    seed(time.time())
    seed(43)
    N = int(os.getenv('_N', '100'))
    A = ''.join(chr(ord('A')+randint(0,25)) for _ in range(N))
    B = ''.join(chr(ord('A')+randint(0,25)) for _ in range(N))
    return A,B

def test():
    A,B = gen_worstcase_input()
    print(A, B, sep='\n')


'''

_N=4000 python3 -c "from a5582 import test; test()" | time $run
# 4,  seed(43) 일때.
# $run  0.80s user 0.02s system 99% cpu 0.829 total   <- 0.8 초, ok.


'''