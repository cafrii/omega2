'''
1074번

Z 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.5 초 (추가 시간 없음)	512 MB	97154	41533	31042	42.677%

문제
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다.
예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.

입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.

제한
1 ≤ N ≤ 15
0 ≤ r, c < 2N

'''


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




'''

2 3 1
2**2 = 4
0  1  4  5
2  3  6  7
8  9  12 13
10 11 14 15


예제 입력 1
2 3 1
예제 출력 1
11

예제 입력 2
3 7 7
예제 출력 2
63

예제 입력 3
1 0 0
예제 출력 3
0

예제 입력 4
4 7 7
예제 출력 4
63

예제 입력 5
10 511 511
예제 출력 5
262143

예제 입력 6
10 512 512
예제 출력 6
786432


echo '15 3 7' | time python3 1074.py
-> 31
python3 1074.py  0.02s user 0.01s system 93% cpu 0.026 total

echo '15 60000 60000' | time python3 1074.py
-> 1073823522
python3 1074.py  0.02s user 0.01s system 94% cpu 0.027 total


'''