'''
16500번
문자열 판별 성공, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	6563	1992	1489	32.740%

문제
알파벳 소문자로 이루어진 문자열 S와 단어 목록 A가 주어졌을 때,
S를 A에 포함된 문자열을 한 개 이상 공백없이 붙여서 만들 수 있는지 없는지 구하는 프로그램을 작성하시오.
A에 포함된 단어를 여러 번 사용할 수 있다.

입력
첫째 줄에 길이가 100이하인 문자열 S가 주어진다.
둘째 줄에는 A에 포함된 문자열의 개수 N(1 ≤ N ≤ 100)이 주어진다.
셋째 줄부터 N개의 줄에는 A에 포함된 단어가 한 줄에 하나씩 주어진다.
A에 포함된 문자열은 알파벳 소문자로만 이루어져 있고, 길이는 100을 넘지 않는다.

출력
A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0을 출력한다.

----

10:47~11:05, bf -> timeout 실패

greedy 방식 으로는 정답을 찾을 수 없을 것이 자명하다.
모든 가능한 경우를 다 찾아보는 bf (brute-force) 탐색으로 시도해 보자.
일치하는 단어만 골라서 시도하는 것이므로 경우의 수가 그리 많지 않을 듯.
물론 최악의 경우는 100! 라고 보면 말도 안되게 큰 수이긴 하지만...

일부러 match 되는 후보들만 의도적으로 앞에 몰아 배치하면 분기 수가 너무 늘어나서 timeout 발생.

----
dp 방법으로 접근, 구현, worst case 성능 확인, 제출 확인.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    S = input().rstrip()
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        A.append(input().rstrip())
    return S,N,A

def solve_bruteforce(S:str, N:int, A:list[str])->int:
    '''
    Returns: 1 if we can compose S, or 0.
    -> 이 방법은 timeout 실패
    '''
    # lm = sys.getrecursionlimit()
    # log("lm: %d", lm)
    # sys.setrecursionlimit(lm + 10)

    def check(idx:int)->bool:
        '''
        idx: index of S, where we will check match
        returns false if failed to match
        '''
        # S[idx:]
        remain = len(S) - idx
        if remain <= 0: return False
        for i,a in enumerate(A):
            sz = len(a)
            if sz > remain: continue
            if S[idx:idx+sz] != a: continue
            if sz == remain: return True
            r = check(idx + sz)
            if r: return True
        return False

    r = check(0)
    return 1 if r else 0


def solve_dp(S:str, N:int, A:list[str])->int:
    '''
    Returns: 1 if we can compose S, or 0.
    '''

    # A 전처리. 중복 제거, 해싱
    # A2 = {}
    # for a in A: A2[a] = 1
    A2 = set(A)
    log("A2: %s", A2)

    dp = [0] * (len(S)+1)
    # dp[k] 는 길이 k 의 S 부분 문자열, 즉 S[:k] 만 대상으로 할 때의 답.
    # 값: 1 이면 성공 (즉, A로 S[:k] 구성 가능), 0 이면 실패.
    dp[0] = 1  # 길이 0 (빈 문자열) 은 항상 구성이 가능하다고 간주

    for k in range(1, len(S)+1):
        log("k %d: dp %s", k, dp)

        # dp[k] 를 결정하려면 아래 조건 중 "하나라도 맞으면" ok.
        #     dp[k-1] 에 한글자짜리 a 를 붙여 일치 여부 확인되면 ok.
        #     dp[k-2] 에 두 글자짜리 a 찾아서 검사.
        #     ...
        #     dp[0]   ...
        #
        for j in range(k-1, -1, -1): # j: k-1 ~ 0
            if dp[j] == 0: continue
            log("   j %d, '%s'", j, S[j:k])
            if S[j:k] not in A2: continue
            dp[k] = 1
            break # 어느 하나만 일치하는게 발견되면 추가 검사는 무의미

    log("final dp %s", dp)
    return dp[len(S)]


if __name__ == '__main__':
    # print(solve_bruteforce(*get_input()))
    print(solve_dp(*get_input()))


'''
예제 입력 1
softwarecontest
2
software
contest
예제 출력 1
1

----
run=(python3 a16500.py)

echo 'softwarecontest\n2\nsoftware\ncontest' | $run
# 1

echo 'aaaa\n1\na' | $run
# 1
echo 'aaaa\n2\na\nb' | $run
# 1
echo 'aaaa\n3\na\na\nb' | $run
# 1
echo 'abcd\n1\na' | $run
# 0
echo 'abcd\n4\na\nbc\nd\nbcd' | $run
# 1


echo 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n1\na' | time $run
# 1


'''

import time,os
from random import seed,randint,shuffle

# 만들고 보니, worst case 가 안됨.
def gen_worstcase_input():
    seed(time.time())
    seed(43)
    S = 'a' * 100
    N = int(os.getenv('_N', '100'))
    A = []
    for _ in range(99): # b ~ z 로만 구성된 100 글자의 단어 99개
        a = ''.join( chr(randint(1,25) + ord('a')) for _ in range(100) )
        A.append(a)
    A.append('a')
    return S,N,A

def gen_worstcase_input2():
    seed(time.time())
    seed(43)
    # z 없는 랜덤 문자열 + 마지막 z
    S = ''.join( chr(randint(0,25) + ord('a')) for _ in range(99) ) + 'z'
    N = int(os.getenv('_N', '100'))
    A = []
    # 앞의 50개는 S 의 substring
    for k in range(50):
        A.append(S[:k+1])
    # 뒤의 50개는 랜덤 알파벳
    for k in range(50):
        a = chr(randint(0,25) + ord('a'))
        A.append(a)
    return S,N,A

def test():
    S,N,A = gen_worstcase_input2()
    print(S)
    print(N)
    print('\n'.join(A))


'''
python3 -c "from a16500 import test; test()" | time $run

# N=100 으로 하고, worst case 2
# 0
# $run  9.02s user 0.03s system 99% cpu 9.079 total

----
# dp 방식으로 개선 후
python3 -c "from a16500 import test; test()" | time $run

# N=100 으로 하고, worst case 2
# 0
# $run  0.02s user 0.01s system 43% cpu 0.070 total

'''

