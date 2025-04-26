'''
문제

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

'''

import sys
def log(fmt, *args): print(fmt % args, file=sys.stderr)

MAX = 1000

def solve(A:str, B:str) -> int:
    # A 는 고정하고 B 를 하나씩 늘려가면서 계산해 보자.
    dp = [ -1 ] * len(B)
    '''
        dp: step k 에서 B[:k] 에 대한 lcs 정보
            dp[0]: 길이 1 lcs의 끝자리 문자 인덱스
            dp[1]: 길이 2 lcs의 끝자리 문자 인덱스
            ...
    '''
    for k in range(1, len(B)+1): # k=1~len_b
        # step: k, B[:k] 에 대해서만 고려. 길이 k 의 부분문자열이다.
        #log("step %d, '%s', new char %s", k, B[:k], B[k-1])

        dpk = [-1] * (k) # dpk[0] ~ dpk[k-1]
        # dpk[i] 는 길이 i+1 의 lcs가 존재하는 경우, lcs 마지막 글자의 A 에서의 index
        #          길이 i+1 lcs 가 없으면 -1

        ch = B[k-1] # 이번 step에 새로 추가된 글자

        for i in range(0, k): # i: 0 ~ k-1
            # 길이 i+1 의 lcs 에 대한 정보 구하기.
            # 두가지 경우가 가능함.
            # (1) 직전 단계의 lcs 그대로. 즉, dp[i]
            prev = (dp[i] if i < k-1 else -1)

            # (2) 직전 단계의 하나 짧은 lcs 에 새 글자 ch 붙인 문자열:
            now = -1
            if i == 0:
                now = A.find(ch)
            else:
                last_loc = dp[i-1] # last_loc 은 -1 일 수도 있음.
                if last_loc >= 0:
                    now = A[last_loc+1:].find(ch) # tail 에서만 검색
                    if now >= 0:
                        now += (last_loc + 1)

            # (1) 과 (2) 중 -1 이 아닌 최소값.
            dpk[i] = min(now, prev) if now>=0 and prev>=0 else \
                        now if now>=0 else prev
            #log("  [%d] prev %d, now %d -> %d", i, prev, now, dpk[i])

        dp = dpk

    # find longest lcs
    # log("dp: %s", dp)
    #  if dp[i] >= 0 then lcs of length i+1 exist.
    # lcs_len = [ i+1 for i in range(len(B)) if dp[i]>=0 ]
    # return max(lcs_len)

    for i in range(len(B)-1, -1, -1):
        if dp[i] >= 0: # lcs exist!
            return i+1
    return 0


A = input().strip()
B = input().strip()
print(solve(A, B))


'''
ACAYKP
CAPCAK

echo 'ACAYKP\nCAPCAK' | python3 9251.py

C
    C:1
CA
    2/ CA:2  이건 앞의 C:1 을 참고하여 [2:] 에서 A 를 찾은 결과임.
    1/ C:1(탈락), A:0
CAP
    3/ CAP:5  이건 앞의 CA:2 참고하여 [3:]에서 P 검색
    2/ CA:2, AP:5(x),
    1/ A:0, P:5(x)
CAPC
    4/ CAPC(x)
    3/ CAP:5, CAC(x)
    2/ CA:2(x), AC:1 <--
    1/ A:0, C:1(x)
CAPCA:
    5/
    4/ CAPA(x)
    3/ CAP:5(x), ACA:2
    2/ AC:1, AA:2(x)
    1/ A:0, A:0 (중복)
CAPCAK:
    5/
    4/ ACAK:6
    3/ ACA:2, ACK:6(x)
    2/ AC:1, AK:6(x)
    1/ A:0


'''