'''
25947번
선물할인, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	3148	805	625	26.928%

문제
n개의 선물 가격이 주어졌을 때, b의 예산으로 최대로 많은 선물을 사려고 한다.
이때 최대 a개의 선물에 대해서는 반값 할인을 받을 수 있다고 했을 때
최대로 살 수 있는 선물의 수를 구하는 프로그램을 작성하시오.
단, 한 선물에는 최대 한 번만 반값 할인을 받을 수 있다.

입력
입력은 표준입력을 사용한다.

첫 번째 줄에 선물의 개수를 나타내는 양의 정수 n (1 ≤ n ≤ 100,000),
예산을 나타내는 양의 정수 b (1 ≤ b ≤ 10^9),
반값 할인을 받을 수 있는 최대 선물의 수를 나타내는 정수
a (0 ≤ a ≤ n)가 공백을 사이에 두고 차례로 주어진다.

다음 줄에 n개의 선물 가격이 공백을 사이에 두고 주어진다.
선물 가격은 2이상 10억 이하의 값을 갖으며, 항상 짝수로 주어진다.

출력
출력은 표준출력을 사용한다.
조건을 만족하며 최대로 살 수 있는 선물의 수를 출력한다.

----

10:31~


26, 2개
2 4 6 8 10/2 12

23 1
2 4 6 8 12 14
1 2 3 4  6  7



'''

import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    N,B,A = map(int, input().split())
    P = list(map(int, input().split()))
    return N,B,A,P


'''
최종적으로 제출한 버전.
수행 시간은 완전 동일함.
'''
def solve_short(N:int, budget:int, half:int, p:list[int])->int:
    p.sort()
    tsum,b = 0,0
    for c in range(N):
        tsum += p[c]//2
        if c - b + 1 > half:
            tsum += (p[b] // 2)
            b += 1
        if tsum > budget:
            return c
        elif tsum == budget:
            return c+1
    return N


def solve(N:int, budget:int, half:int, p:list[int])->int:
    p.sort()
    tsum = 0

    if half > 0:
        b = 0
        for c in range(N):
            tsum += p[c]//2
            if c - b + 1 > half:
                tsum += (p[b] // 2)
                b += 1
            if tsum > budget:
                return c
            elif tsum == budget:
                return c+1
    else:
        for c in range(N):
            tsum += p[c]
            if tsum > budget:
                return c
            elif tsum == budget:
                return c+1

    return N


def solve1(N:int, budget:int, half:int, p:list[int])->int:
    '''
    Args:
    Returns:
    '''
    p.sort() # prices

    b,c = 0,0  # index
    # p[0] 부터 p[c-1] 인덱스의 선물까지 구매 고려 대상
    # 그 중 p[b]부터는 반값 할인 적용

    # total price sum
    tsum = (p[0] if half == 0 else p[0]//2)
    if tsum > budget:
        # 맨 처음 선물 하나 골랐을 뿐인데 이미 예산 초과.
        return 0

    # 두번째 선물부터 하나씩 구매 가능 여부 판단.
    for c in range(1, N): # c: 1 ~ N-1
        delta = p[c]

        # 새로운 선물 c를 반값으로 받을 수 있는지 확인.
        # c를 포함한 반값 선물 개수가 허용 범위 초과이면..
        if half > 0:
            if c - b + 1 > half:
                # 기존 반값 할인 받은 것중 하나를 반값이 아닌 정가로 구매해야 함.
                tsum += (p[b] // 2)  # 반값 할인 무효. 나머지 반값 추가 지출.
                b += 1
            delta = p[c]//2
        tsum += delta
        # 이제 물건 c는 반값 구매 가능함
        if tsum > budget:
            # 예산 초과. c 구매 불가능. 0 부터 c-1 까지 총 c 개만 구매 가능.
            return c
        elif tsum == budget:
            return c+1

    # 여기까지 왔다면 모든 선물을 예산 내에 구매 했음.
    return N


if __name__ == '__main__':
    print(solve_short(*get_input()))


'''
예제 입력 1
6 26 2
4 6 2 10 8 12
예제 출력 1
5
예제 입력 2
6 23 1
4 6 2 12 8 14
예제 출력 2
4

----
pr=25947
run=(python3 a$pr.py)

echo '6 26 2\n4 6 2 10 8 12' | $run
# 5
echo '6 23 1\n4 6 2 12 8 14' | $run
# 4

echo '1 10 0\n5' | $run
# 1
echo '1 10 0\n20' | $run
# 0
echo '1 10 1\n20' | $run
# 1
echo '2 10 2\n12 8' | $run
# 2


echo '6 0 2\n4 6 2 10 8 12' | $run
# 0
echo '3 10 0\n1 2 7' | $run
# 3
echo '1 1 1\n2' | $run
# 1


echo '3 3 3\n2 2 2' | $run
# 3
echo '3 6 3\n2 4 6' | $run
# 3
echo '3 10 2\n2 4 6' | $run
# 3


echo '3 10 0\n1 2 7' | $run
# 3
echo '1 1 1\n2' | $run
# 1
echo '3 3 3\n2 2 2' | $run
# 3
echo '3 6 3\n2 4 6' | $run
# 3
echo '3 10 2\n2 4 6' | $run
# 3


'''
