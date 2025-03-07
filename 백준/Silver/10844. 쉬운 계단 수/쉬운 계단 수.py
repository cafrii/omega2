
def solve(len):
    # len: 1~100

    num = [ 0 ] * 10
    # num[i]는 해당 단계(step)에서 끝자리가 i 로 끝나는 계단수의 개수.

    # step 1: 1 자리 숫자. 0 은 해당 안됨.
    for k in range(1, 10):
        num[k] = 1

    # step 2 부터는 이터레이션.
    for step in range(2, len+1):
        # len 2)
        next = [0]*10
        next[0] = num[1]
        for k in range(1, 9):
            next[k] = num[k-1] + num[k+1]
        next[9] = num[8]
        num = next

    # return sum(num)
    # return int(str(sum(num))[-9:])
    return sum(num) % 1_000_000_000


N = int(input().strip())
print(solve(N))
