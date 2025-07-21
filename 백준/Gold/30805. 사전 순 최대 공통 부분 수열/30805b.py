'''

아래 코드는 알고리즘에 문제가 있어서 결국 실패.

성공하지 못하는 TC 예:

6
9 7 1 7 9 4
6
9 7 4 9 7 1

echo '6\n9 7 1 7 9 4\n6\n9 7 4 9 7 1' | $run

정답: 2, 9 9
오답: 2, 9 7 1

뒤에서부터 채워 오다가 lgcs 가 다시 큰 수로 리셋되어야 하는 경우를 대응하지 못함.
더 큰 수가 앞에 붙게 되면 이후는 다시 원점에서 다 검토해야 함
이렇게 되면 dp의 효과를 별로 볼 수 없음!


이 코드는 기록 용도로 남겨둠.


-------

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def read_quiz():
    input = sys.stdin.readline
    N = int(input().strip())
    A = list(map(int, input().split()))
    assert len(A) == N, "wrong number of A elem."
    M = int(input().strip())
    B = list(map(int, input().split()))
    assert len(B) == M, "wrong number of B elem."
    return A,B



def index2(iterable, x, defval=-1):
    for i, item in enumerate(iterable):
        if item == x:
            return i
    return defval

def get_lgcs2(A:list[int], B:list[int])->list[int]:
    '''
    using recursive
    '''
    if not (A and B): # both should not be empty
        return []
    if len(A) == len(B) == 1:
        return [A[0]] if A[0]==B[0] else []
    for n in range(100,-1,-1):
        ia = index2(A, n)
        if ia < 0: continue
        ib = index2(B, n)
        if ib < 0: continue
        return [n] + get_lgcs2(A[ia+1:], B[ib+1:])
    return [] # no lgcs

def solve_recursive(A:list[int], B:list[int])->list[int]:
    return get_lgcs2(A, B)



def index3(L:list, e, idx_not_found=-1):
    '''
        e 가 L 에 포함되어 있는지 검사하고 index 리턴.
        여럿이 일치하는 경우 가장 나중에 일치하는 것 선택 (가장 큰 index)
    '''
    length = len(L)
    for i, item in enumerate(reversed(L)):
        if item == e:
            return length-1-i
    return idx_not_found # 발견되지 않는 경우의 리턴값


def select_lgcs(C:list[list[int]])->int:
    '''
    Args:
        list of lgcs candidates. each lgcs is list of integers, whose length is variable.
    Returns:
        index of selected lgcs (0>=)
    Notes:
        comparison operation on python list behaves the same way as this quiz,
        which is lexicographical,
        left to right on each element,
        and shorter list is less than longer one.
    '''
    return C.index(max(*C))


def solve_dp(A:list[int], B:list[int])->list[int]:
    '''

    '''
    N,M = len(A),len(B)

    dp = [ [ [[],-1,-1] for m in range(M) ] for n in range(N) ]
    '''
    dp[][] 의 구성:
        dp[j][k] 는 A[j:] 와 B[k:] 사이의 lgcs 정보로서, [lgcs, gia, gib] 형식.
        g 는 lgcs 의 첫번째 숫자.
        gia 는 그 첫번재 숫자 g가 A[j:]에서의 위치 (인덱스). j <= gia.
        gib 는 그 첫번재 숫자 g가 B[k:]에서의 위치 (인덱스). k <= gib.

    dp[j][k] 구하기
        dp[j][k] 를 구하기 위해서는 기존에 구한 lgcs 정보를 활용해야 하는데,
        다음과 같은 두가지 경우를 모두 검사한 후 하나를 선택하여 저장.

        dp[j+1][k]
            A[j+1:] 과 B[k:] 의 lgcs 정보이다.
            기존 lgcs 의 맨 앞에 새로운 A[j] 추가될 수 있는가 를 검사해야 한다.
            그렇게 하려면,
            (1) A[j]가 기존 lgcs 의 g 보다 크거나 같고,
            (2) B[k:gib] 중에 A[j]가 있는지 검사해야 함.
                있다면 그 B[k:gib] 에서 발견된 A[j]의 index(원본 B 기준)을 기록해 둔다.
                여럿이 발견될 경우 '맨 뒤'의 것을 기록한다.
            그 결과 새로운 g,gib 의 후보를 찾는다.
        dp[j][k+1]
            위와 비슷한 방식으로,
            새로운 g, gia 의 후보를 찾는다.

        위 둘 중에 선택하는 기준:
            lgcs를 비교하여 더 큰 gcs를 선택.
    '''
    # 루프는 뒤에서부터.. 어느 축을 먼저 할 것인지는 상관이 없음.

    # if A[N-1] == B[M-1]:
    #     dp[N-1][M-1] = [ [A[N-1]], N-1, M-1 ]

    for j in range(N-1, -1, -1):
        for k in range(M-1, -1, -1):

            log("[%d][%d]: %s, %s", j, k, A[j:], B[k:])
            cand = [] # candidate

            # consider dp[j+1][k]:
            if j+1 < N:
                new = A[j]
                lgcs,gia,gib = dp[j+1][k]
                if not lgcs: # lgcs is empty. gia,gib should be -1
                    pass
                elif new < lgcs[0]:
                    cand.append([lgcs, gia, gib]) # no update. use previous one.
                else:
                    idx = index3(B[k:gib], new)
                    if idx >= 0:
                        lgcs,gia,gib = [new]+lgcs, j, k+idx
                        cand.append([lgcs, gia, gib]) # lgcs is updated.
                    else:
                        cand.append([lgcs, gia, gib]) # no update. use previous one.

            # consider dp[j][k+1]:
            if k+1 < M:
                new = B[k]
                lgcs,gia,gib = dp[j][k+1]
                if not lgcs: # lgcs is empty. gia,gib should be -1
                    pass
                elif new < lgcs[0]:
                    cand.append([lgcs, gia, gib]) # no update. use previous one.
                else:
                    idx = index3(A[j:gia], new)
                    if idx >= 0:
                        lgcs,gia,gib = [new]+lgcs, j+idx, k
                        cand.append([lgcs, gia, gib]) # lgcs is updated.
                    else:
                        cand.append([lgcs, gia, gib]) # no update. use previous one.

            log("   c: %s", cand)

            if len(cand) > 1:
                # 목록 중에 제일 적당한 것을 선택
                selected = select_lgcs([ c[0] for c in cand ])
                dp[j][k] = cand[selected]
            elif cand:
                dp[j][k] = cand[0]
            else:
                if A[j] == B[k]:
                    dp[j][k] = [ [A[j]], j, k ] # single element lgcs

            log("       --> %s, gia:%d, gib:%d", dp[j][k][0], dp[j][k][1], dp[j][k][2])

        # for k
    # for j
    return dp[0][0][0]




if __name__ == '__main__':
    A,B = read_quiz()
    K = solve_dp(A,B)
    print(len(K))
    if K:
        print(' '.join(str(k) for k in K))

    # K = solve_recursive(A,B)
    # print(len(K))
    # if K:
    #     print(' '.join(str(k) for k in K))


'''
예제 입력 1
4
1 9 7 3
5
1 8 7 5 3
예제 출력 1
2
7 3


run=(python3 30805.py)

echo '4\n1 9 7 3\n5\n1 8 7 5 3' | $run
-> 2, 7 3

echo '2\n100 100\n2\n100 100' | $run
-> 2, 100 100

echo '9\n5 4 3 1 5 3 7 5 5\n8\n5 7 2 1 3 5 4 3' | $run
-> 2, 7 5


echo '100\n13 29 50 36 2 27 45 2 9 10 4 29 37 17 34 34 84 90 92 83 43 25 54 12 29 53 100 74 89 25 87 84 75 45 1 12 10 51 11 7 27 38 10 40 2 41 83 3 87 45 35 44 35 20 73 44 73 22 64 18 100 33 3 20 61 82 61 69 94 20 20 2 3 33 25 30 51 46 18 47 60 55 52 94 74 86 8 50 67 24 36 41 67 23 16 19 62 37 68 10\n100\n57 96 52 17 39 62 25 49 12 14 55 100 65 42 65 83 29 67 75 18 60 25 40 67 22 25 95 36 69 51 94 49 50 18 92 65 91 15 22 25 77 23 55 53 30 54 12 45 26 15 96 84 60 19 93 45 1 20 27 26 42 37 20 89 16 57 64 68 72 17 43 6 38 94 46 16 21 56 9 64 45 47 4 81 50 51 60 92 14 84 83 7 1 61 69 41 54 64 64 44' | time $run
-> 5, 100 94 94 50 41
오답:
3, 100 94 68
처음에 68 이 먼저 잡혀 버린 이후에, 이게 나중에 41 로 갱신이 안됨.


echo '4\n8 1 1 7\n4\n8 1 1 7' | $run
-> 2, 8 7


echo '10\n9 8 7 6 5 1 2 3 4 5\n8\n1 3 5 7 9 6 5 4' | $run
-> 4, 9 6 5 4


echo '7\n7 2 5 3 5 2 4\n8\n1 7 2 5 3 5 3 4' | $run
-> 4, 7 5 5 4

echo '100\n100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100\n100\n100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100 100' | time $run
-> 100, 100 ... 100 # 100 이 100개

$run  0.02s user 0.01s system 62% cpu 0.041 total
# 이 문제는 길이가 100 으로 제한이 되어 있어서 그리 시간이 많이 걸리진 않는다.





'''

