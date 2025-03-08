'''
1904

01타일

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.75 초 (추가 시간 없음)	256 MB	115315	38005	30114	31.911%

문제

지원이에게 2진 수열을 가르쳐 주기 위해, 지원이 아버지는 그에게 타일들을 선물해주셨다. 그리고 이 각각의 타일들은 0 또는 1이 쓰여 있는 낱장의 타일들이다.

어느 날 짓궂은 동주가 지원이의 공부를 방해하기 위해 0이 쓰여진 낱장의 타일들을 붙여서 한 쌍으로 이루어진 00 타일들을 만들었다.
결국 현재 1 하나만으로 이루어진 타일 또는 0타일을 두 개 붙인 한 쌍의 00타일들만이 남게 되었다.

그러므로 지원이는 타일로 더 이상 크기가 N인 모든 2진 수열을 만들 수 없게 되었다.
예를 들어, N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다. (01, 10은 만들 수 없게 되었다.)
또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.

우리의 목표는 N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것이다. 단 타일들은 무한히 많은 것으로 가정하자.

입력
첫 번째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

출력
첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
'''


MOD = 15746


def solve_memory_overflow(len:int):
    # len: length of tile

    num = [ 0 ] * (len+1)
    # num[k] 는 길이가 k 인 2진 수열 가짓수

    num[0] = 0
    num[1] = 1 # '1'
    num[2] = 2 # '11', '00'

    for k in range(3, len+1):
        # 두 가지 경우가 있음.
        #   '<길이 k-1 수열>' + '1'
        #   '<길이 k-2 수열>' + '00'
        #
        num[k] = num[k-1] + num[k-2]
        # print(f'{k}: {num[k]}')

    return num[len] % 15746



def solve_timeout(len:int):
    # avoid using num[] list to save memory.
    # remember last two nums.

    # len: length of tile

    num_k_pre2 = 1  # num[1]
    num_k_pre = 2   # num[2]

    for k in range(3, len+1):
        # 두 가지 경우가 있음.
        #   '<길이 k-1 수열>' + '1'
        #   '<길이 k-2 수열>' + '00'
        #
        num_k = num_k_pre + num_k_pre2

        # print(f'{k}: {num[k]}')

        num_k_pre2, num_k_pre = num_k_pre, num_k

    return num_k % MOD


def solve(len:int):
    # len: length of tile

    if len == 1:
        return 1
    if len == 2:
        return 2

    num_k_pre2 = 1  # num[1]
    num_k_pre = 2   # num[2]

    for k in range(3, len+1):
        num_k = (num_k_pre + num_k_pre2) % MOD

        # print(f'{k}: {num[k]}')

        num_k_pre2, num_k_pre = num_k_pre, num_k

    return num_k % MOD



# to speed up, use readline instead of input. see prob. 15552
import sys
readline = sys.stdin.readline

N = int(readline().rstrip())
print(solve(N))



'''
1
11 / 00
111, 100 / 001
1111, 1001, 0011 / 1100, 0000
..

예제 입력 1
4
예제 출력 1
5

40
10951

10000000
3073

'''