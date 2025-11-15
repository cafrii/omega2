'''
28449번
누가 이길까, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	1386	506	389	36.977%

문제
HI-ARC는 종강을 맞아 HI팀과 ARC팀으로 나누어 친선대회를 열려고 한다.
HI팀엔 N명 ARC팀엔 M명이 속해있다.
대회는 다른 팀끼리 모든 사람들끼리 한번씩 대결을 하는 것으로,
대회는 N x M개의 대결로 이루어진다.
모든 참가자는 코딩실력을 가지고 있다.
대결을 하면 더 높은 코딩실력을 가진 참가자가 승리하고, 두 참가자의 코딩실력이 같다면 무승부가 된다.

하얔이는 이 대회의 결과를 빨리 알고싶어졌다. 하얔이를 위해 대회의 결과를 예측해보자!

입력
첫째 줄에 HI팀의 인원 수 N, ARC팀의 인원 수 M이 공백으로 구분되어 정수로 주어진다.
(1 <= N, M <= 100,000)

둘째 줄에 HI팀의 참가자의 코딩실력을 나타내는 길이 N 수열 a가 공백으로 구분되어 정수로 주어진다.
(1 <= a_i <= 100,000)

셋째 줄에 ARC팀의 참가자의 코딩실력을 나타내는 길이 M 수열 b가 공백으로 구분되어 정수로 주어진다.
(1 <= b_i <= 100,000)

출력
첫째 줄에 HI팀 참가자의 승리 횟수, ARC팀 참가자의 승리 횟수, 무승부 횟수를 공백으로 구분하여 출력한다.

--------

11:23~45

하나의 팀의 숫자 목록을 정렬
다른 팀 인원을 하나씩 어느 위치에 들어갈 수 있는지 확인
bisect 사용하자.
bisect_left 를 호출하여 첫번째 동점자 위치를,
bisect_right 를 호출하여 마지막 동점자 위치 + 1을 얻을 수 있음.


'''

import sys, bisect

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return N,M,A,B

def solve(Nhi:int, Narc:int, Ahi:list[int], Aarc:list[int])->list[int]:
    '''
    Args:
    Returns:
    '''
    ans = [0]*3  # HI winner, ARC winner, draw
    # 길이가 좀 더 긴 쪽을 이분탐색의 대상으로 하자.
    if Nhi > Narc:
        Ahi.sort()
        for a in Aarc:
            lf = bisect.bisect_left(Ahi, a)
            rg = bisect.bisect_right(Ahi, a)
            ans[1] += lf # arc winner
            ans[2] += (rg - lf)
            ans[0] += Nhi - rg
    else: # Nhi <= Narc
        Aarc.sort()
        for a in Ahi:
            lf = bisect.bisect_left(Aarc, a)
            rg = bisect.bisect_right(Aarc, a)
            ans[0] += lf # hi winner
            ans[2] += (rg - lf)
            ans[1] += Narc - rg

    return ans

if __name__ == '__main__':
    print(*solve(*get_input()))


'''
예제 입력 1
4 3
1000 90 3 20000
1 3 100000
예제 출력 1
7 4 1
예제 입력 2
5 5
1 2 3 4 5
1 2 3 4 5
예제 출력 2
10 10 5

----
pr=28449
run=(python3 a$pr.py)

echo '4 3\n1000 90 3 20000\n1 3 100000' | $run
# 7 4 1

echo '5 5\n1 2 3 4 5\n1 2 3 4 5' | $run
# 10 10 5

'''


