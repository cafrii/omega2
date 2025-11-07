import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = [ int(input().rstrip()) for _ in range(N) ]
    return N,A

def solve(N:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''
    # 누적합 구해놓기
    asum = [0] * (N+1)
    # asum[k] 는 첫 k개 요소의 합. 즉, A[0] 부터 A[k-1] 까지의 합

    for k in range(N): # k: 0 ~ N-1
        asum[k+1] = asum[k] + A[k]

    # A[j] 부터 A[k]의 합은 asum[k+1] - asum[j] 이다.
    total_sum = asum[N]

    def bruteforce():
        # 범위의 시작, 끝 인덱스.
        # 안쪽 합 [s, e) 와 바깥쪽 합 [e, s) 를 비교해야 함.
        # 바깥 합은 총합에서 안쪽 합을 빼면 됨.
        max_dist = -1
        max_dist_pair = (0,0)
        for s in range(N):
            for e in range(s+1, N+1):
                if s==0 and e==N: continue
                # 내합 [s, e)
                isum = asum[e] - asum[s]
                # 외합 [e, s). 분할되어 있을텐데 그냥 전체에서 빼기로 계산
                osum = total_sum - isum
                dist = min(isum, osum)
                if dist > max_dist:
                    max_dist_pair = (s,e,isum,osum)
                max_dist = max(max_dist, dist)

        return max_dist

    def twopointer():
        '''
        투포인터 방식 적용. 포인터 이동 시점 판단을 좀 고민해야 함.
        잘 생각해 보니, S를 증가해야 하는 시점, E를 증가해야 하는 시점이 명확하다.
        내합, 외합이 동일한 경우가 좀 문제가 된다.
        '''
        max_dist = -1
        s,e = 0,1
        while True:
            # 내합 [s, e)
            isum = asum[e] - asum[s]
            # 외합 [e, s). 양쪽으로 분할되어 있을텐데 그냥 전체에서 빼기로 계산
            osum = total_sum - isum
            dist = min(isum, osum)
            max_dist = max(max_dist, dist)
            if e >= N:
                break
            if isum < osum:
                e += 1
            elif isum > osum:
                s += 1
            # else: # isum == osum
            # 이 경우는 좀 복잡해진다.
            # 최대한 내합, 외합이 비슷하게 만들어야 하니 적은 쪽을 이동해야 한다.
            elif A[s] < A[e]:
                s += 1
            elif A[s] > A[e]:
                e += 1
            else: # 양쪽 둘 다 같으면 둘 다 이동.
                s,e = s+1,e+1

        return max_dist

    return twopointer()

if __name__ == '__main__':
    print(solve(*get_input()))
