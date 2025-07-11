'''

이 문제를 dfs 로 풀어버리다니!!!

https://www.acmicpc.net/source/96181539


이 코드가 효율적인 이유를 극단적으로 설명하는 예시는 다음과 같다.

### 와 #### 는 가로로 연결된 세 셀의 합을 구하는 것 까지는 동일하고
  #
그 다음 밑으로 내려가느냐, 더 오른쪽으로 가느냐 차이만 있다.
그래서 앞의 세 sum 계산을 공유하게 된다.


또 가지치기 기법도 사용되고 있는데
(  if 1000*(4-n) + sm < mx:  )

이 아이디어는 기존 내 구현에도 적용해 볼 순 있는데, 셀 숫자들의 범위가 아주 크지 않으면
그 효과는 별로 크진 않다.

'''


import sys
input = sys.stdin.readline

def dfs(n, sm, tlst):
    global mx
    if n == 4:
        mx = max(sm, mx)
        return
    if 1000*(4-n) + sm < mx:
        return
    for cn, cm in tlst:
        for k in range(4):
            nn = cn + dn[k]
            nm = cm + dm[k]
            if 0<=nn<N and 0<=nm<M:
                if v[nn][nm] == 0:
                    v[nn][nm] = 1
                    dfs(n+1, sm+arr[nn][nm], tlst+[(nn,nm)])
                    v[nn][nm] = 0

N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
dn = [1, 0, -1, 0]
dm = [0, 1, 0, -1]
mx = 0
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(1, arr[i][j], [(i,j)])
print(mx)


