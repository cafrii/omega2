import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = []
    for _ in range(N):
        L = int(input().rstrip())
        B = list(map(int, input().split()))
        assert len(B) == L
        A.append(B)
    return N,A

def solve(N:int, A:list[list[int]])->list[str]:
    '''
    Args:
    Returns:
    '''
    NINF = int(-1e8) # -(1_000*10_000 + 1)  # negative infinity

    def find_max_subseq(seq:list[int])->list[int]:
        '''
        Returns: [ start_idx, end_idx, max_sum ]
        '''
        n = len(seq)

        # format of dp and max_kv: [ start_idx, end_idx, max_sum ]
        # index is 0-based.

        dp = [ [k, k, v] for k,v in enumerate(seq) ]
        # 자기 자신 단독으로만 구성된 경우로 초기화
        max_kv = dp[0][:]

        for k in range(1, n): # k: 1 ~ n-1

            if dp[k-1][2] > 0:
                # 직전의 수열을 이어서 하는 것이 도움이 되는 경우임. 끝 인덱스는 현재 인덱스
                dp[k] = [dp[k-1][0], k, dp[k-1][2] + seq[k]]

            # 최대값 추척
            if dp[k][2] < max_kv[2]: continue

            if dp[k][2] > max_kv[2]:  # 새로운 최대값
                max_kv = dp[k][:] # (dp[k][0], k, dp[k][2])
                continue

            # dp[k][2] == max_kv[2]:  # 동점자인 경우.
            # 보석 개수가 최소가 되는 것을 선택
            if dp[k][1] - dp[k][0] > max_kv[1] - max_kv[0]:
                continue

            if dp[k][1] - dp[k][0] < max_kv[1] - max_kv[0]:
                max_kv = dp[k][:]

            # dp[k][1] - dp[k][0] == max_kv[1] - max_kv[0]:
            # 여전히 동점자. 사전식, 즉, 먼저 발견된 것 우선. 따라서 갱신 없이 skip
            pass

        return max_kv

    ans = ['']
    max_sum = 0
    for i in range(N):
        s,e,mx = find_max_subseq(A[i])
        max_sum += mx
        ans.append(f'{s+1} {e+1}')
    ans[0] = str(max_sum)
    return ans

if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))

