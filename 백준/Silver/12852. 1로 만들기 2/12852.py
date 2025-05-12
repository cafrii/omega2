'''
12852번

 1로 만들기 2 성공스페셜 저지

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초	512 MB	37127	17548	13784	47.033%

문제

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다. 정답이 여러 가지인 경우에는 아무거나 출력한다.


--------------
참고
    1463 과 같은 문제인데, 출력해야 하는 값이 하나 더 있음.
    N을 1로 만드는 history를 유지 관리 해야 한다.

개선 1
    history 리스트를 유지할 경우, 약간 시간 제한을 넘는 것 같음. 그래서 일단 이전 dp index 만 기록 하고,
    맨 나중에 역추적하여 리스트를 생성하는 방식으로 변경했음.

다른 해법들
    dp 에 cnt 와 index 둘 다 추적하지 않고, 그냥 prev_index 만 추적하게 할 수도 있다.
    그러면 1 -> N 까지 dp 채우는 것이 좀 더 빨라진다.
    대신 나중에 답을 내는 과정에 좀 더 신경을 써야 함.

'''

import sys
input = sys.stdin.readline

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(N) -> tuple[int,list]:

    dp = [ None ] * (N+1)
    # dp[k] 는 (cnt,nums)
    #   cnt 는 k를 1로 만드는데 필요한 연산 횟수
    #   nums 는 위 연산 순서에 따라 만들어지는 중간 숫자들의 목록. 처음 k와 최종 1까지 포함.
    dp[1] = (0, 0)

    for k in range(2, N+1):
        candidates = []  # (cnt, prev_dp_index)
        kd2 = kd3 = -1
        if k % 3 == 0:
            kd3 = k // 3
            if kd3 >= 1:
                candidates.append((dp[kd3][0] + 1, kd3))
        if k % 2 == 0:
            kd2 = k // 2
            if kd2 != kd3 and kd2 >= 1:
                candidates.append((dp[kd2][0] + 1, kd2))
        km1 = k-1
        candidates.append((dp[km1][0] + 1, km1))

        cnt,prev_idx = min(candidates, key = lambda x: x[0])
        dp[k] = (cnt, prev_idx)

        # log('%d: cnt %d, %s', k, dp[k][0], dp[k][1])

    # construct nums list, tracking dp, starting from dp[N]
    idx = N
    nums = []
    while idx >= 1:
        nums.append(idx)
        idx = dp[idx][1]

    return dp[N][0], nums



def solve2(N) -> tuple[int,list]:

    dp = [ 0 ] * (N+1)
    # dp[k] 는 참조한 이전 dp 의 index
    dp[1] = 0

    for k in range(2, N+1):
        candidates = []  # (cnt, prev_dp_index)
        kd2 = kd3 = -1
        if k % 3 == 0:
            kd3 = k // 3
            if kd3 >= 1:
                candidates.append(kd3)
        if k % 2 == 0:
            kd2 = k // 2
            if kd2 != kd3 and kd2 >= 1:
                candidates.append(kd2)
        candidates.append(k - 1)

        dp[k] = min(candidates)
        # log('%d: cnt %d, %s', k, dp[k][0], dp[k][1])

    # construct nums list, tracking dp, starting from dp[N]
    count = 0
    idx = N
    nums = []
    while idx >= 1:
        nums.append(idx)
        idx = dp[idx][1]
        count += 1

    return count-1, nums # count 에서는 마지막 1은 제외 해야 함.

'''
속도 비교
solve()
    0.44s user 0.03s system 17% cpu 2.609 total

solve2()
    0.24s user 0.01s system 10% cpu 2.380 total
    거의 절반 정도로 시간이 단축되었음.

'''


N = int(input().strip())

cnt,nums = solve2(N)
print(cnt)
print(' '.join([ str(x) for x in nums ]))



'''
예제 입력 1
2
예제 출력 1
1
2 1

예제 입력 2
10
예제 출력 2
3
10 9 3 1
'''
