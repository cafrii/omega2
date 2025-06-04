'''
15663번

N과 M (9) 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	54914	27709	21151	49.466%

문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수 중에서 M개를 고른 수열

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.


----
9:58~10:30   어려운 문제도 아닌데 좀 헤맸음. 중복 처리 조건 잘 생각해야 함.

'''


import sys
input = sys.stdin.readline

def solve(A:list, M:int):
    N = len(A)
    arr = [0]*M

    def populate(index, digits:list):
        if index >= M:
            print(*arr)
            return
        d2 = sorted(set(digits))
        for k in d2:
            arr[index] = k
            d3 = digits.copy(); d3.remove(k)  # digits 에서 k 하나만 제거한 것.
            populate(index + 1, d3)
            arr[index] = 0

    populate(0, A)


# set, sort 등의 사용을 최소화 하도록 개선해 본 코드.
# 하지만 별 차이는 없었음.
def solve2(A:list, M:int):
    N = len(A)
    A.sort()
    target = [0]*M  # target array that should be composed
    used = [0]*N  # flag which input digits are used

    def populate(index):
        if index >= M:
            print(*target)
            return
        prev = 0
        for j in range(N):
            if used[j]: # 앞 단계에서 사용된 숫자 skip
                continue
            digit = A[j]  # 이번 단계에서 사용할 숫자
            if digit == prev: # 앞 루프에서 사용된 숫자 skip
                continue

            target[index],used[j] = digit,1
            populate(index + 1)
            target[index],used[j],prev = 0,0,digit

    populate(0)




N,M = map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == N
solve2(A, M)



'''
예제 입력 1
3 1
4 4 2
예제 출력 1
2
4

예제 입력 2
4 2
9 7 9 1
예제 출력 2
1 7
1 9
7 1
7 9
9 1
9 7
9 9

예제 입력 3
4 4
1 1 1 1
예제 출력 3
1 1 1 1

------

8 8
8 7 6 5 4 3 2 1
-> 총 40320 라인...

8 8
1 1 1 1 1 1 1 2
-> 8 가지 경우


run=(python3 15663.py)

echo '8 8\n8 7 6 5 4 3 2 1' | time $run > /dev/null
-> 0.09s

# 개선 코드도 성능 면에서 별 차이는 없음.



'''


