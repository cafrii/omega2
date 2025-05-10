'''
참고할 만한 다른 제출자들의 답변들..
주의: 직접 실행 안됨. 오류가 포함되어 있을 수도 있음..

대체로 좀 더 dp 스럽지만, 시간과 메모리는 더 소요하는 방식.

'''

# https://www.acmicpc.net/source/94089535

n,m = map(int,input().split())
memory = list(map(int,input().split()))
cost = list(map(int,input().split()))
k = sum(cost)

d = [0] * (k+1)
# index 가 cost 이고, d[i] 가 memory 를 의미함.

for i in range(n):
    a,c = memory[i], cost[i]
    for j in range(k,c-1,-1): d[j] = max(d[j], d[j-c] + a)

answer = 0
for i in range(k+1):
    if d[i] >= m:
        answer = i
        break
print(answer)


'''
echo '5 60\n30 10 20 35 40\n3 0 3 5 4' | python3 7579b.py

'''

# https://www.acmicpc.net/source/94089652

N, M = map(int, input().split())
bytes = list(map(int, input().split()))
price = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(sum(price)+1)]
# 2-d array.
# dp[cost][i]

for p in range(sum(price)+1):
    for i in range(1,N+1):
        if price[i-1] > p:
            dp[p][i] = dp[p][i-1]
        else:
            dp[p][i] = max(dp[p][i-1], dp[p-price[i-1]][i-1]+bytes[i-1])
        if dp[p][i] >= M:
            print(p)
            exit(0)

