


def solve2(n:int, digits:list)->int:
    digits.sort(reverse=True)
    n_str = str(n)
    n_len = len(n_str)

    def find_largest(index, current_num):
        if index == n_len:
            return int(current_num) if int(current_num) <= n else -1

        for digit in digits:
            next_num = current_num + str(digit)
            if index == 0 and digit == 0:
              continue

            if int(next_num) <= int(n_str[:index+1]):
                result = find_largest(index + 1, next_num)
                if result != -1:
                    if result <= n:
                      return result

        for digit in digits:
            next_num = str(digit) * (n_len - len(current_num))

            if len(next_num) != n_len - len(current_num):
                continue

            if index == 0 and digit == 0:
              continue

            if n_str[:index] + str(digit) > n_str[:index + 1]:
               continue

            result = int(current_num + str(digit) + next_num[:len(next_num)])

            if result <= n:
                return result
        return -1

    result = find_largest(0, "")
    if result == -1:
        temp = ""
        # 가장 큰 숫자로만 자리수 하나 적은 수를 만들어 리턴.
        for i in range(n_len-1):
            temp += str(digits[0])

    return temp if temp != "" else "0"


N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve2(N, A))
