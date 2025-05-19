'''
15654

N과 M (5) 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	49677	36115	28616	72.108%

문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

N개의 자연수 중에서 M개를 고른 수열
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.


8:31~42 1차 코딩 완료.
9:02 제출. 문제를 잘못 이해해서 런타임 에러로 1회 실패했음.

'''

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
nums = list(sorted(map(int, input().split())))
assert len(nums) == N

arr = [0] * M
# used = [0] * 10 # 0~9. used[0] is not used.
used = {}

def back(idx):
    if idx >= M:
        print(*arr)
        return
    for k in nums:
        # check if k is already used.
        if used.get(k, 0): continue
        arr[idx] = k
        used[k] = 1
        back(idx + 1)
        used[k] = 0

back(0)


'''
예제 입력 1
3 1
4 5 2
예제 출력 1
2
4
5

echo '3 1\n4 5 2' | python3 15654.py

예제 입력 2
4 2
9 8 7 1
예제 출력 2
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8

echo '4 2\n9 8 7 1' | python3 15654.py



echo '3 2\n55 66 77' | python3 15654.py


'''



