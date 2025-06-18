'''
2343번
기타 레슨 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	45826	16375	11348	33.879%

문제
강토는 자신의 기타 강의 동영상을 블루레이로 만들어 판매하려고 한다.
블루레이에는 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다.
순서가 뒤바뀌는 경우에는 강의의 흐름이 끊겨, 학생들이 대혼란에 빠질 수 있기 때문이다.
즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.

강토는 이 블루레이가 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고 한다.
오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다.
이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.

강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다.
다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다.
각 강의의 길이는 10,000분을 넘지 않는다.

출력
첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.

----

10:37~ 아이디어 채팅
11:26~53 구현

구분: 이분탐색으로 범위 좁히기

'''


import sys
input = sys.stdin.readline

def solve(A:list, M:int):
    '''
    '''
    def count_bl(L:int):
        # 주어진 L(블루레이 크기)로 녹화 시 블루레이 개수
        num_bl, psum = 1, 0 # number of blueray, partial sum
        for n in A:
            if psum + n <= L:
                psum += n
            else:
                num_bl,psum = num_bl+1,n
        return num_bl

    # lmin 은 최대 숫자 하나만 담을 수 있는 크기.
    # lmax 는 하나의 bl 에 모든 숫자를 다 담을 수 있는 크기.
    lmin,lmax = max(A),sum(A)

    while lmin < lmax:
        # 중간에서부터 시도.
        lmid = (lmin + lmax)//2
        if count_bl(lmid) <= M:
            # 일단은 만족. 더 좋은 해가 있는지 찾기 위해 범위 축소.
            lmin,lmax = lmin,lmid
        else:
            # M개에 포함하기 실패. L을 더 키워야 함.
            lmin,lmax = lmid+1,lmax
            if lmid == lmax:
                return lmid  # 굳이 시도해 보지 않아도, 됨.
    # 아마도 lmin == lmax 상태일 것임.
    return lmin


N,M = map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == N
print(solve(A, M))



'''
예제 입력 1
9 3
1 2 3 4 5 6 7 8 9
예제 출력 1
17

echo '9 3\n1 2 3 4 5 6 7 8 9' | $run
-> 17

echo '3 2\n1 1 1' | $run
-> 2

echo '9 4\n9 9 9 9 9 9 9 9 9' | $run
-> 27

'''
