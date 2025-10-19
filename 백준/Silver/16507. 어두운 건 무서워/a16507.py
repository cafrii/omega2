'''
16507번
어두운 건 무서워 성공, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초 (하단 참고)	512 MB	3590	2272	1944	65.388%

문제
호근이는 겁이 많아 어두운 것을 싫어한다.
호근이에게 어떤 사진을 보여주려는데 사진의 밝기가 평균 이상이 되지 않으면 일절 보려 하지 않는다.
호근이가 이 사진에서 일부분이라도 볼 수 있는 부분을 찾아주자.


위 그림은 호근이에게 보여줄 5×6 크기의 사진이며, 각 픽셀은 밝기를 나타낸다.
호근이가 사진의 일부분이라도 볼 수 있는지 알아보기 위해서는
두 점 (r1, c1)과 (r2, c2)를 꼭짓점으로 하는 직사각형의 밝기 평균을 구해야 한다.
예를 들어, 위 그림에서는 (2, 2)와 (4, 5)를 꼭짓점으로 하는 직사각형을 말한다.

호근이에게 보여줄 R×C 크기의 사진이 주어질 때, 사진의 일부분에 해당하는 밝기 평균을 구하여라.

입력
첫 번째 줄에는 사진의 크기를 의미하는 정수 R, C (1 ≤ R, C ≤ 1,000)와
사진 일부분의 밝기 평균을 알아볼 개수를 의미하는 정수 Q (1 ≤ Q ≤ 10,000)가 주어진다.

다음 R개의 줄에 걸쳐 R×C 크기의 사진 정보가 주어지며,
사진의 각 픽셀에는 밝기를 의미하는 정수 K (1 ≤ K ≤ 1,000)가 주어진다.

다음 Q개의 각 줄에는 사진의 일부분을 나타내기 위한 두 꼭짓점을 의미하는
정수 r1, c1, r2, c2 (1 ≤ r1 ≤ r2 ≤ R, 1 ≤ c1 ≤ c2 ≤ C)가 주어진다.

출력
Q개의 각 줄에 주어진 사진에서 두 점 (r1, c1)과 (r2, c2)를 꼭짓점으로 하는
직사각형의 밝기 평균을 출력한다. 평균은 정수 나눗셈으로 몫만 취한다.

----
7:49~8:04

----
평범한 누적합 구현

'''


import sys

log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)

def get_input():
    input = sys.stdin.readline
    R,C,Q = map(int, input().split())
    A = []
    for _ in range(R):
        A.append(list(map(int, input().split())))
        assert len(A[-1]) == C
    B = []
    for _ in range(Q):
        B.append(list(map(int, input().split())))
        assert len(B[-1]) == 4
    return A,B

def solve(A:list[list[int]], B:list[list[int]])->list[int]:
    '''
    Args:
    Returns:
    '''
    R,C = len(A),len(A[0])

    # partial sum
    psum = [ [0]*(C+1) for _ in range(R+1) ]

    for r in range(1,R+1):
        rsum = 0
        for c in range(1,C+1):
            rsum += A[r-1][c-1]
            psum[r][c] = psum[r-1][c] + rsum

    ans = []
    for r1,c1,r2,c2 in B:
        tsum = psum[r2][c2] - psum[r1-1][c2] - psum[r2][c1-1] + psum[r1-1][c1-1]
        area = (r2-r1+1)*(c2-c1+1)
        ans.append(tsum // area)

    return ans

if __name__ == '__main__':
    print('\n'.join(map(str, solve(*get_input()))))


'''
예제 입력 1
5 6 1
4 1 3 4 9 5
1 2 8 7 5 5
8 1 2 5 3 2
1 5 3 4 2 5
5 2 1 2 3 5
2 2 4 5
예제 출력 1
3

예제 입력 2
4 3 5
25 93 64
10 29 85
80 63 71
99 58 86
2 2 2 3
3 2 3 3
1 2 2 2
1 2 4 3
2 3 2 3
예제 출력 2
57
67
61
68
85


----
run=(python3 a16507.py)

echo '5 6 1\n4 1 3 4 9 5\n1 2 8 7 5 5\n8 1 2 5 3 2\n1 5 3 4 2 5\n5 2 1 2 3 5\n2 2 4 5' | $run
# 3

echo '4 3 5\n25 93 64\n10 29 85\n80 63 71\n99 58 86\n2 2 2 3\n3 2 3 3\n1 2 2 2\n1 2 4 3\n2 3 2 3' | $run
# 57  67  61  68  85

echo '1 1 2\n3\n1 1 1 1\n1 1 1 1' | $run
# 3  3


'''
