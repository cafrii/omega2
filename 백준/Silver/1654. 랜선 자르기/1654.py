'''
1654번
랜선 자르기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	273889	67220	45362	22.110%

문제
집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다.
박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.

이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다.
(이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며,
기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자.
N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다.
K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다.
그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다.
랜선의 길이는 231-1보다 작거나 같은 자연수이다.

출력
첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.


---------

4:26~4:44  bruteforce
4:53~5:10  binary search

'''

import sys
input = sys.stdin.readline


def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve_bruteforce(A:list[int], N:int)->int:
    '''
    Args:
        A: array of length of cables
        N: number of cables needed
    Returns:
        max length of cable
    '''
    A.sort(reverse=True)

    log("%s, N %d", A, N)

    # chunk len 을 점점 줄여가면서, 만들수 있는 chunk 개수가 N이상이 될 때 가지 반복
    cl = A[0]

    while cl > 0:
        arr = [k//cl for k in A]
        num = sum( k//cl for k in A )
        if num >= N:
            return cl
        log("cl:%d, %s, %d", cl, arr, num)
        cl -= 1
    log("! failed")
    return cl # it should not happen



def solve_bs(A:list[int], N:int)->int:
    '''
    Args:
        A: array of length of cables
        N: number of cables needed
    Returns:
        max length of cable
    '''
    A.sort(reverse=True)

    log("%s, N %d", A, N)

    def allowed_len(clen:int)->bool:
        return sum( k//clen for k in A ) >= N

    cl_mx,cl_mn = A[0],1

    if allowed_len(cl_mx):
        return cl_mx
    # assert allowed_len(cl_mn)

    while cl_mx > cl_mn:
        # cl_mn 길이로는 항상 성공 (allowed)
        # cl_mx 길이로는 항상 실패 (not allowed)

        cl_mid = (cl_mx + cl_mn)//2

        if allowed_len(cl_mid):
            cl_mn = cl_mid
        else:
            cl_mx = cl_mid

        if cl_mx == cl_mn+1:
            return cl_mn

        # log("cl: %d, %d", cl_mn, cl_mx)

    return cl_mn


def solve_opt(A:list[int], N:int)->int:
    '''
    Args:
        A: array of length of cables
        N: number of cables needed
    Returns:
        max length of cable
    '''

    log("%s, N %d", A, N)

    def allowed_len(clen:int)->bool:
        # check if clen (chunk len) can be one of solution
        return sum( k//clen for k in A ) >= N

    mn,mx = 1,max(A)
    # gurantee that we always success with mn, always fail with mx.
    # chunk len 1 always succeed.

    if allowed_len(mx):
        return mx

    while mn < mx:
        mid = (mn + mx) // 2
        if mn == mid:
            break
        if allowed_len(mid):
            mn = mid
        else:
            mx = mid
    return mn


K,N = map(int, input().split())
A = []
for _ in range(K):
    A.append(int(input().strip()))

# print(solve_bruteforce(A, N))
# print(solve_bs(A, N))
print(solve_opt(A, N))



'''
예제 입력 1
4 11
802
743
457
539
예제 출력 1
200

run=(python3 1654.py)

echo '4 11\n802\n743\n457\n539' | $run

1 10
100
-> 10

1 1
10
-> 10

2 10
1000
1
-> 100

3 3
1
10
100
-> 33


'''
