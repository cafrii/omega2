import sys

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
        tb = ta[j]
        for k in range(1, N+1):
            tb[k] = tb[k-1] + tb[k]

    # 각 문제 풀이
    return [ ta[c][ri+1] - ta[c][li] for c,li,ri in Q ]


if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
