'''
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	167546	67115	56403	39.745%
문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1
60
100
예제 출력 1
620
61
예제 입력 2
64
65
예제 출력 2
-1

'''

# [M,N] = map(int, input().split())
M = int(input())
N = int(input())
# M <= N

is_prime = bytearray(N+1)

# fill is_prime with 1
for i in range(N+1):
    is_prime[i] = 1

is_prime[0] = is_prime[1] = 0

for i in range(2, N+1):
    if is_prime[i]:
        for k in range(i+i, N+1, i):
            is_prime[k] = 0

# extract prime numbers from M to N inclusive
# sum all these prime numbers and print
# get the minimum prime number and print

primes = [ i for i in range(M,N+1) if is_prime[i] ]
print(f'primes: {primes}')
print(sum(primes) if primes else -1)
# print(min(primes) if primes else '')
if primes: print(min(primes))



