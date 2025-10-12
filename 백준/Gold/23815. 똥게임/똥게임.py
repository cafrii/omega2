
def get_input():
    import sys
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        a,b = input().split()
        A.append((a,b))
    return N,A

def solve(N:int, A:list[tuple[str,str]])->str:
    '''
    Returns:
        answer string
    '''

    def calc(num:int, ops:str)->int:
        '''
        Args: ops 는 문자 두개로 구성된 연산 명령
        Returns: 연산 적용 후 결과
        '''
        if num <= 0: return 0
        op = ops[0]
        arg = int(ops[1])
        ret = (
            num+arg if op=='+' else
            num-arg if op=='-' else
            num*arg if op=='*' else
            num//arg if op=='/' else 0
        )
        return ret if ret > 0 else 0

    dp = [1,0]  # 초기 인원 수
    # 0 이면 game over 상태임.

    for k in range(1, N+1):
        a,b = A[k-1]  # 두 개의 선택지
        prev0,prev1 = dp

        dp[0] = max(calc(prev0, a), calc(prev0, b))  # skip 안 한 경우
        dp[1] = max(
            prev0,        # 이번 단계에서 skip 하는 경우
            calc(prev1, a), calc(prev1, b),
        )
        if dp == [0,0]: break

    ans = max(dp)
    return str(ans) if ans > 0 else 'ddong game'

if __name__ == '__main__':
    print(solve(*get_input()))
