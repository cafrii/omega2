'''
2780번
비밀번호 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	3318	1414	1146	43.311%

문제
석원이는 자신의 현관문에 비밀번호 기계를 설치했다. 그 기계의 모양은 다음과 같다.

지나가던 석원이 친구 주희는 단순한 호기심에 저 비밀번호를 풀고 싶어한다.
이때 주희는 바닥에 떨어져 있는 힌트 종이를 줍게 된다.
이 종이에는 석원이가 비밀번호를 만들 때 사용했던 조건이 적혀 있다.
이제 주희는 이 조건을 가지고, 석원이 집의 가능한 비밀번호의 전체 개수를 알고 싶어 한다.
현재 컴퓨터를 사용할 수 없는 주희는 당신에게 이 문제를 부탁했다.
석원이의 힌트 종이는 다음과 같다.

- 비밀번호의 길이는 N이다.
- 비밀번호는 위 그림에 나온 번호들을 눌러서 만든다.
- 비밀번호에서 인접한 수는 실제 위 기계의 번호에서도 인접해야 한다.

(ex. 15 라는 비밀번호는 불가능하다. (1과 5는 인접하지 않는다. ) 하지만 1236이라는 비밀번호는 가능하다.)

입력
첫 번째 줄에 Test case의 수 T가 주어진다.
그리고 각각의 케이스마다 입력으로 첫 번째 줄에 비밀번호의 길이 N이 주어진다.( 1 <= N <= 1,000 )

출력
각각의 Test case에 대해서 조건을 만족하는 비밀번호의 개수를 출력하라.
단, 수가 매우 커질 수 있으므로 비밀번호의 개수를 1,234,567으로 나눈 나머지를 출력하라.

----

8:48~

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

MOD = 1234567
MAX_N = 1000

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    Ns = []
    for _ in range(C):
        Ns.append(int(input().rstrip()))
    return Ns,

def solve(Ns:list[int])->list[int]:
    '''
    '''
    max_n = max(Ns)
    ans = [0] * (max_n + 1)

    la = [1]*10  # la[k]: num cases where last digit is k
    nx = [0]*10  # next of la[]
    ans[1] = sum(la)

    for k in range(2, max_n+1):
        # nx = [0]*10  # next of la[]
        nx[1] = (la[2]+la[4]) % MOD
        nx[2] = (la[1]+la[3]+la[5]) % MOD
        nx[3] = (la[2]+la[6]) % MOD
        nx[4] = (la[1]+la[5]+la[7]) % MOD
        nx[5] = (la[2]+la[4]+la[6]+la[8]) % MOD
        nx[6] = (la[3]+la[5]+la[9]) % MOD
        nx[7] = (la[4]+la[8]+la[0]) % MOD
        nx[8] = (la[5]+la[7]+la[9]) % MOD
        nx[9] = (la[6]+la[8]) % MOD
        nx[0] = la[7]
        la,nx = nx,la
        ans[k] = sum(la) % MOD

    return [ ans[n] for n in Ns ]

if __name__ == '__main__':
    r = solve(*get_input())
    print('\n'.join(map(str, r)))


'''
예제 입력 1
3
1
2
3
예제 출력 1
10
26
74

----
run=(python3 2780.py)

echo '3\n1\n2\n3' | $run
# 10 26 74



'''
