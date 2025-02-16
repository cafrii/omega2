'''

입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

예제 입력 1
5 21
5 6 7 8 9
예제 출력 1
21
예제 입력 2
10 500
93 181 245 214 315 36 185 138 216 295
예제 출력 2
497

'''

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)
result = 0

for i in range(N):
    if A[i] > M:
        break
    for j in range(i+1, N):
        if A[i] + A[j] > M:
            break
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] <= M:
                result = max(result, A[i] + A[j] + A[k])
            else:
                break

print(result)
