


'''
부분합 다국어
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (하단 참고)	128 MB	118167	33096	23370	26.353%
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다.
수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

아이디어
sum 을 계산할 때 코드 간략화를 위해 sum()을 사용하고자 함.
부분합 계산을 위해 sub-array 를 새로 만들지 않고, 이터레이터를 활용함.

아이디어2
시간 초과가 무조건 걸릴 만하게 문제가 나온다.
부분합을

'''

# input = __import__('sys').stdin.readline

# timeout!
def solve1(N, S, A):
    islice = __import__('itertools').islice
    min_sum = 0
    # increasing the length of the subarray
    for len in range(1, N):
        # print(f'len: {len}')
        for j in range(0, N-(len-1)):
            # calculate sublen, from [j:j+len]
            s = sum(islice(A, j, j + len))
            if s >= S: # consider only when s >= S
                # min_sum = min(s, min_sum) if min_sum != 0 else s
                # we only need to find the minimum length, not the sum itself!
                # so, do not try to get minimum of sum.
                print(len)
                exit()
            # print(f'  {A[j:j+len]} ->{s}, {min_sum}')
        if min_sum != 0:
            return len
    return 0

# timeout!
def solve2(N, S, A):
    LEN_MAX = 100000

    min_len = LEN_MAX
    for i in range(N): # start index
        s1 = 0
        for j in range(i, N): # end index
            s1 += A[j]
            if s1 >= S:
                len = j - i + 1
                break
        min_len = min(min_len, len)
    return min_len if min_len != LEN_MAX else 0


# timeout!
def solve3(N, S, A):
    # increasing the length of the subarray
    for len in range(1, N):
        # print(f'len: {len}')
        for j in range(0, N-(len-1)):
            # calculate sublen, from [j:j+len]
            # slice shifting 를 할 때, 새 요소 하나 더하고 구 요소 하나를 빼는 방식으로 계산.
            # len 이 1 인 경우는 sliding window 가 더 효율적이진 않다.
            if len == 1:
                subsum = A[j]
            elif j == 0: # first slice
                subsum = sum(islice(A, j, j + len))
            else:
                subsum = subsum + A[j + len - 1] - A[j - 1] # using previous subsum

            # print(f'  {A[j:j+len]} -> {subsum}')
            if subsum >= S:
                return len
    return 0



def solve4(N, S, A):
    # 부분합을 구할 때, 이전 부분합을 이용한다.

    # 0 부터 시작하는 sub-array 의 각 길이 별 부분합을 저장한다.
    # subsum_of_len[3] 은 A[0] 부터 3개의 합, 즉 A[0:4] 의 부분합이다.
    subsum_of_len = [0] * (N+1)
    for i in range(1, N+1): # 1 ~ N
        subsum_of_len[i] = subsum_of_len[i-1] + A[i-1]

    # increasing the length of the subarray
    for len in range(1, N):
        # print(f'len: {len}')
        sum = 0
        for j in range(0, N-(len-1)):
            # calculate sublen, from [j:j+len]
            # slice shifting 를 할 때, 새 요소 하나 더하고 구 요소 하나를 빼는 방식으로 계산.

            # len 이 1 인 경우는 sliding window 가 더 효율적이진 않다.
            if len == 1:
                sum = A[j]
            elif j == 0: # first slice. A[0:len]
                sum = subsum_of_len[len]
            else:
                sum = sum + A[j+len-1] - A[j-1]
                # get new sum using previous sum

            # print(f'  {A[j:j+len]} -> {sum}')
            if sum >= S:
                return len
    return 0



def solve5(N, S, A):
    # 부분합을 구할 때, 이전 부분합을 이용한다.

    # slicing 표기법을 활용한다.
    # [i:k] 는 i 부터 k-1 까지의 요소들을 의미한다.
    # A[i:k] 는 A[i] 부터 A[k-1] 까지의 범위를,
    # sum[i:k] 는 A[i] 부터 A[k-1] 까지의 부분합을 의미한다.
    #
    # 길이로 표현하면, A[i:k] 의 길이는 k - i 이다.
    # 길이가 len 인 sub-array 는 A[j:j+len] 으로 표현할 수 있다.

    # A[j:j+len] 의 부분합을 sum[j:j+len] 이라고 부른다.
    # 이는 A[j] 부터 A[j+len-1] 까지의 합이다.

    # 0 부터 시작하는 sub-array 의 각 길이 별 부분합을 저장한다.
    # partial_sum[k] 은 sum[0:k+1], 즉 A[0] 부터 A[k] 까지의 합이다.

    partial_sum = [0] * N
    partial_sum[0] = A[0]
    for i in range(1, N): # 1 ~ N-1
        partial_sum[i] = partial_sum[i-1] + A[i]

    # increasing the length of the subarray
    for len in range(1, N):
        print(f'len: {len}') if len % 100 == 0 else None
        sum = 0
        for j in range(0, N-(len-1)):
            # sum[j:j+len] = partial_sum[j+len-1] - partial_sum[j-1]
            sum = partial_sum[j+len-1] - partial_sum[j-1] if j > 0 else partial_sum[j+len-1]

            if sum >= S:
                return len
    return 0
    # 하지만 이 조차도 시간 초과!


def solve6(N, S, A):
    # two pointer algorithm
    # refer https://butter-shower.tistory.com/226

    li = ri = 0 # left and right index
    sum = A[0]  # partial sum from A[li] to A[ri] inclusive
    min_len = N+1

    while ri < N:
        if sum < S:
            if ri == N-1:
                break
            ri += 1
            sum += A[ri]
        else: # if sum >= S:
            min_len = min(min_len, ri - li + 1)
            sum -= A[li]
            li += 1

    return min_len if min_len != N+1 else 0


#------------

N,S = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

print(solve6(N, S, A))
# print(solve5(N, S, A))
# print(solve4(N, S, A))
# print(solve3(N, S, A))
# print(solve2(N, S, A))
# print(solve1(N, S, A))


'''
예제 입력 1
10 15
5 1 3 5 10 7 4 9 2 8

예제 출력 1
2

python3 1806.py < 1806.i1
2
python3 1806.py < 1806.i2
10
python3 1806.py < 1806.i3
1
python3 1806.py < 1806.i4
19783
python3 1806.py < 1806.i5
16645
python3 1806.py < 1806.i6
0
'''

import random, time

# question generation
def gen(N, S):
    randint = random.randint
    random.seed(time.time())

    # 10,000 이하의 자연수로 이루어진 길이 N짜리 수열
    if N < 10:
        N = randint(10, 100_000-1)
    if S < 1:
        S = randint(1, 100_000_000)

    print(f'{N} {S}')

    for _ in range(N):
        r = randint(1, 10_000)
        print(r, end=' ')
    print() # new line

    # print(f'# N: {N}, S: {S}')

# gen(0, 0)
# gen(100)
# gen(100000, 100000000)
