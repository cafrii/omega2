'''
25427번
DKSH를 찾아라, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	989	442	343	46.922%

문제
준혁이는 DKSH(단국대학교부속소프트웨어고등학교)에 다니는 학생이다.
어느 날, 준혁이는 길을 걷다가 N 개의 알파벳 대문자가 써있는 종이를 발견했다.
평소에 자신이 DKSH에 다니는 학생이라는 것을 자랑스러워하던 준혁이는
이 종이에서 네 개의 문자를 골라서 그 문자들을 제외한 나머지 문자를 전부 지웠을 때 "DKSH"가 되도록 하려고 한다.
준혁이는 이렇게 네 개의 문자를 고르는 방법의 수를 세어 보기로 했다.
하지만 영어울렁증이 있는 준혁이는 금방 포기해버리고 말았다.
준혁이를 도와 네 개의 문자를 골라 나머지 문자를 전부 지웠을 때 "DKSH"가 되는 경우의 수를 세어 주자.(큰 따옴표 제외)
정확히는, 문자열에서 a번째 문자가 'D', b번째 문자가 'K', c번째 문자가 'S', d번째 문자가 'H'이고
a<b<c<d인 순서쌍 (a, b, c, d)의 갯수를 찾자.

입력
첫째 줄에 N이 주어진다. (1≤N≤100,000)

둘째 줄에 길이 N의 문자열 S가 주어진다. (S는 알파벳 대문자로만 이루어져 있다.)

출력
첫째 줄에 문제에서 설명한 순서쌍 (a, b, c, d)의 갯수를 출력한다.


--------

11:59~12:7

잘 보니까 dpx 를 도입할 필요도 없어 보인다.
-> solve2 로 개선.

'''


import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    S = input().rstrip()
    assert len(S)==N
    return N,S

def solve(N:int, S:str)->int:
    '''
    Args:
    Returns:
    '''
    # dp = [ [0]*4 for _ in range(N+1) ]
    dp = [0]*4

    for i,s in enumerate(S):
        dpx = dp[:] # dp for next
        if s == 'D':
            dpx[0] += 1
        elif s == 'K':
            dpx[1] += dp[0]
        elif s == 'S':
            dpx[2] += dp[1]
        elif s == 'H':
            dpx[3] += dp[2]
        dp = dpx

    return dp[3]

'''
    앞의 solve()를 좀 더 최적화.
    dp의 업데이트 순서를 조정하면 dpx 를 따로 마련할 필요가 없어진다.
'''
def solve2(N:int, S:str)->int:
    '''
    Args:
    Returns:
    '''
    dp = [0]*4

    for s in S:
        if s == 'H':
            dp[3] += dp[2]
        elif s == 'S':
            dp[2] += dp[1]
        elif s == 'K':
            dp[1] += dp[0]
        elif s == 'D':
            dp[0] += 1

    return dp[3]


if __name__ == '__main__':
    print(solve2(*get_input()))



'''
예제 입력 1
11
DABKCDSEFHH
예제 출력 1
2

----
pr=25427
run=(python3 a$pr.py)

echo '11\nDABKCDSEFHH' | $run
# 2

echo '1\nX' | $run
# 0
echo '4\nDKSH' | $run
# 1

echo '8\nDDKKSSHH' | $run
# 16

'''

