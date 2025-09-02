'''
10453번
제출
문자열 변환 다국어

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	1460	819	649	61.987%

문제
좋은 문자열은 다음과 같이 정의된다.

ab 는 좋은 문자열이다.
만약 문자열 [S]가 좋은 문자열이라면, 오른쪽과 왼쪽 끝에 각각 a와 b를 추가한 문자열 a[S]b 또한 좋은 문자열이다.
만약 문자열 [S]와 [T]가 좋은 문자열이라면 이들을 붙여 쓴 [S][T] 또한 좋은 문자열이다.

어떤 두 좋은 문자열 A와 B가 주어진다. 문자열 A를 '인접한 두 문자를 서로 바꾸는' 연산을 통해 문자열 B로 바꾸려고 한다.
이때 필요한 연산의 수를 구하는 프로그램을 작성하시오.
A를 B로 바꾸는 중에 나타나는 문자열도 모두 좋은 문자열이어야 한다.

예를 들어, A = aabbabab 이고 B = aaaabbbb라 해 보자.
그렇다면 다음과 같이 5번의 연산을 통해 A를 B로 변환할 수 있다.

aabbabab → aabbaabb → aabababb → aabaabbb → aaababbb → aaaabbbb

입력
첫 줄에 테스트 케이스의 수 T가 주어진다.

각각의 테스트 케이스마다, 한 줄에 문자열 A, B가 공백으로 분리되어 주어진다.
이때 A와 B는 좋은 문자열이며, 각각의 길이는 2 이상 100,000 이하이다.

출력
T줄에 걸쳐서, 각 테스트 케이스에서 주어진 문자열 A를 문자열 B로 변환할 때 필요한 연산의 수를 출력하시오.
만약 변환이 불가능한 경우 -1을 출력한다.


'''


import sys
# from typing import Iterator

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    T = int(input().rstrip())
    def get_it():
        for _ in range(T):
            a,b = input().split()
            yield a,b
    return get_it(),

def solve(s1:str, s2:str)->int:
    '''
    Returns:
        number of flips required to convert from string s1 to s2.
    '''
    N = len(s1)
    assert s1[0]=='a'==s2[0], "bad string head"
    assert s1[-1]=='b'==s2[-1], "bad string tail"

    # convert ab string to nested depth list

    d1,d2 = [1],[1]
    for i in range(1,N):
        # nested level calculation
        if s1[i]=='a': d1.append(d1[-1]+1)
        elif s1[i]=='b': d1.append(d1[-1]-1)
        else: assert False, "wrong string s1"

        if s2[i]=='a': d2.append(d2[-1]+1)
        elif s2[i]=='b': d2.append(d2[-1]-1)
        else: assert False, "wrong string s2"

    # 요소의 모든 값이 >=0 이면 good string.
    assert sum((1 for k in d1 if k<0), 0)==0, "d1 is bad"
    assert sum((1 for k in d2 if k<0), 0)==0, "d2 is bad"

    assert d1[-1]==d2[-1]==0, "badly nested"

    # ?ab -> ?ba: de-nesting
    #   ex: 343 -> 323,  net absdiff: -2
    # ?ba -> ?ab: en-nesting
    #   ex: 212 -> 232,  net absdiff: +2

    diff = 0
    for k1,k2 in zip(d1,d2):
        diff += abs(k1-k2)
    assert diff%2 == 0, "diff should be even"
    return diff // 2

if __name__ == '__main__':
    it, = get_input()
    for a,b in it:
        assert len(a)==len(b)
        print(solve(a,b))


'''
예제 입력 1
2
aabbabab aaaabbbb
aabbab abaabb

예제 출력 1
5
2

----
run=(python3 10453.py)

echo '2\naabbabab aaaabbbb\naabbab abaabb' | $run
# 5 2

echo '1\naaaaaaaaaabbbbbbbbbb ababaaababaaabbbbbab' | $run
# 31

'''

