import sys

def get_input():
    input = sys.stdin.readline
    T = int(input().rstrip())
    def gen():
        for _ in range(T):
            N,M,K = map(int, input().split())
            A = list(map(int, input().split()))
            #assert len(A)==N
            yield N,M,K,A
    return gen()

def solve(N:int, M:int, K:int, A:list[int])->str:
    '''
    Args:
    Returns:
    '''
    # 이 조건이 함정. 결국 모든 숫자를 다 선택한다 라는 것은 1가지의 선택 으로 봐야 함.
    if N == M:
        return '1' if sum(A)<K else '0'

    A2 = A + A[:M-1]
    cnt = 0

    #--- brute-force
    # for k in range(0, N): # k: 0 ~ N-1
    #     s = sum(A2[k:k+M])
    #     if s < K:
    #         cnt += 1

    #--- sliding window
    summ = 0
    for k in range(0, N): # k: 0 ~ N-1
        if k == 0:
            summ = sum(A2[0:M])
        else:
            summ = summ - A2[k-1] + A2[k-1+M]
        if summ < K:
            cnt += 1

    ans = str(cnt)
    return ans

if __name__ == '__main__':
    print('\n'.join(solve(n,m,k,a) for n,m,k,a in get_input()))
