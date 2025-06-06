'''
이친수
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	108415	46835	35825	41.812%
문제
0과 1로만 이루어진 수를 이진수라 한다. 이러한 이진수 중 특별한 성질을 갖는 것들이 있는데,
이들을 이친수(pinary number)라 한다. 이친수는 다음의 성질을 만족한다.

이친수는 0으로 시작하지 않는다.
이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다.
하지만 0010101이나 101101은 각각 1, 2번 규칙에 위배되므로 이친수가 아니다.

N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다.

출력
첫째 줄에 N자리 이친수의 개수를 출력한다.
'''

def solve_greedy(N:int):
    # N 이 35 를 넘기면 너무 늦어짐.
    def count(start, n):
        # start 로 시작하는, 부분 자리수 n으로 이루어진 이친수 개수
        # 첫자리가 0으로 시작하지 않는다는 조건은 무시해도 됨.
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if start == 0:
            return count(0, n-1) + count(1, n-1)
        else:
            return count(0, n-1)

    # 첫자리 1 가정. 그 뒤에는 0 으로만 시작 가능.
    return count(0, N-1)





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
# print(solve_greedy(N))


'''
예제 입력 1
3
예제 출력 1
2
'''