import sys

def get_input():
    input = sys.stdin.readline
    N,K,Q,M = map(int, input().split())
    Ks = list(map(int, input().split()))
    Qs = list(map(int, input().split()))
    Ms = []
    for _ in range(M):
        s,e = map(int, input().split())
        Ms.append((s, e))
    return N,Ks,Qs,Ms

def solve(N:int, Ks:list[int], Qs:list[int], Ms:list[tuple[int,int]])->list[str]:
    '''
    Args:
    Returns:
    '''

    # 학생 번호는 3번부터 N+2.
    attn = [0] * (N+3)
    # attn[k]는 학생 번호 k의 출석 여부. 1이면 출석.

    # 졸고 있는 학생 상태 표
    sleep = [0] * (N+3)
    for k in Ks:
        sleep[k] = 1

    # 출석 코드 보내기
    for q in Qs:
        # 코드 받은 학생이 졸고 있으면 모조리 미출.
        if sleep[q]:
            continue
        for qq in range(q, N+3, q):
            if not sleep[qq]: attn[qq] = 1
            # 문제 모호한 부분. 졸고 있는 그 학생 만 미출이고 그 이후는 영향 받지 않음.

    # 누적합 계산
    psum = [0]*(N+3)
    # psum[j] 는 처음(학생 3) 부터 학생 j까지의 미출석
    for j in range(3, N+3):
        # j: 학생 번호
        psum[j] = psum[j-1] + (0 if attn[j] else 1)

    # 검사 구간
    ans = []
    for s,e in Ms:
        ans.append(str(psum[e] - psum[s-1]))

    return ans

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))
