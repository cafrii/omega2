
def solve(N:int):
    # 자릿수 N 으로 이루어진 이친수 개수를 구해야 함.

    A = [ [0, 0] for _ in range(N) ]
    # A[k] 는 k+1 자릿수로 이루어진 이친수의 개수
    # A[k][0] 은 끝자리가 0 으로 끝나는 것,
    # A[k][1] 은 끝자리가 1 로 끝나는 것.

    # 한 자리수 의 이친수
    A[0] = [0, 1] # 문제 조건에 의해 1 하나만 가능.

    for k in range(1, N):
        A[k][0] = A[k-1][0] + A[k-1][1] # 0 으로 끝나는 수
        A[k][1] = A[k-1][0]  # 1로 끝나는 수
        # print(A)

    return A[N-1][0] + A[N-1][1]

N = int(input().strip())
print(solve(N))