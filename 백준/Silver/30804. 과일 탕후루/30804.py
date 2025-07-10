'''
30804번
과일 탕후루 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	1024 MB	16893	5977	4821	34.350%

문제

은하는 긴 막대에 N개의 과일이 꽂혀있는 과일 탕후루를 만들었습니다.
과일의 각 종류에는 1부터 9까지의 번호가 붙어있고, 앞쪽부터 차례로 S_1, S_2, ..., S_N 번 과일이 꽂혀있습니다.
과일 탕후루를 다 만든 은하가 주문을 다시 확인해보니 과일을 두 종류 이하로 사용해달라는 요청이 있었습니다.

탕후루를 다시 만들 시간이 없었던 은하는, 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 했습니다.
앞에서 a개, 뒤에서 b개의 과일을 빼면
S_{a+1}, S_{a+2}, ..., S_{N-b-1}, S_{N-b} 번 과일, 총 N-(a+b) 개가 꽂혀있는 탕후루가 됩니다.
( 0 <= a,b;  a+b < N )

이렇게 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 구하세요.

입력
첫 줄에 과일의 개수 N 이 주어집니다. (1 <= N <= 200,000)

둘째 줄에 탕후루에 꽂힌 과일을 의미하는 N 개의 정수 S_1, ..., S_N 이 공백으로 구분되어 주어집니다. (1 <= S_i <= 9)

출력
문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.

----

2:50~

'''


import sys
input = sys.stdin.readline

# from collections import deque, defaultdict


def log(fmt, *args): print(fmt % args, file=sys.stderr)


def solve_wrong(A:list[int])->int:
    '''
    '''
    N = len(A)

    kk,jk = [0]*(N+1), [0]*(N+1)
    ks,js = set(),set()

    answer = 0 # distance between j and k

    j = 0
    for k in range(1, N+1):
        ks.add(A[k-1])
        kk[k] = len(ks)
        # kk[k] 는 S_1 부터 S_k 까지의 과일이 모두 포함된 상태에서의 종류 개수
        # kk[0] 은 0 으로 고정.

        log("\n[%d]: A %s", k, A[:k])
        log("  kk %s, ks %s", kk[:k+1], ks)

        while kk[k] - jk[j] > 2:
            j += 1
            js.add(A[j-1])
            jk[j] = len(js)

        answer = max(answer, k-j)
        log("  jk %s, js %s, dist %d, max %d", jk[:j+1], js, k-j, answer)

    return answer



def solve(A)->int:
    N = len(A)

    hist = [0]*10
    # hist[i]: 주어진 구간에서 숫자 i의 과일 개수
    # hist[0]은 사용되지 않음.

    maxdist = 0

    # 포인터 j, k 운용. (j, k] 사이의 구간을 계산
    j = -1
    for k in range(N):
        hist[A[k]] += 1

        # hist 에서 개수가 0 이상인 숫자들의 개수.
        while len([ h for h in hist if h>0 ]) > 2:
            j += 1  # proceed j
            hist[A[j]] -= 1

        dist = k-j
        maxdist = max(maxdist, dist)

    return maxdist


N = int(input().strip())
A = list(map(int, input().split()))

print(solve(A))



'''
예제 입력 1
5
5 1 1 2 1
예제 출력 1
4

과일을 앞에서 $1$개, 뒤에서 $0$개의 과일을 빼면 남은 과일은  $1, 1, 2, 1$번 과일이 꽂혀있는 탕후루가 됩니다. 과일의 개수는
$4$개입니다.

예제 입력 2
3
1 1 1
예제 출력 2
3
탕후루가 이미 두 종류 이하의 과일로만 이루어져 있습니다.

예제 입력 3
9
1 2 3 4 5 6 7 8 9

예제 출력 3
2
과일을 앞에서 $3$개, 뒤에서 $4$개의 과일을 빼면 남은 과일은 $4, 5$번 과일이 꽂혀있는 탕후루가 됩니다. 과일의 개수는 $2$개입니다.


----

run=(python3 30804.py)

echo '5\n5 1 1 2 1' | $run
# -> 4
echo '3\n1 1 1' | $run
# -> 3
echo '9\n1 2 3 4 5 6 7 8 9' | $run
# -> 2
echo '1\n4' | $run
# -> 1
echo '8\n1 2 1 2 3 3 3 3' | $run
# -> 5


'''
