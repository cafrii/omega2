import sys
input = sys.stdin.readline


# 최대 N: 50
# 수열의 수: -1,000 ~ 1,000
# 최소 sum = -1000*1000*25 = -25000000
MINF = int(-1e9)


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

print(solve_optimum(A))
