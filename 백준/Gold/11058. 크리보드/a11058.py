'''
11058번
크리보드, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	8654	3924	3143	44.531%

문제
크리보드는 kriii가 만든 신기한 키보드이다. 크리보드에는 버튼이 4개만 있으며, 하는 역할은 다음과 같다.

1. 화면에 A를 출력한다.
2. Ctrl-A: 화면을 전체 선택한다
3. Ctrl-C: 전체 선택한 내용을 버퍼에 복사한다
4. Ctrl-V: 버퍼가 비어있지 않은 경우에는 화면에 출력된 문자열의 바로 뒤에 버퍼의 내용을 붙여넣는다.

크리보드의 버튼을 총 N번 눌러서 화면에 출력된 A개수를 최대로하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
크리보드의 버튼을 총 N번 눌러서 화면에 출력할 수 있는 A 개수의 최댓값을 출력한다.

----

9/10, 11:48~12:38

----
키 1회 누르는 것을 cost 1 라고 간주.
화면에 표시된 A 개수를 value 라고 하자.

# A 단독 사용의 경우
A: cost 1, 1+
A A .. A: cost N, N+

# 시퀀스 사용의 경우
CA CC CV: cost 3, 두배 2x
CA CC CV CV: cost 4, 3x
CA CC CV CV CV: cost 5, 4x
CA CC CV CV CV CV: cost 6, 5x
CA CC CV1 ... CVk: cost k+2, (k+1)x

# CV가 길수록 cost 당 얻는 가치 비율도 커짐.

cost 사용, +value 획득, 1차원 dp로 풀이.
가능한 모든 배율 (multiply)을 다 시도해야 함.


-----
채점 확인 완료

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N,

def solve(N:int)->int:
    '''
    올려보기 방식. 현재 step 에서 미래의 dp들을 단계적 갱신.
    '''

    max_n = 100
    # dp[k]: cost k에서의 A 표시 최대 출력 수

    dp = [ k for k in range(max_n+1) ]
    # A 키만 사용하는 경우: cost k, value k

    # log("dp: %s", dp[1:N+1])

    for k in range(1, N+1): # k: 1 ~ 100

        for ratio in range(2, N+1): # r: 2 ~ 100
            # ratio range 최대는 충분히 크면 됨.
            c = ratio+1  # extra cost. x2:3, x3:4, ...
            if k+c > N: break

            # 올려서 보기
            dp[k+c] = max(dp[k+c], dp[k] * ratio)
            # log("dp[%d]=%d x %d -> dp[%d]=%d", k, dp[k], ratio, k+c, dp[k+c])

            # 내려 보기도 가능함.

        # log("k=%2d, dp %s", k, dp[1:N+1])

    return dp[N]



def solve2(N:int)->int:
    '''
    내려 보기 방식. 현재 dp 를 구하기 위해 과거 dp 값을 참고.
    '''

    max_n = 100
    # dp[k]: cost k에서의 A 표시 최대 출력 수

    dp = [ k for k in range(max_n+1) ]
    # A 키만 사용하는 경우: cost k, value k

    # 내려 보기 방식.
    for k in range(1, N+1): # k: 1 ~ 100
        # dp[k]:
        #  dp[k-3]*2, dp[k-4]*3, dp[k-5]*4, .. dp[1]*? 들 중에서 최대 값 선택.
        if k <= 3: continue
        dp[k] = max(dp[k],
                    max( dp[j]*(k-j-1) for j in range(k-3,0,-1) )
                )
    return dp[N]


if __name__ == '__main__':
    # print(solve(*get_input()))
    print(solve2(*get_input()))



'''
예제 입력 1
3
예제 출력 1
3
예제 입력 2
7
예제 출력 2
9
예제 입력 3
11
예제 출력 3
27
----

run=(python3 a11058.py)

echo 3 | $run
# 3
echo 7 | $run
# 9
echo 11 | $run
# 27

echo 15 | $run
# 81
echo 100 | $run
# 1391569403904

'''
