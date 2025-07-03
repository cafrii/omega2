'''
1744
수 묶기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	50776	18111	14331	34.540%

문제
길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다.
하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다.
하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다.
그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.

수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

입력
첫째 줄에 수열의 크기 N이 주어진다. N은 50보다 작은 자연수이다. 둘째 줄부터 N개의 줄에 수열의 각 수가 주어진다. 수열의 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
수를 합이 최대가 나오게 묶었을 때 합을 출력한다.


-------

3:35~4:44 greedy 문제 실패! timeout!

'''


import sys
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

# 최대 N: 50
# 수열의 수: -1,000 ~ 1,000
# 최소 sum = -1000*1000*25 = -25000000
MINF = int(-1e9)


def backtrack(A1:list[int], A2:list[int])->int:
    '''
    A1 은 묶이지 않은 단일 수 목록
    A2 는 두 개가 묶여서 합쳐진 수 목록. 다시 묶을 수 없음.

    A1 에서 일부를 선택하여 묶는 경우를 검토하여 가장 sum이 큰 값을 리턴.
    '''
    # 묶지 않은 상태에서 한번 계산
    max_sum = sum(A1)+sum(A2)
    log("==== A1: %s, A2: %s", A1, A2)

    if len(A1) < 2: # 더 이상 묶을 수 없음.
        return max_sum

    # A1 에서 두 개를 선택하여 묶기
    for i in range(len(A1)):
        A1m1 = A1[:i] + A1[i+1:]  # A1[] 에서 A1[i]를 제외한 나머지
        log("    a1m1: %s", A1m1)
        for k in range(i, len(A1m1)):
            A1m2 = A1m1[:k] + A1m1[k+1:]
            A2.append(A1[i] * A1m1[k])
            sum1 = backtrack(A1m2, A2)
            A2.pop()
            max_sum = max(max_sum, sum1)

    return max_sum


def solve_greedy(A:list[int])->int:
    '''
    '''
    A.sort()
    A2:list[int] = [] # for pair-ed num. initially empty.
    return backtrack(A, A2)


def solve_try1(A:list[int])->int:
    A.sort()
    log("A: %s", A)

    negatives,positives,zeros,ones = [],[],[],[]
    for a in A:
        if a <= -1:
            negatives.append(a)
        elif a == 0:
            zeros.append(a)
        elif a == 1:
            ones.append(a)
        else:
            positives.append(a)

    pairs = []

    negatives.sort(reverse=True)
    while len(negatives) >=2 :
        pairs.append(negatives[-1]*negatives[-2])
        del negatives[-2:]

    positives.sort()
    while len(positives) >=2 :
        pairs.append(positives[-1]*positives[-2])
        del positives[-2:]

    assert len(positives) <= 1 and len(negatives) <= 1

    if zeros and negatives:
        # 0 하나와 음수 자투리 묶어서 없애기
        del negatives[-1]
        del zeros[-1]

    # zero 들은 모두 그냥 버리면 됨.
    if ones:
        pairs.append(sum(ones))

    log("pos: %s, neg: %s, pairs: %s", positives, negatives, pairs)
    return backtrack(positives + negatives, pairs)



def solve_optimum(A:list[int])->int:
    '''
    네 자연수 a,b,c,d 에 대해서 1 < a < b < c < d 일때
    ab+cd 가 항상 ac+bd, ad+bc 보다 크다는 것을 증명할 수 있다.

    음수, 양수 구분하고
    양수 중에서 1보다 큰 수 들에 대해서는 항상 묶어야 한다.
    묶을 때에는 가장 큰 수 부터 묶어야 한다.

    음수는 반드시 음수끼리 묶어서 양수로 만들어야 한다.
    이때에도 절대값이 큰 수끼리 먼저 묶는다.

    홀수개 라서 묶이지 않은 자투리는 그냥 남긴다.

    묶을 수 있는 모든 묶음 수를 제외하면, 나머지는 다음과 같다.
    음수 자투리, 0, 1, 양수 자투리

    // 나머지들은 몇 개 안될테니 그냥 greedy 로 푸는 게 좋겠다.
    자투리로만 12개가 넘으면 timeout 된다!
    (숫자가 중복되지 않는다 라는 조건이 없으니..)

    숫자 0: 마이너스 자투리가 있다면 묶어서 없애야 함. 그렇지 않다면 그냥 더하기.
    숫자 1: 곱하기 보다는 더하기가 유리. 항상.

    '''

    negatives,positives,zeros,ones = [],[],[],[]
    for a in A:
        if a <= -1:
            negatives.append(a)
        elif a == 0:
            zeros.append(a)
        elif a == 1:
            ones.append(a)
        else:
            positives.append(a)

    pairs = []

    negatives.sort(reverse=True)
    while len(negatives) >=2 :
        pairs.append(negatives[-1]*negatives[-2])
        del negatives[-2:]

    positives.sort()
    while len(positives) >=2 :
        pairs.append(positives[-1]*positives[-2])
        del positives[-2:]

    assert len(positives) <= 1 and len(negatives) <= 1

    if zeros and negatives:
        # 0 하나와 음수 자투리 묶어서 없애기
        del negatives[-1]
        del zeros[-1]

    # zero 들은 모두 그냥 버리면 됨.
    if ones:
        pairs.append(sum(ones))

    # log("pos: %s, neg: %s, pairs: %s", positives, negatives, pairs)
    return sum(positives) + sum(negatives) + sum(pairs)




N = int(input().strip())
A = []
for _ in range(N):
    A.append(int(input().strip()))

# print(solve_greedy(A))
# print(solve_try1(A))
print(solve_optimum(A))


'''
예제 입력 1
4
-1
2
1
3
예제 출력 1
6

run=(python3 1744.py)
echo '4\n-1\n2\n1\n3' | $run
-> 6

echo '4\n-1\n2\n1\n3' | $run
echo '6\n0\n1\n2\n4\n3\n5' | $run
echo '1\n-1' | $run
echo '3\n-1\n0\n1' | $run
echo '2\n1\n1' | $run
->
6 27 -1 1 2




예제 입력 2
6
0
1
2
4
3
5
예제 출력 2
27

예제 입력 3
1
-1
예제 출력 3
-1

예제 입력 4
3
-1
0
1
예제 출력 4
1

예제 입력 5
2
1
1
예제 출력 5
2


시간제한 시뮬레이션

export _N=8

(python3 <<EOF
import os
N = int(os.getenv("_N", "10"))
print(N)
for k in range(1,N+1):
    print(k)
EOF
) | time $run

export _N=11
-> 251
$run  0.69s user 0.01s system 98% cpu 0.712 total

export _N=12
-> 323
$run  7.39s user 0.03s system 99% cpu 7.447 total

greedy 로는 N 값이 12만 되어도 timeout!!

export _N=50
-> 21451
$run  7.39s user 0.03s system 99% cpu 7.447 total


echo '12\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1' | time $run
-> 12
$run  0.02s user 0.01s system 68% cpu 0.053 total


echo '12\n1\n1\n1\n1\n1\n0\n0\n0\n0\n0\n0\n0' | time $run
-> 5

echo '12\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12' | time $run
-> 323

echo '11\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12' | time $run
-> 322

echo '12\n-1\n-2\n-3\n-4\n-5\n-6\n-7\n-8\n-9\n-10\n-11\n-12' | time $run
-> 322


echo '4\n-4\n0\n1\n3' | $run
-> 4

echo '7\n3\n2\n1\n0\n-3\n-2\n-1' | $run
-> 13


echo '42\n-282\n-865\n153\n-63\n-419\n48\n528\n-754\n-460\n-790\n125\n258\n-326\n386\n340\n-101\n225\n-805\n55\n-429\n-640\n-717\n-662\n88\n-41\n-538\n885\n-509\n791\n810\n-485\n938\n41\n104\n105\n-453\n556\n430\n155\n787\n-593\n-873' | $run
-> 5792654
??

pos: [41], neg: [-41],
pairs: [755145, 635950, 540618, 423680, 319034, 246865, 208380, 179751, 91932, 6363,
    830130, 640710, 437572, 227040, 131240, 58050, 23715, 13125, 9152, 2640]
5816885

pos: [41], neg: [-41], pairs: [830130, 640710, 437572, 227040, 131240, 58050, 23715, 13125, 9152, 2640, 755145, 635950, 540618, 423680, 319034, 246865, 208380, 179751, 91932, 6363]
5792654

out/a
755145 635950 540618 423680 319034 246865 208380 179751 91932 6363
830130 640710 437572 227040 131240 58050 23715 13125 9152 2640
5781092


755145+635950+540618+423680+319034+246865+208380+179751+91932+6363+830130+640710+437572+227040+131240+58050+23715+13125+9152+2640
-> 5781092




'''
