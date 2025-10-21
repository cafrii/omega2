'''
16139번
질문 게시판
인간-컴퓨터 상호작용, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	256 MB	32733	9412	7493	30.072%

문제
승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다.
이를 알아보기 위해 승재는 다음과 같은 생각을 했다.

'문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서
자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'

승재를 도와 특정 문자열 S, 특정 알파벳 alpha와 문자열의 구간 [l,r]이 주어지면
S의 l번째 문자부터 r번째 문자 사이에 alpha가 몇 번 나타나는지 구하는 프로그램을 작성하여라.
승재는 문자열의 문자는 0번째부터 세며, l번째와 r번째 문자를 포함해서 생각한다.
주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을 q번 할 것이다.

입력
첫 줄에 문자열 S가 주어진다. 문자열의 길이는 200,000자 이하이며 알파벳 소문자로만 구성되었다.
두 번째 줄에는 질문의 수 q가 주어지며, 문제의 수는 1 <= q <= 200,000을 만족한다.
세 번째 줄부터 (q+2)번째 줄에는 질문이 주어진다.
각 질문은 알파벳 소문자 alpha_i 와 0 <= l_i <= r_i<|S|를 만족하는 정수
l_i,r_i가 공백으로 구분되어 주어진다.

출력
각 질문마다 줄을 구분해 순서대로 답변한다.
i번째 줄에 S의 l_i번째 문자부터 r_i번째 문자 사이에 alpha_i가 나타나는 횟수를 출력한다.

서브태스크 1 (50점)
문자열의 길이는 2,000자 이하, 질문의 수는 2,000개 이하이다.

서브태스크 2 (50점)
추가 제한 조건이 없다.

----
10/21, 3:45~

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    S = input().rstrip()
    q = int(input().rstrip())
    Q = []
    for _ in range(q):
        a,l,r = input().split()
        Q.append((ord(a)-ord('a'), int(l), int(r)))
    return S,Q


def solve(S:str, Q:list[list[int]])->list[int]:
    '''

    '''
    N = len(S)
    # 누적합 테이블 초기화
    ta = [ [0]*(N+1) for a in range(26) ]

    # 먼저 차분합 테이블로 구성한 후 누적합 테이블로 변환한다.
    for k in range(1, N+1):
        idx = ord(S[k-1]) - ord('a')
        ta[idx][k] = 1

    # 차분 합 테이블을 누적 합 테이블로 변환
    for j in range(26): # 각 알파벳 별로 각각 진행
        log("(%d) %s", j, chr(ord('a') + j))
        tb = ta[j]
        for k in range(1, N+1):
            tb[k] = tb[k-1] + tb[k]
        log("   %s", tb)

    # 각 문제 풀이
    ans = [ ta[c][ri+1] - ta[c][li] for c,li,ri in Q ]
    return ans



def solve2(S:str, Q:list[list[int]])->list[int]:
    '''

    '''
    N = len(S)
    # 누적합 테이블 초기화
    ta = [ [] for _ in range(N+1) ]
    # ta[0]은 의도적으로 비워둠.
    ta[0] = [0]*26

    for k in range(1, N+1):
        ta[k] = ta[k-1][:] # copy
        c = ord(S[k-1]) - ord('a')
        ta[k][c] += 1

    # 각 문제 풀이
    ans = [ ta[ri+1][c] - ta[li][c] for c,li,ri in Q ]
    return ans


if __name__ == '__main__':
    print('\n'.join(map(str, solve2(*get_input()))))


'''
예제 입력 1
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
예제 출력 1
0
1
2
1

----
pr=3020
run=(python3 a$pr.py)

echo 'seungjaehwang\n4\na 0 5\na 0 6\na 6 10\na 7 10' | $run
#  0  1  2  1

echo 'hello\n5\nh 0 4\no 0 4\nk 0 4\ne 0 4\nl 3 3' | $run
#  1  1  0  1  1
'''