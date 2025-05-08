
def solve(N, r, c):
    # r, c 는 0-base 이다.

    def find_z(size, y, x) -> int:
        # size x size 의 서브 매트릭스 안에서 (y, x)가 몇번째 인지 찾는다.
        # 리턴 값은 0 ~ size**2-1 범위의 값이어야 한다.

        if size == 1:
            return 0
        if size == 2:
            # y, x 는 0 또는 1 이어야 함.
            return y*2 + x
        assert size % 2 == 0

        # 어느 사분면에 위치하는지에 따라 분할 정복
        half = size // 2
        half_square = half*half

        if 0 <= y < half:
            if 0 <= x < half:
                return find_z(half, y, x)
            else:
                return find_z(half, y, x-half) + half_square
        else:
            if 0 <= x < half:
                return find_z(half, y-half, x) + half_square*2
            else:
                return find_z(half, y-half, x-half) + half_square*3

    return find_z(2**N, r, c)


N,r,c = map(int, input().split())

print(solve(N,r,c))

