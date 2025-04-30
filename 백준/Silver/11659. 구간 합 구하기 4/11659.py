'''
구간 합 구하기 4 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	153608	63099	45797	38.424%
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N

'''

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))

# calculate partial sum
sums = [0] * (N+1)
# sums[k]: == sum(A[:k]), 앞의 k개 요소의 부분합. 즉, A[0] 부터 A[k-1] 까지의 합
for k in range(1, N+1):
    sums[k] = sums[k-1] + A[k-1]

for _ in range(M):
    i,j = map(int, input().split())
    # i번째 수 부터 j번째 수 까지의 합 == j번째 수 까지의 부분합 - (i-1)번째 수 까지의 부분합
    print(sums[j] - sums[i-1])




'''
예제 입력 1
5 3
5 4 3 2 1
1 3
2 4
5 5

예제 출력 1
12
9
1


5 2
1 2 2 3 3
1 1
5 5
-> 1, 3



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N,M = 100_000,100_000
print(N, M)
for _ in range(N):
    print(randint(1,1000), end=' ')
print('')
for k in range(M):
    i,j = randint(1,1000),randint(1,1000)
    if i > j: i,j = j,i
    print(i,j)
print('')
EOF
) | time python3 11659.py > /dev/ttys048

python3 11659.py > /dev/ttys048  0.16s user 0.06s system 69% cpu 0.323 total


'''