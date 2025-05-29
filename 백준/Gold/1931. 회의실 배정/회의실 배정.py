import sys
input = sys.stdin.readline

def solve(A:list[tuple[int,int]])->int:
    # 끝나는 시간 기준으로 오름차순 정렬. 동일한 종료 시각일 경우 시작 시각도 고려
    A.sort(key = lambda t: (t[1], t[0]))

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

