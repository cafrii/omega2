
import sys
input = sys.stdin.readline

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
        price = [pack_price[i]]
        for k in range(1, i):
            price.append(dp[i-k] + pack_price[k])
        dp[i] = max(price)

    return dp[N]


N = int(input().strip())
P = list(map(int, input().split()))
assert len(P) == N

print(solve(P))
