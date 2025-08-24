'''
2293번
동전 1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	4 MB	76277	36839	28045	48.260%

문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
다음 n개의 줄에는 각각의 동전의 가치가 주어진다.
동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.


---
1.
처음에는 brute_force 로 먼저 구현 해 봄. -> 2293_bf.py

2.
계산 과정 중에 중복이 많이 눈에 띄어서, 그 부분을 memoization 으로 변환.
그러다 보니 2차원 dp 형태로 구현된.
코드가 쉽게 이해하기 어려운 구조인데다 worst case 입력 조건에서 시간 초과. 포기.
-> 2293b_dp2d.py

3.
힌트를 얻어서 1차원 dp로 변환.
처음에 이 방식을 얼른 생각해 내지 못했던 건
layered (staged?) 형태의 dp update 인데 그냥 sequential 하게만 생각했음.
이런 유형의 dp를 좀 더 풀어보아야 할 듯.


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input().rstrip()))
    return A,K



def solve_dp(A:list[int], K:int)->int:
    '''
    Args:
        A[]: list of unit price of each coin
        K: target value which we will compose using coins.
    Returns:
        the number of cases we can compose K using any number of provided coins.
    Algo:
        using 1-dimensional dp.
    '''

    # A.sort()
    # A.sort(reverse=True)
    # 이 dp 알고리즘은 동전 종류의 순서에 영향을 받지 않는것 같음.

    N = len(A)

    dp = [0] * (K+1)
    # dp[k]는 목표 k를 만들어내는 경우의 수.

    dp[0] = 1  # 아무 동전도 사용하지 않는 경우 1가지.

    # dp 는 전체 dp array가 여러 단계에 걸쳐 점진적으로 누적 업데이트 된다.

    # for i,c in enumerate(A):
    for i in range(N):
        c = A[i]
        # log("using coin[%d] %d", i, c)
        for k in range(c, K+1): # 증가하는 방향으로만 가능.
            dp[k] += dp[k-c]
        # log("  dp: %s", dp)

    return dp[K]


if __name__ == '__main__':
    inp = get_input()
    r = solve_dp(*inp)
    print(r)



'''
예제 입력 1
3 10
1
2
5
예제 출력 1
10



----
run=(python3 2293.py)

echo '3 10\n1\n2\n5' | $run
# -> 10

echo '3 100\n1\n2\n5' | $run
# 541

echo '4 100\n1\n2\n5\n10' | $run
# 2156

echo '5 100\n1\n2\n5\n10\n13' | $run
# 5643

echo '8 100\n1\n2\n5\n7\n11\n13\n17\n19' | $run
# 51777

#------------------
# 아래 문제들은 2^31 == 2147483648 보다 커서 문제 자격 안됨!

echo '6 10000\n1\n2\n5\n7\n11\n13' | $run
# 84064685830739

echo '7 10000\n1\n2\n5\n7\n11\n13\n17' | $run
# 8299786181715568

echo '8 10000\n1\n2\n5\n7\n11\n13\n17\n19' | $run
# 629947105727245350

echo '100 10000\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27\n28\n29\n30\n31\n32\n33\n34\n35\n36\n37\n38\n39\n40\n41\n42\n43\n44\n45\n46\n47\n48\n49\n50\n51\n52\n53\n54\n55\n56\n57\n58\n59\n60\n61\n62\n63\n64\n65\n66\n67\n68\n69\n70\n71\n72\n73\n74\n75\n76\n77\n78\n79\n80\n81\n82\n83\n84\n85\n86\n87\n88\n89\n90\n91\n92\n93\n94\n95\n96\n97\n98\n99\n100' | time $run
# 22683324467557455025270363928849330511235016373648534420498657018392011562024963097559021800
# $run  0.09s user 0.01s system 97% cpu 0.100 total


'''


