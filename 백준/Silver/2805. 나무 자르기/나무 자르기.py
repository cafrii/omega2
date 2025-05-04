
import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

N,M = map(int, input().split())
A = list(map(int, input().split()))

def solve():
    '''
    Global:
        A: list of wood heights
    Returns:
        max height to be cut
    '''
    # sort with descending order
    A.sort(reverse = True)
    # log('%s', A)

    amount = 0 # 지금까지 획득한 총 나무 길이
    for i in range(len(A)):
        # 이 단계에서 최대 얼마 길이까지 내려올 수 있는가?
        if i < len(A)-1:
            step = A[i] - A[i+1]
        else:
            step = A[i]
        if amount + (i+1)*step >= M:
            #log('[%d] amount %d + (step %d * %d) > %d', i, amount, step, i+1, M)
            # base = A[i+1] if i < len(A) else 0
            # q = ceiling((M - amount)/(i+1))
            q = (M - amount + i)//(i+1)
            #log('[%d] step %d, amount %d, q %d -> %d', i, step, amount, q, A[i]-q)
            return A[i] - q
        amount += (i+1)*step
        #log('[%d] %d*%d -> amount %d', i, i+1, step, amount)
    return -1

print(solve())