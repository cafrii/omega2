
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

    for i in range(len(B)-1, -1, -1):
        if dp[i] >= 0: # lcs exist!
            return i+1
    return 0


A = input().strip()
B = input().strip()
print(solve(A, B))

