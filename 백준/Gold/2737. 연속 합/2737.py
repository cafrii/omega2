'''
2737번

연속 합 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	780	363	303	59.412%

문제

대부분의 양의 정수는 적어도 2개 이상의 연속된 자연수의 합으로 나타낼 수 있다.

예를 들면 다음과 같다.
6 = 1 + 2 + 3
9 = 5 + 4 = 4 + 3 + 2

하지만, 8은 연속된 자연수 합으로 나타낼 수가 없다.

자연수 N이 주어졌을 때, 이 수를 적어도 2개 이상의 연속된 자연수의 합으로 나타낼 수 있는 경우의 수를 출력하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 정수 하나로 이루어져 있다.
이 정수는 문제에서 설명한 N이며, 231보다 작다.

출력
각 테스트 케이스에 대해서 N을 적어도 2개 이상의 연속된 자연수의 합으로 나타내는 경우의 수를 출력한다.


--------

1:
2:
3: 1,2
4:
5: 2,3
6: 1,2,3 - 중간수 2*3
7: 3,4 - 중간수 3.5*2


9: 4.5*2 - 4,5
   3*3 -> 2,3,4

10: 2*5 x
    3*3.3 x           // sl 이 홀수이면 자연수로 나눠 떨어져야 함.
    4*2.5 -> 1,2,3,4  // sl 이 짝수이면 x.5 형태가 되어야 함. 10*2%(sl) == 0, 10//sl = 2, lcenter, lcenter - sl//2 >= 0
    5*2       0 1 2 3 4

11:
    2*5.5 -> 5,6
    3*3.6
    4*2.7
    5*2.2
    6*1.8 ->

13:
    2*5.5

14:
    4*3.5
               2 3 4 5

15:
    5*3,   1 2 3 4 5
        // sl 이 홀수이면, 15%sl == 0, 15//sl==3, center, center - sl//2 >= 1


15: 6+9,  5+10

'''

import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(N):
    cnt = 0
    log("N: %d", N)

    # sl: sequence length
    for sl in range(2, N+1):
        # log("  sl: %d", sl)
        if sl % 2 == 0:
            lcenter = N // sl  # lower center
            least = lcenter - sl//2 + 1
            if least < 1:
                log("    !! stop: sl %d: lcenter %d least %d", sl, lcenter, least)
                break

            # sl 이 짝수이면 N/sl 은 *.5 형태가 되어야 함.
            if 2*N % sl != 0 or N%sl == 0:
                log("    ! skip sl %d, %.2f", sl, N/sl)
                continue

            # 예: N==14, sl==4, N/sl = 3.5, lcenter = 3
            # seq:  2 3 (3.5) 4 5
            seq = list(range(lcenter - sl//2 + 1, lcenter - sl//2 + 1 + sl))
            log("    sl %d: lcenter %d, %s = %d", sl, lcenter, '+'.join(map(str,seq)), sum(seq))
            cnt += 1

        else:
            # sl 이 홀수이면 N은 sl로 나누어 떨어지는 수 이어야 함.
            if N % sl != 0:
                log("    ! skip sl %d, %.2f", sl, N/sl)
                continue

            center = N // sl
            # center 를 중심으로 양쪽에 sl//2 개 씩의 숫자가 붙어야 함.
            least = center - sl//2
            if least < 1:
                break
            # 예: N=15, sl=5, center = 15/5 = 3
            # center - sl//2 = 3 - 5//2 = 3-2 = 1, ok
            # seq:  1 2 3 4 5
            seq = list(range(center - sl//2, center - sl//2 + sl))
            log("    sl %d: center %d, %s = %d", sl, center, '+'.join(map(str,seq)), sum(seq))
            cnt += 1

    return cnt



T = int(input().strip())
qs = [0]*T  # questions
ans = {} # answer dict for caching

for k in range(T):
    n = int(input().strip())
    qs[k] = n
    if n in ans: # if already solved
        continue
    ans[n] = solve(n)

# print ans lately
for k in qs:
    print(ans[k])

'''
run=(time python3 2737.py)
run=(time python3 2737.py 2> /dev/null)

echo '3\n6\n9\n8' | $run

echo '1\n1800' | $run

echo '1\n987654321' | $run
echo '1\n987654323' | $run
echo '1\n987654325' | $run

echo '2\n6\n987654321' | $run


echo '7\n6\n9\n8\n1800\n987654321\n987654323\n987654325' | $run


'''
