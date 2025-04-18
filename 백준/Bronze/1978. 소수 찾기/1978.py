'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1
4
1 3 5 7
'''

import sys
MAX = 1000

N = int(input().strip())
nums = list(map(int, input().split()))
# assert(len(nums) == N)

is_prime = [1] * (MAX + 1) # 0~MAX
is_prime[:2] = [0, 0] # 0 and 1 is not prime

for k in range(2, int(MAX**0.5)+1): # 2 ~ root(MAX)
    if not is_prime[k]: continue
    for j in range(k*2, MAX+1, k): # 2k, 3k, 4k, ...
        is_prime[j] = 0

# print(is_prime, file=sys.stderr)

# 리스트 num 중에서 is_prime[num]==1 인 것의 개수 출력
print(sum(is_prime[x] for x in nums))

