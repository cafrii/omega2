'''
2565번
전깃줄, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	47592	23350	18694	48.642%

문제
두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다.
합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄,
A의 3번 위치와 B의 9번 위치를 잇는 전깃줄,
A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.

< 그림 1 >

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다.
전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때,
남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다.
둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다.
위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

출력
첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.


------

LIS (longest increasing sequence)의 응용
채점 완료.


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)


# MAX_N = 500

def get_input():
    input = sys.stdin.readline
    M = int(input().rstrip()) # M: 1 ~ 100
    L = [] # link array
    for _ in range(M):
        a,b = map(int, input().split())
        L.append((a, b))
    return L,


def solve(L:list[tuple[int,int]])->int:
    '''
    '''
    L.sort(key=lambda x:x[0])

    R,S = zip(*L)
    # R is sorted, increasing order
    # problem: S 에서 LIS 의 길이를 찾으면 됨.

    # log("R: %s", R)
    # log("S: %s", S)

    N = len(S)
    dp = [ 0 for _ in range(N) ]
    # dp[k]는 S[k]를 마지막으로 포함하는 sub-sequence 의 LIS 길이

    dp[0] = 1  # 단일 요소는 항상 IS

    for k in range(1, N):
        s = S[k] # s: 현재 검토 중인 seq 의 마지막 숫자
        # s 를 덧붙일 수 있는 IS 들 중 최대 길이 찾기
        mx = 1
        for j in range(k): # j: 0 ~ k-1
            if S[j] >= s: continue
            # 이제 S[j] < s 이므로 S[j] 뒤에 s 를 붙일 수 있음.
            mx = max(mx, dp[j]+1)
        dp[k] = mx
        # log("dp: %s", dp[:k+1])

    # LIS 길이는 max(dp). LIS 에 포함 안되는 나머지는 모두 제거 필요.
    return N - max(dp)


if __name__ == '__main__':
    print(solve(*get_input()))



'''
예제 입력 1
run=(python3 2565.py)

echo '8\n1 8\n3 9\n2 2\n4 1\n6 4\n10 10\n9 7\n7 6' | $run

예제 출력 1
3

echo '4\n5 7\n6 8\n7 5\n8 6' | $run
# 2

echo '6\n1 1\n2 2\n3 5\n4 3\n5 4\n6 6' | $run
# 1

echo '50\n56 65\n54 25\n75 79\n81 9\n95 44\n70 24\n36 19\n3 88\n50 58\n12 37\n88 16\n8 46\n44 38\n53 55\n32 6\n47 60\n96 42\n17 27\n66 20\n59 89\n7 43\n69 51\n57 75\n91 63\n14 10\n74 80\n92 50\n73 87\n77 90\n1 7\n19 53\n72 64\n64 48\n86 97\n45 76\n68 91\n34 94\n99 52\n16 4\n63 11\n2 66\n25 56\n35 57\n80 39\n84 29\n49 13\n97 41\n93 30\n58 62\n40 22' | $run
# 38

echo '80\n91 57\n35 46\n12 66\n10 82\n61 84\n20 19\n3 59\n83 87\n86 53\n69 33\n66 42\n54 18\n72 55\n15 52\n32 64\n77 91\n29 90\n81 80\n74 11\n27 9\n19 10\n92 98\n37 48\n100 47\n6 44\n63 75\n41 65\n44 97\n58 78\n26 30\n25 36\n85 24\n11 29\n76 43\n79 49\n46 71\n99 41\n59 28\n56 3\n22 76\n34 17\n23 22\n80 68\n45 2\n28 72\n94 93\n73 60\n62 12\n4 7\n38 83\n13 62\n7 56\n48 63\n90 81\n39 1\n96 74\n24 69\n68 86\n75 25\n1 27\n82 95\n98 6\n64 51\n42 70\n47 34\n18 21\n21 38\n8 4\n36 5\n53 77\n87 31\n97 32\n33 14\n14 50\n31 96\n51 15\n57 8\n9 73\n70 20\n50 79' | $run
# 63



(python3 <<EOF
import time
from random import seed,randint,shuffle
seed(time.time())
N,M = 50,100
print(N)
R,S = list(range(1,M+1)),list(range(1,M+1))
shuffle(R); shuffle(S)
R,S = R[:N],S[:N]
print('\n'.join(f'{a} {b}' for a,b in zip(R,S)))
EOF
) | time $run



'''

