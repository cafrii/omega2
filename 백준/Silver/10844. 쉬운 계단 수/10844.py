'''
쉬운 계단 수

10844

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	163402	53412	39104	31.107%
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''



def solve(len):
    # len: 1~100

    num = [ 0 ] * 10
    # num[i]는 해당 단계(step)에서 끝자리가 i 로 끝나는 계단수의 개수.

    # step 1: 1 자리 숫자. 0 은 해당 안됨.
    for k in range(1, 10):
        num[k] = 1

    # step 2 부터는 이터레이션.
    for step in range(2, len+1):
        # len 2)
        next = [0]*10
        next[0] = num[1]
        for k in range(1, 9):
            next[k] = num[k-1] + num[k+1]
        next[9] = num[8]
        num = next

    # return sum(num)
    # return int(str(sum(num))[-9:])
    return sum(num) % 1_000_000_000


N = int(input().strip())
print(solve(N))


'''
예제 입력 1
1
예제 출력 1
9

예제 입력 2
2
예제 출력 2
17
'''