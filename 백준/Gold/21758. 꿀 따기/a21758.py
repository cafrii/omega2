'''
21758번
꿀 따기 서브태스크, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	15603	5824	4423	38.371%

문제
아래와 같이 좌우로 N개의 장소가 있다.

장소들 중 서로 다른 두 곳을 골라서 벌을 한 마리씩 둔다.
또, 다른 한 장소를 골라서 벌통을 둔다.
아래 그림에서 연한 회색의 장소는 벌이 있는 장소이고 진한 회색의 장소는 벌통이 있는 장소이다.

두 마리 벌은 벌통으로 똑바로 날아가면서 지나가는 모든 칸에서 꿀을 딴다.
각 장소에 적힌 숫자는 벌이 지나가면서 꿀을 딸 수 있는 양이다.

두 마리가 모두 지나간 장소에서는 두 마리 모두 표시된 양 만큼의 꿀을 딴다. (벌통이 있는 장소에서도 같다.)
벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
위의 그림과 같이 배치된 경우 두 마리의 벌 모두
4 + 1 + 4 + 9 + 9 = 27의 꿀을 따서, 전체 꿀의 양은 54가 된다.

위의 그림과 같이 배치된 경우 왼쪽 장소에서 출발한 벌은
9 + 4 + 4 + 9 + 9 = 35 의 꿀을 따고 오른쪽 장소에서 출발한 벌은
$4 + 9 + 9 = 22$의 꿀을 따므로, 전체 꿀의 양은 57이 된다.

위의 그림과 같은 경우는 전체 꿀의 양이 31이 된다.

장소들의 꿀 양을 입력으로 받아 벌들이 딸 수 있는 가능한 최대의 꿀의 양을 계산하는 프로그램을 작성하라.

입력
첫 번째 줄에 장소의 수 N이 주어진다.

다음 줄에 왼쪽부터 각 장소에서 꿀을 딸 수 있는 양이 공백 하나씩을 사이에 두고 주어진다.

출력
첫 번째 줄에 가능한 최대의 꿀의 양을 출력한다.

제한
3 <= N <= 100~000 각 장소의 꿀의 양은 $1$ 이상 $10~000$ 이하의 정수이다.


------

10:05~

'''



import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    assert len(A) == N
    return N,A


def solve_wrong(N:int, A:list[int])->int:
    '''
    Args:
    Returns:
    '''
    # prefix sum 계산.
    asum = [0]*(N+1)
    # asum[k]는 A[0]부터 A[k-1]까지의 합
    for k in range(1, N+1): # k: 1 ~ N
        asum[k] = asum[k-1] + A[k-1]

    def psum(j:int, k:int):
        # A[j] 부터 A[k] 까지의 부분 합. j, k는 A의 인덱스. (0 ~ N-1)
        return asum[k+1] - asum[j]

    maxval = -1
    # 벌통은 무조건 양 끝이고, 벌 하나는 반대쪽 끝에 위치한다.
    # case 1: 우측 끝 A[N-1] 이 벌통, 좌측 끝 A[0]이 벌
    val0 = psum(1, N-1)
    # 또 하나의 벌은 A[1]부터 시작하여 가능한 모든 위치에 대해 계산.
    for j in range(1, N-1): # j: 1 ~ N-2
        val = val0 - A[j] + psum(j+1, N-1)
        # A[j]를 뺀 이유는 두번째 벌 위치의 꿀은 딸 수 없기 때문
        maxval = max(maxval, val)

    # case 2: 좌측 끝 A[0]가 벌통, 우측 끝 A[N-1]이 벌
    val0 = psum(0, N-2)
    for j in range(N-2, 0, -1): # j: N-2 ~ 1
        val = val0 - A[j] + psum(0, j-1)
        # A[j]를 뺀 이유는 두번째 벌 위치의 꿀은 딸 수 없기 때문
        maxval = max(maxval, val)

    return maxval


def solve_slow(N:int, A:list[int])->int:
    '''
    Args:
    Returns:

    모든 위치를 다 검사.
    답은 맞는 거 같은데.. 시간 초과. 좀 더 가지치기 필요함!
    '''
    # prefix sum 계산.
    asum = [0]*(N+1)
    # asum[k]는 A[0]부터 A[k-1]까지의 합
    for k in range(1, N+1): # k: 1 ~ N
        asum[k] = asum[k-1] + A[k-1]

    def psum(j:int, k:int):
        # A[j] 부터 A[k] 까지의 부분 합. j, k는 A의 인덱스. (0 ~ N-1)
        return asum[k+1] - asum[j]

    maxval = -1

    for b in range(N): # 벌통 위치. b: 0 ~ N-1
        if b > 0:
            # case 1: 좌측 끝 A[0]이 첫번째 벌
            val0 = psum(1, b)
            # 또 하나의 벌은 나머지 모든 가능한 위치에 대해 계산.
            for j in range(1, N): # j: 1 ~ N-1
                if j == b: continue # 벌이 벌통 위에 있을 수 없음.
                if j < b:
                    val = (val0 - A[j]) + psum(j+1, b)
                    # A[j]를 뺀 이유는 두번째 벌 위치의 꿀은 첫번째 벌이 딸 수 없기 때문
                else: # b < j
                    val = val0 + psum(b, j-1)

                if val > maxval: log("b %d, 1, j %d -> %d", b, j, val)
                maxval = max(maxval, val)

        if b < N-1:
            # case 2: 우측 끝 A[N-1]이 첫번째 벌
            val0 = psum(b, N-2)
            for j in range(0, N-1):
                if j == b: continue
                if j < b:
                    val = val0 + psum(j+1, b)
                else:
                    val = val0 - A[j] + psum(b, j-1)

                if val > maxval: log("b %d, 2, j %d -> %d", b, j, val)
                maxval = max(maxval, val)

    return maxval



def solve_slow2(N:int, A:list[int])->int:
    '''
    Args:
    Returns:

    벌통은 모든 위치를 다 시도하고,
    벌의 위치를 선택적으로 함. 첫번째 벌은 무조건 맨 끝. 두번째 벌은 가능한 여러 곳 시도.
    -> 여전히 시간 초과. N 5000 일 때 수 초 소요됨.

    '''
    # prefix sum 계산.
    asum = [0]*(N+1)
    # asum[k]는 A[0]부터 A[k-1]까지의 합
    for k in range(1, N+1): # k: 1 ~ N
        asum[k] = asum[k-1] + A[k-1]

    def psum(j:int, k:int):
        # A[j] 부터 A[k] 까지의 부분 합. j, k는 A의 인덱스. (0 ~ N-1)
        return asum[k+1] - asum[j]

    maxval = -1

    for b in range(N): # 벌통 위치. b: 0 ~ N-1
        # case 1: 좌측 끝 A[0]이 첫번째 벌
        if b > 0:
            val0 = psum(1, b)
            # 또 하나의 벌.
            # case 1-1: 벌통 좌측의 모든 가능한 위치에 대해
            for j in range(1, b): # j: 1 ~ b-1
                val = (val0 - A[j]) + psum(j+1, b)
                # A[j]를 뺀 이유는 두번째 벌 위치의 꿀은 첫번째 벌이 딸 수 없기 때문
                # if val > maxval: log("b %d, 1, j %d -> %d", b, j, val)
                maxval = max(maxval, val)
            # case 1-2: 두번째 벌이 우측 맨 끝 A[N-1]
            if b < N-1:
                val = val0 + psum(b, N-2)  # 벌통 우측의 대부분
                maxval = max(maxval, val)

        # case 2: 우측 끝 A[N-1]이 첫번째 벌
        if b < N-1:
            val0 = psum(b, N-2)
            # case 2-1: 두번째 벌이 좌측 끝 A[0]
            if 0 < b:
                val = val0 + psum(1, b) # 벌통 좌측의 대부분
                maxval = max(maxval, val)
            # case 2-2: 두번째 벌이 벌통(b)의 우측에.
            for j in range(b+1, N-1): # j: b+1 ~ N-2
                val = val0 - A[j] + psum(b, j-1)

                # if val > maxval: log("b %d, 2, j %d -> %d", b, j, val)
                maxval = max(maxval, val)

    return maxval


def solve_improve(N:int, A:list[int])->int:
    '''
    Args:
    Returns:

    벌통의 위치를 양 끝과 최대값 위치로 한정함.
    -> N 100_000 인 경우 여전히 11초나 소요됨!
    어디를 더 개선해야 하지?
    '''
    # prefix sum 계산.
    asum = [0]*(N+1)
    # asum[k]는 A[0]부터 A[k-1]까지의 합
    for k in range(1, N+1): # k: 1 ~ N
        asum[k] = asum[k-1] + A[k-1]

    def psum(j:int, k:int):
        # A[j] 부터 A[k] 까지의 부분 합. j, k는 A의 인덱스. (0 ~ N-1)
        return asum[k+1] - asum[j]

    maxval = -1

    bmax = max(A)
    # bloc = [ k for k in range(N) if A[k] == bmax ]
    # bloc = list(set(bloc + [0, N-1]))
    bloc = list(set([0, A.index(bmax), N-1]))

    for b in sorted(bloc): # 벌통 위치
        # case 1: 좌측 끝 A[0]이 첫번째 벌
        if b > 0:
            val0 = psum(1, b)
            # 또 하나의 벌.
            # case 1-1: 벌통 좌측의 모든 가능한 위치에 대해
            for j in range(1, b): # j: 1 ~ b-1
                val = (val0 - A[j]) + psum(j+1, b)
                # A[j]를 뺀 이유는 두번째 벌 위치의 꿀은 첫번째 벌이 딸 수 없기 때문
                # if val > maxval: log("b %d, 1, j %d -> %d", b, j, val)
                maxval = max(maxval, val)
            # case 1-2: 두번째 벌이 우측 맨 끝 A[N-1]
            if b < N-1:
                val = val0 + psum(b, N-2)  # 벌통 우측의 대부분
                maxval = max(maxval, val)

        # case 2: 우측 끝 A[N-1]이 첫번째 벌
        if b < N-1:
            val0 = psum(b, N-2)
            # case 2-1: 두번째 벌이 좌측 끝 A[0]
            if 0 < b:
                val = val0 + psum(1, b) # 벌통 좌측의 대부분
                maxval = max(maxval, val)
            # case 2-2: 두번째 벌이 벌통(b)의 우측에.
            for j in range(b+1, N-1): # j: b+1 ~ N-2
                val = val0 - A[j] + psum(b, j-1)

                # if val > maxval: log("b %d, 2, j %d -> %d", b, j, val)
                maxval = max(maxval, val)

    return maxval


def solve_optimum(N:int, A:list[int])->int:
    '''

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
    # print(solve_slow(*get_input()))

    # inp = get_input()
    # a1 = solve_slow2(*inp)
    # a2 = solve(*inp)
    # assert a1 == a2
    # print(a1)




'''
예제 입력 1
7
9 9 4 1 4 9 9
예제 출력 1
57
예제 입력 2
7
4 4 9 1 9 4 4
예제 출력 2
54
예제 입력 3
3
2 5 4
예제 출력 3
10

----
pr=21785
run=(python3 a$pr.py)

echo '7\n9 9 4 1 4 9 9' | $run
# 57
echo '7\n4 4 9 1 9 4 4' | $run
# 54
echo '3\n2 5 4' | $run
# 10

'''



#-------------------------
import time,os
from random import seed,randint,shuffle

def gen_worstcase_input():
    seed(time.time())
    seed(43)
    N = int(os.getenv('_N', '10'))
    A = [ randint(1,99) for _ in range(N) ]
    return N,A

def test():
    N,A = gen_worstcase_input()
    print(N)
    print(' '.join(map(str, A)))

def testloop():
    for i in range(10000):
        N,A = gen_worstcase_input()
        print(f'({i}) A: {A}')
        ans = solve(N, A)
        print(f'ans: {ans}')

'''
# worst case simulation

python3 -c "from a$pr import test; test()" | time $run

_N=100000 python3 -c "from a$pr import test; test()" | time $run

# for seed(43)
_N=500 python3 -c "from a$pr import test; test()" | time $run
# 48500
# $run  0.09s user 0.01s system 97% cpu 0.094 total

5000 부터는 timeout!

# 개선후

_N=500 python3 -c "from a$pr import test; test()" | time $run
# 48500
# $run  0.04s user 0.01s system 96% cpu 0.053 total

_N=5000 python3 -c "from a$pr import test; test()" | time $run
# 503346
# $run  2.80s user 0.01s system 99% cpu 2.817 total

여전히 timeout!!

더 개선. bmax 값을 하나만 취해서 bloc 구성.

_N=1000 python3 -c "from a$pr import testloop; testloop()"


'''


