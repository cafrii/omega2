'''
연속합

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (추가 시간 없음)	128 MB	158561	61306	43810	37.537%

문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

'''


N_MIN = -1000

def solve(nums):
    # 두 개의 값을 계산하면서 윈도우를 증가.
    # v1: 윈도우 우측 끝에 붙은 부분수열의 최대 값.
    # v2: 부분수열의 최대 값.
    v1, v2 = N_MIN-1, N_MIN-1

    for n in nums:
        v1 = max(v1 + n, n)
        v2 = max(v2, v1)

    return max(v1, v2)


N = int(input().strip())
A = map(int, input().strip().split())

print(solve(A))


'''
10, -4, 3, 1, 5, 6, -35, 12, 21, -1

10: 10, 10
-4: 10, 6
3: 10, 9
1: 10, 10
5: 15, 15
6: 21, 21
-35: 21, -35
12: 21, 12
21: 33, 33
-1: 33, 32



예제 입력 1
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1
33

예제 입력 2
10
2 1 -4 3 4 -4 6 5 -5 1
예제 출력 2
14

예제 입력 3
5
-1 -2 -3 -4 -5
예제 출력 3
-1

'''