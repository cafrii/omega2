'''

여러가지 시행 착오들

'''



def solve_wrong(N:int)->int:
    '''
    prefix 와 postfix 가 둘 다 있는 경우를 고려하지 않은 문제가 있음.
    예: extra 길이가 2 일 때, 다음 세가지 경우가 있을 수 있는데..
    - prefix 2
    - postfix 2
    - prefix 1, postfix 1
    아래 코드는 세번째 경우를 고려하지 않고 있으므로 틀린 답을 출력함.
    '''
    def gen_prefix(width:int)->int:
        digits = [0]*width
        for k in range(width):
            start = 1 if k==0 else 0
            for j in range(start,10):
                digits[k] = j
        # convert list to number
        value = 0
        for d in reversed(digits):
            value = value * 10 + d
        return value

    # A:list[int] = [666]
    A:set[int] = {666}

    for extra in range(1,N):

        # add as prefix
        # if extra is 2, prefix is 10~99, postfix is 0~99
        # if extra is 3, prefix is 100~999, postfix is 0~999

        mn = 10**(extra-1)
        mx = 10**(extra) - 1

        for prefix in range(mn,mx+1):
            A.add(prefix * 1000 + 666)

        # append as postfix
        for postfix in range(0,mx+1):
            A.add(666 * (10**extra) + postfix)

        if len(A) >= N:
            break

    # sort and pick N-th element
    A1 = sorted(list(A))
    print(A1)
    return A1[N-1]


N = int(input().strip())
print(solve_wrong(N))


'''


run=(python3 1436.py)

'''
