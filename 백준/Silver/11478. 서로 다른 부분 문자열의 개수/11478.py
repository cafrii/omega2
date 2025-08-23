'''
11478번
서로 다른 부분 문자열의 개수 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	41506	26482	21438	64.143%

문제
문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고,
서로 다른것의 개수는 12개이다.

입력
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

출력
첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.


----

10:17~10:27

----
개선:
단일 set 로 모든 substr 를 다 담아서 셈을 하는 것 보다,
좀 더 적은 크기의 여러 set 로 나눠서 세는 것이 좀 더 빠름.

예: 길이 1 짜리와 길이 2 짜리는 결코 겹치는 요소가 없을 것이므로 각각의 set 로 사용.

결과
97768389  cafrii  11478  맞았습니다!!  33432KB  180ms  Python 3  356B   <-- solve_fast()
97768003  cafrii  11478  맞았습니다!! 238308KB  416ms  Python 3  288B   <-- solve()

solve_fast() 버전이 메모리도 훨씬 더 적게 소모한다!

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def solve(s:str)->int:
    n = len(s) # length
    ss = set() # substring set
    for i in range(n):
        for j in range(i+1,n+1):
            # log("  '%s'", S[i:j])
            ss.add(s[i:j])
    return len(ss)

def solve_fast(s:str)->int:
    n = len(s)
    cnt = 0
    for sn in range(1,n+1): # substr length
        log("sn: %d", sn)
        ss = set() # substring set
        for k in range(n+1-sn):
            log("  '%s'", s[k:k+sn])
            ss.add(s[k:k+sn])
        cnt += len(ss)
    return cnt


if __name__ == '__main__':
    input = sys.stdin.readline
    s = input().rstrip()
    # print(solve(s))
    print(solve_fast(s))


'''
예제 입력 1
ababc
예제 출력 1
12

run=(python3 11478.py)

echo 'ababc' | $run
# 12


'''
