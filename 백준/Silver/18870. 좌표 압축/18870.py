'''
좌표 압축 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	120317	51684	38669	40.124%
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109

'''


import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
assert N == len(A)

set1 = set(A)
# print(set1)

dict1 = {}
acc_sum = 0 # 누적 개수 합
for k in sorted(list(set1)):
    dict1[k] = acc_sum
    acc_sum += 1

# print(dict1)

# print
for i in range(N):
    A[i] = dict1[A[i]]
print(*A)


'''
예제 입력 1
5
2 4 -10 4 -9
예제 출력 1
2 3 0 3 1

echo '5\n2 4 -10 4 -9' | python3 18870.py

예제 입력 2
6
1000 999 1000 999 1000 999

예제 출력 2
1 0 1 0 1 0



(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
# N = 100
N = 1_000_000
# N = randint(1,1_000_000)
print(N)
print(' '.join([str(randint(-10**9,10**9)) for x in range(N)]))
EOF
) | time python3 18870.py > /dev/null

1.11s user 0.07s system 73% cpu 1.607 total

'''

