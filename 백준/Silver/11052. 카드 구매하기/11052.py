'''
11052번

카드 구매하기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	57412	35522	26917	61.773%

문제
요즘 민규네 동네에서는 스타트링크에서 만든 PS카드를 모으는 것이 유행이다.

PS카드는 PS(Problem Solving)분야에서 유명한 사람들의 아이디와 얼굴이 적혀있는 카드이다.
각각의 카드에는 등급을 나타내는 색이 칠해져 있고, 다음과 같이 8가지가 있다.

전설카드
레드카드
오렌지카드
퍼플카드
블루카드
청록카드
그린카드
그레이카드

카드는 카드팩의 형태로만 구매할 수 있고, 카드팩의 종류는 카드 1개가 포함된 카드팩, 카드 2개가 포함된 카드팩, ...
카드 N개가 포함된 카드팩과 같이 총 N가지가 존재한다.

민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿고 있다.
따라서, 민규는 돈을 최대한 많이 지불해서 카드 N개 구매하려고 한다. 카드가 i개 포함된 카드팩의 가격은 Pi원이다.

예를 들어, 카드팩이 총 4가지 종류가 있고, P1 = 1, P2 = 5, P3 = 6, P4 = 7인 경우에 민규가 카드 4개를 갖기 위해
지불해야 하는 금액의 최댓값은 10원이다. 2개 들어있는 카드팩을 2번 사면 된다.

P1 = 5, P2 = 2, P3 = 8, P4 = 10인 경우에는 카드가 1개 들어있는 카드팩을 4번 사면 20원이고,
이 경우가 민규가 지불해야 하는 금액의 최댓값이다.

마지막으로, P1 = 3, P2 = 5, P3 = 15, P4 = 16인 경우에는 3개 들어있는 카드팩과
1개 들어있는 카드팩을 구매해 18원을 지불하는 것이 최댓값이다.

카드 팩의 가격이 주어졌을 때, N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오.
N개보다 많은 개수의 카드를 산 다음, 나머지 카드를 버려서 N개를 만드는 것은 불가능하다.
즉, 구매한 카드팩에 포함되어 있는 카드 개수의 합은 N과 같아야 한다.

입력
첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)

둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

출력
첫째 줄에 민규가 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.


'''


import sys
input = sys.stdin.readline

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(pack_price:list) -> int:
    N = len(pack_price)
    pack_price = [0] + pack_price

    dp = [0] * (N+1)
    # dp[i]: 카드 i 장을 구매하기 위한 최대 가격

    for i in range(1, N+1):
        # 카드 i 장 구매는 다음과 같은 경우들로 구성
        #  - 카드 i장 팩 1개 구매
        #        pack_price[i]
        #  - 카드 i-1장 구매의 최대 가격에 카드 1장 추가 구매 가격 합
        #        dp[i-1] + pack_price[1]
        #  - 카드 i-2장 구매의 최대 가격에 카드 2팩 구매 가격 합
        #        dp[i-2] + pack_price[2]
        #  - ...
        #  - 카드 1장 구매 최대 가격에 카드 (i-1)팩의 구매 가격 합
        #        dp[1] + pack_price[i-1]
        # 위 경우 중 최대 값.
        #
        price = [pack_price[i]]

        for k in range(1, i):
            price.append(dp[i-k] + pack_price[k])

        dp[i] = max(price)

    return dp[N]


N = int(input().strip())
P = list(map(int, input().split()))
assert len(P) == N

print(solve(P))



'''
예제 입력 1
4
1 5 6 7
예제 출력 1
10

echo '4\n1 5 6 7' | python3 11052.py
-> 10

echo '5\n10 9 8 7 6' | python3 11052.py
-> 50

echo '10\n1 1 2 3 5 8 13 21 34 55' | python3 11052.py
-> 55

echo '10\n5 10 11 12 13 30 35 40 45 47' | python3 11052.py
-> 50

echo '4\n5 2 8 10' | python3 11052.py
-> 20

echo '4\n3 5 15 16' | python3 11052.py
-> 18

12
1 1 6 8 11 1 1 1 1 1 1 1
-> 25

(python3 <<EOF
N = 1000
print(N)
P = [1] * 500 + [ k for k in range(500,N) ]
print(' '.join([ str(e) for e in P ]))
EOF
) | time python3 11052.py
-> 1000


(python3 <<EOF
import time
from random import seed,randint
seed(time.time())
N = 1000
print(N)
print(' '.join([ str(randint(1,10_000)) for k in range(N) ]))
EOF
) | time python3 11052.py


'''

