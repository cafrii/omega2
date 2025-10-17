import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    A = list(map(int, input().split()))
    #assert len(A) == N
    Q = int(input().rstrip())
    B = [ list(map(int, input().split()))  for _ in range(Q) ]
    return A,B

def solve(A:list[int], B:list[list[int]])->list[int]:
    '''
    Args: A: 주어진 숫자 배열, B: 검사할 범위 [x,y]의 목록
    Returns: 주어진 각 x,y 범위에서의 감소 횟수의 목록
    '''
    N = len(A)
    delta = [0]*(N)
    # delta[k]는 첫번째 악보(A[0])부터 k번째 악보(A[k])까지의 범위 (즉 A[0:k+1]) 에서
    # 감소하는 요소의 (누적) 개수
    #
    for k in range(1,N):
        if A[k-1] > A[k]:
            delta[k] = delta[k-1] + 1
        else:
            delta[k] = delta[k-1]

    return [ delta[y-1] - delta[x-1] for x,y in B ]

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))
