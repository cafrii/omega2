'''

https://www.acmicpc.net/source/87341275

bfs 가 아니라 dfs 를 적용했다. 이게 최적의 해를 찾음을 어떻게 보장하는 것인가?

몇가지 눈에 띄는 점은, n//3 과 n//2 의 중복도 있지만 그건 dp로 해결함.


'''

dp = {1:0,2:1,3:1,4:2,6:2}
def dfs(n):
    if n in dp:
        return dp[n]
    r = min(dfs(n//3)+n%3,dfs(n//2)+n%2) + 1
    dp[n] = r
    return dp[n]
print(dfs(int(input())))

