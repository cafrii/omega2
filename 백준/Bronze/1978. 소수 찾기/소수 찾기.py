
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

print(sum(is_prime[x] for x in nums))
