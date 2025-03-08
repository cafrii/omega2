
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
        num_k_pre2, num_k_pre = num_k_pre, num_k

    return num_k % MOD



# to speed up, use readline instead of input. see prob. 15552
import sys
readline = sys.stdin.readline

N = int(readline().rstrip())
print(solve(N))

