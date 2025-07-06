'''
1622번
공통 순열 성공다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	2797	766	589	28.634%

문제
알파벳 소문자로 이루어진 두 문자열 a와 b에 대해,
a의 부분 수열의 순열이자 b의 부분 수열의 순열이 되는 가장 긴 문자열 x를 구하여라.

입력
각각의 입력은 한 쌍의 줄로 이루어져 있다.

첫 줄에는 문자열 a가 두 번째 줄에는 문자열 b가 주어진다.

각각의 문자열은 줄로 구분되며, 최대 1000개의 알파벳 소문자로 이루어졌다.

출력
각각의 입력에 대해, x를 출력한다.

가능한 x가 여러 개 존재하는 경우, 사전순으로 가장 앞에 오는 것을 출력한다.

------

"부분 수열" 로 검색하여 관련 된 문제 같이 몰아서 풀기.

'''


import sys
input = sys.stdin.readline


# 문제를 잘못 이해 했음.
def solve_wrong(A:str, B:str)->str:
    '''
    '''

    cur_max_depth = sys.getrecursionlimit()
    if cur_max_depth < 2000:
        sys.setrecursionlimit(2000)

    def find_lcs(A:str, B:str)->str:
        if len(A)==0 or len(B)==0:
            return ''
        # pick any a in A
        res = []
        for i in range(len(A)):
            j = B.find(A[i])
            if j<0: continue
            res.append(A[i] + find_lcs(A[i+1:], B[j+1:]))
        if res:
            res.sort()
            return res[0]
        else:
            return ''

    return find_lcs(A, B)




def solve_slow(A:str, B:str)->str:
    '''
    최대 길이가 1000 이므로 brute force search 로 시간 내 풀수 있을까?
    재귀 호출 사용.
    '''

    def find_lcs(A:str, B:str)->str:
        if len(A)==0 or len(B)==0:
            return ''
        # pick any a in A
        res = []
        for i in range(len(A)):
            j = B.find(A[i])
            if j<0: continue
            res.append(A[i] + find_lcs(A[i+1:], B[j+1:]))
        if res:
            res.sort()
            return res[0]
        else:
            return ''

    sa = ''.join(sorted(A))
    sb = ''.join(sorted(B))

    return find_lcs(sa, sb)



def solve(A:str, B:str)->str:
    '''
    '''
    ha,hb = [0]*26,[0]*26  # alphabet histogram of string a,b

    for a in A:
        id = ord(a)-ord('a')
        ha[id] += 1
    for b in B:
        id = ord(b)-ord('a')
        hb[id] += 1

    # find common of both
    hc = [ min(ha[k], hb[k]) for k in range(26) ]

    # generate
    result = []
    for i in range(26):
        if not hc[i]: continue
        result.extend([chr(ord('a') + i)]*hc[i])

    return ''.join(result)


while True:
    try:
        A,B = input(),input()
    except EOFError:
        break
    # for readline, it returns empty string at EOF.
    if A == "" or B == "":
        break
    A,B = A.strip(),B.strip()
    print(solve(A, B))


'''
예제 입력 1
pretty
women
walking
down
the
street

예제 출력 1
e
nw
et


run=(python3 1622.py)

echo 'pretty\nwomen\nwalking\ndown\nthe\nstreet' | $run
-> e nw et

echo 'women\nwalking' | $run
-> nw




(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
T = 1
for _ in range(T):
    L1,L2 = randint(0,1000),randint(999,1000)
    print(''.join([ chr(ord('a') + randint(0,25)) for _ in range(L1) ]))
    print(''.join([ chr(ord('a') + randint(0,25)) for _ in range(L2) ]))
EOF
) | time $run



'''
