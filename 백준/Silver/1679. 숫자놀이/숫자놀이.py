import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    Ns = list(map(int, input().split()))
    #assert len(Ns) == N
    K = int(input().rstrip())
    return N,Ns,K

def solve2(N:int, Ns:list[int], K:int)->str:
    '''
    Args:
        Ns: 사용할 수 있는 숫자들의 목록
        K: 최대 사용 횟수
    '''
    max_n = max(Ns)
    max_k = max_n * K + 1

    # 각 단계에서 만들어진 결과
    dp = [0]*(max_k+1)
    dp[0] = 1

    for k in range(1, K+1): # k: 1 ~ K. 최대 K 개의 숫자를 사용할 수 있음.
        for j in range(max_k, -1, -1):
            if dp[j] == 0: continue
            for n in Ns:
                # n 이라는 숫자 1개를 더 덧셈에 추가하여 만들 수 있는 수를 모두 찾음.
                dp[j + n] = 1

    # 승 패 결정 여부 확인
    for k in range(max_k+1):
        if not dp[k]:
            winner = ['holsoon', 'jjaksoon'][k % 2]
            return f'{winner} win at {k}'
    return 'something wrong'

if __name__ == '__main__':
    print(solve2(*get_input()))

