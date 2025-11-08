import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    return N,A

def solve_optimum(N:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''
    def calculate_case2()->int:
        '''
        벌1 -> 벌2 -> 벌통 배치인 경우의 최대 값
        벌1은 A[0]위치, 벌통은 A[N-1]위치에 고정. 벌2가 i위치에 있음.
        A[0]는 절대 못 먹음. A[i]도 못 먹음.
        i 를 1부터 N-2 까지 쭈욱 변경시켜가며 최대로 먹을 수 있는 값 계산.
        '''
        maxval = 0
        hsum = 2 * (sum(A) - A[0]) # honey sum
        for i in range(1, N-1):
            hsum -= A[i]*2  # 벌1, 벌2 모두 못 먹음
            maxval = max(maxval, hsum)
            hsum += A[i]  # 벌2가 우측 이동하면 적어도 벌1은 여기 꿀 먹을 수 있음.
        return maxval

    # 케이스1: 벌 -> 벌통 <- 벌
    a1 = sum(A)-A[0]-A[-1]+max(A)
    # 케이스2: 벌1 -> 벌2 -> 벌통
    a2 = calculate_case2()
    # 케이스3: 케이스2의 반대
    A.reverse()
    a3 = calculate_case2()

    return max(a1,a2,a3)

if __name__ == '__main__':
    print(solve_optimum(*get_input()))

