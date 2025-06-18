
import sys
input = sys.stdin.readline

def solve(A:list, M:int):
    '''
    '''
    def count_bl(L:int):
        # 주어진 L(블루레이 크기)로 녹화 시 블루레이 개수
        num_bl, psum = 1, 0 # number of blueray, partial sum
        for n in A:
            if psum + n <= L:
                psum += n
            else:
                num_bl,psum = num_bl+1,n
        return num_bl

    # lmin 은 최대 숫자 하나만 담을 수 있는 크기.
    # lmax 는 하나의 bl 에 모든 숫자를 다 담을 수 있는 크기.
    lmin,lmax = max(A),sum(A)

    while lmin < lmax:
        # 중간에서부터 시도.
        lmid = (lmin + lmax)//2
        if count_bl(lmid) <= M:
            # 일단은 만족. 더 좋은 해가 있는지 찾기 위해 범위 축소.
            lmin,lmax = lmin,lmid
        else:
            # M개에 포함하기 실패. L을 더 키워야 함.
            lmin,lmax = lmid+1,lmax
            if lmid == lmax:
                return lmid  # 굳이 시도해 보지 않아도, 됨.
    # 아마도 lmin == lmax 상태일 것임.
    return lmin


N,M = map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == N
print(solve(A, M))
