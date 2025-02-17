'''

1로 만들기
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.15 초 (하단 참고)	128 MB	345274	119982	76572	33.382%
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

rule 1: X가 3으로 나누어 떨어지면, 3으로 나눈다.
rule 2: X가 2로 나누어 떨어지면, 2로 나눈다.
rule 3: 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 10**6보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

'''


def solve(N):
    A = [ N ] * (N + 1)
    A[0] = 0 # not used
    A[1] = 0 # already reached to 1

    # # using A[1]
    # A[2] = 1 # x2 or +1
    # A[3] = 1 # x3

    # # using A[2]
    # A[4] = 2 # x2
    # A[6] = 2 # x3

    # # using A[3]
    # A[6] = 2 # x2, but redundant
    # A[9] = 2 # x3

    # construction approach
    for i in range(1, N+1):
        if i * 3 <= N:
            A[i*3] = min(A[i*3], A[i]+1)
        if i * 2 <= N:
            A[i*2] = min(A[i*2], A[i]+1)
        if i + 1 <= N:
            A[i+1] = min(A[i]+1, A[i+1])
        # print(f'{i}: {A}')
    return A

def solve2(N):
    # it failed to solve the problem!!

    A = [0] * (N + 1)
    A[1] = 0 # already reached to 1

    # fill x3 rule, from A[1] to A[N]
    for i,n in enumerate(range(3, N+1, 3), 1):
        A[n] = i
    print(A)
    # fill x2 rule, from A[1] to A[N]
    for i,n in enumerate(range(2, N+1, 2), 1):
        if A[n] == 0:
            A[n] = i
    print(A)
    # fill +1 rule
    for n in range(1, N+1):
        if A[n] == 0:
            A[n] = A[n-1] + 1
    return A

def solve3(N):
    A = [0] * (N + 1)
    A[1] = 0 # already reached to 1
    for n in range(2, N+1):
        A[n] = A[n-1] + 1
        # rule2 와 rule3 중 어느 것이 더 최소 값이 될 지는 모르므로, 둘 다 계산 필요.
        if n % 2 == 0:
            A[n] = min(A[n], A[n//2] + 1)
        if n % 3 == 0:
            A[n] = min(A[n], A[n//3] + 1)
    return A

N = int(input())

mode = __import__('os').getenv('SOLVE', '')
if mode:
    print(f'mode: {mode}')
    solve = globals().get(f'solve{mode}', solve)
    print(solve)

A = solve(N)
# print(A)
print(A[N])



'''
예제 입력 1
2
예제 출력 1
1

예제 입력 2
10
예제 출력 2
3
힌트
10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.
'''