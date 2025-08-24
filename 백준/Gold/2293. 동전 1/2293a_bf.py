'''

최초 풀이. brute_force 방식.
제출하면 당연히 시간 초과 뜰 것임.

다른 알고리즘의 정확성 검증을 위한 용도로 사용 가능.

-----
초기 스케치.

1, 2, 5 로 10을 만드는 경우의 수.

10을 만드는 경우의 수 = 9를 만드는 경우의 수 (여기에 1만 더하면 10이 되므로) + 8을 만드는 경우의 수 + 5를 만드는 경우의 수
하지만 이 방법은 중복 제거가 불가능.

5, 2, 1 로 순서 바꾸고..
5로만 만들기 1가지.
2로만 만들기 1가지.
1로만 만들기 1가지.
5와 2로 만들기. 1 (5,5)
5와 1로 만들기. 1 (5,1,1,1,1,1)
2와 1로 만들기.   (2,2,2,2,1,1) (2,2,2,)

55, 5221, 52111, 511111
22222, 222211, 2221111, 22111111, 211111111
1111111111
# -> 10
이건 그냥 브루트포스 같은데.. 어떻게 dp로 풀 수 있는가?


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input().rstrip()))
    return A,K

def solve_bruteforce(A:list[int], K:int)->int:
    '''
    1 ≤ N ≤ 100
    1 ≤ K ≤ 10,000

    미리 자리를 만들어 두고, 한 자리씩 채워나가기.
    backtracking 과 유사한 형태이긴 한데 가지치기는 따로 없음.

    '''
    N = len(A)
    A.sort(reverse=True)

    use = [0]*N
    # use[k] 는 k번째 동전의 사용 회수

    success_count = 0

    def populate(idx:int):
        '''
        idx 번째 자리의 동전을 채우기.
        '''
        nonlocal success_count
        if idx > N: return False
        value = sum( use[k]*A[k] for k in range(idx) )
        if value > K: return False
        if value == K:
            log("success, %s", use[:idx])
            success_count += 1
            return True
        if idx == N: return False
        max_n = (K - value) // A[idx]
        for c in range(max_n,-1,-1):
            use[idx] = c
            populate(idx+1)
        use[idx] = 0

    populate(0)
    return success_count



if __name__ == '__main__':
    inp = get_input()
    r = solve_bruteforce(*inp)
    print(r)


'''
예제 입력 1
3 10
1
2
5
예제 출력 1
10

----
run=(python3 2293a_bf.py)

echo '3 10\n1\n2\n5' | $run
# -> 10

echo '3 100\n1\n2\n5' | $run
# 541

echo '4 100\n1\n2\n5\n10' | $run
# 2156


'''


