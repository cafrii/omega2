def solve(nums:list):
    # max_len[num] 은 최종 숫자 num 으로 끝나는 가장 긴 부분 수열의 길이.

    max_n = max(nums)
    max_len = [ 0 ] * (max_n + 1)

    for n in nums:
        # n 이 이전 부분 수열의 뒤에 붙을 수 있는 경우는 끝 수가 n 보다 작아야 함.
        # n-1 까지 중 최대 길이를 찾고
        # 그 길이에 +1

        new_max = max(max_len[i] for i in range(n)) + 1

        if new_max > max_len[n]:
            max_len[n] = new_max

    return max(max_len)

N = int(input().strip())
A = list(map(int, input().split()))
print(solve(A))
