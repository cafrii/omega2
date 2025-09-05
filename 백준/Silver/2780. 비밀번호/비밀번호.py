
import sys

MOD = 1234567
MAX_N = 1000

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    Ns = []
    for _ in range(C):
        Ns.append(int(input().rstrip()))
    return Ns,

def solve(Ns:list[int])->list[int]:
    '''
    '''
    max_n = max(Ns)
    ans = [0] * (max_n + 1)

    la = [1]*10  # la[k]: num cases where last digit is k
    nx = [0]*10  # next of la[]
    ans[1] = sum(la)

    for k in range(2, max_n+1):
        nx[1] = (la[2]+la[4]) % MOD
        nx[2] = (la[1]+la[3]+la[5]) % MOD
        nx[3] = (la[2]+la[6]) % MOD
        nx[4] = (la[1]+la[5]+la[7]) % MOD
        nx[5] = (la[2]+la[4]+la[6]+la[8]) % MOD
        nx[6] = (la[3]+la[5]+la[9]) % MOD
        nx[7] = (la[4]+la[8]+la[0]) % MOD
        nx[8] = (la[5]+la[7]+la[9]) % MOD
        nx[9] = (la[6]+la[8]) % MOD
        nx[0] = la[7]
        la,nx = nx,la
        ans[k] = sum(la) % MOD

    return [ ans[n] for n in Ns ]

if __name__ == '__main__':
    r = solve(*get_input())
    print('\n'.join(map(str, r)))
    