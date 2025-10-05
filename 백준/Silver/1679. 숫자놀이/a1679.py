'''


'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    Ns = list(map(int, input().split()))
    assert len(Ns) == N
    K = int(input().rstrip())
    return N,Ns,K

def solve(N:int, Ns:list[int], K:int)->str:
    '''
    Args:
        Ns: 사용할 수 있는 숫자들의 목록
        K: 최대 사용 횟수
    '''
    max_n = max(Ns)
    max_k = max_n * K + 1

    log("K %d, Ns %s, maxk %d", K, Ns, max_k)

    dp = set()  # 만들어지는 중간 단계의 숫자 집합
    dp.add(0) # 초기 값. 0을 만드는 것은 가능함.

    # 각 단계에서 만들어진 결과
    res = [0]*(max_k+1)
    res[0] = 1

    for k in range(1, K+1): # k: 1 ~ K. 최대 K 개의 숫자를 사용할 수 있음.
        dpx = set()

        for d in dp:
            # k-1 단계까지 만들 수 있는 숫자들에 대해
            for n in Ns:
                # n 이라는 숫자 1개를 더 덧셈에 추가하여 만들 수 있는 수를 모두 찾음.
                dpx.add(d + n)
                res[d + n] = 1

        dp = dpx
        log("K %d: dp %s", k, dp)

    # 승 패 결정 여부 확인
    log("res: %s", res)
    for k in range(max_k+1):
        if not res[k]:
            winner = ['holsoon', 'jjaksoon'][k % 2]
            return f'{winner} win at {k}'

    return 'something wrong'


def solve2(N:int, Ns:list[int], K:int)->str:
    '''
    Args:
        Ns: 사용할 수 있는 숫자들의 목록
        K: 최대 사용 횟수
    '''
    max_n = max(Ns)
    max_k = max_n * K + 1

    log("K %d, Ns %s, maxk %d", K, Ns, max_k)

    # 각 단계에서 만들어진 결과
    dp = [0]*(max_k+1)
    dp[0] = 1

    for k in range(1, K+1): # k: 1 ~ K. 최대 K 개의 숫자를 사용할 수 있음.

        for j in range(max_k, -1, -1):
            if dp[j] == 0: continue

            for n in Ns:
                # n 이라는 숫자 1개를 더 덧셈에 추가하여 만들 수 있는 수를 모두 찾음.
                dp[j + n] = 1

        log("K %d: dp %s", k, dp)

    # 승 패 결정 여부 확인
    log("final: %s", dp)
    for k in range(max_k+1):
        if not dp[k]:
            winner = ['holsoon', 'jjaksoon'][k % 2]
            return f'{winner} win at {k}'

    return 'something wrong'



if __name__ == '__main__':
    r = get_input()
    print(solve(*r))
    print(solve2(*r))

    # print(solve(*get_input()))
    # print(solve2(*get_input()))




'''
예제 입력 1
2
1 3
5
예제 출력 1
holsoon win at 14


----
run=(python3 a1679.py)

echo '2\n1 3\n5' | $run
# holsoon win at 14

echo '1\n1\n6' | $run
# jjaksoon win at 7

echo '2\n1 7\n7' | $run
# holsoon win at 20

echo '2\n1 7\n10' | $run 2> /dev/null
# jjaksoon win at 41


'''

