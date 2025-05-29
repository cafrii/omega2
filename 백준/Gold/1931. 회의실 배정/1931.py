'''
1931번

회의실 배정 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	254284	86130	59246	31.417%

문제
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

입력
첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.


--------

딱히 알고리즘 적으로 난이도 높은 문제는 아닌듯 한데, 논리적 문제 해석 능력이 필요함.

8:48~9:02
9:06~9:31 재채점 완료
'''


import sys
input = sys.stdin.readline

# MAX_N = 100_000

def solve_failed(A:list[tuple[int,int]])->int:
    # 끝나는 시간 기준으로 오름차순 정렬. 동일한 종료 시각일 경우 짧은 회의 먼저 (시작 시각이 늦은 것부터)
    A.sort(key = lambda t: (t[1],-t[0]))
    print(A)

    num = len(A)
    # dp = [0] * (MAX_N+1)
    dp = [ [0,0] for x in range(num+1) ]
    # dp[k][0]: 회의 개수
    #      [1]: 마지막 회의가 끝나는 시각

    for k in range(1, num+1):
        s,e = A[k-1]
        if dp[k-1][1] <= s:
            dp[k][:] = [dp[k-1][0] + 1, e]
        else:
            dp[k][:] = dp[k-1]

    return dp[num][0]



def solve(A:list[tuple[int,int]])->int:
    # 끝나는 시간 기준으로 오름차순 정렬. 동일한 종료 시각일 경우 시작 시각도 고려
    A.sort(key = lambda t: (t[1], t[0]))
    print(A, file=sys.stderr)

    num_meetings = 0 # 조건을 만족하는 회의 개수
    last_meeting_end = 0 # 조건 만족하는 마지막 회의가 끝나는 시각

    for s,e in A:
        if last_meeting_end <= s:
            num_meetings += 1
            last_meeting_end = e

    return num_meetings


N = int(input().strip())
A = []
for _ in range(N):
    s,e = map(int, input().split())
    A.append((s, e))

print(solve(A))




'''

echo '11\n1 4\n3 5\n0 6\n5 7\n3 8\n5 9\n6 10\n8 11\n8 12\n2 13\n12 14' | python3 1931.py
-> 4

3
1 4
4 5
2 4
-> 2

3
1 1
1 1
1 2
-> 3

6
1 5
1 2
2 3
3 4
4 5
5 6
-> 5

5
1 1
2 3
2 2
2 2
2 2
-> 5

7
11 64
80 86
16 55
55 83
32 80
72 76
9 12
-> 4


5
3 3
1 2
2 3
3 4
4 5
-> 5


'''

