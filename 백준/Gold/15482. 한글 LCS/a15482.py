'''
15482번
한글 LCS, 골드5

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	1837	990	814	57.405%

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, "최백준"과 "백준온라인"의 LCS는 "백준"이고, "스타트링크"와 "스트라토캐스터"의 LCS는 "스트"이다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다.
문자열은 최대 1000글자이고, 유니코드 U+AC00(가)부터 U+D7A3(힣)까지로만 이루어져 있으며,
UTF-8로 인코딩 되어 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.


--------
9/29
input()의 utf-8 처리 기능을 그냥 활용.
일반 lcs 풀이와 동일하게 진행함.

검증 완료.

'''


# import sys

# def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    # input = sys.stdin.readline
    # utf-8 자동 변환 기능을 활용하기 위해서는 original input() 함수가 필요.
    A = input().rstrip()
    B = input().rstrip()
    return A,B

def solve(A:str, B:str)->int:
    '''
    '''

    Na,Nb = len(A),len(B)

    dp = [ [0]*(Nb+1) for _ in range(Na+1) ]

    for ka in range(1, Na+1):
        for kb in range(1, Nb+1):
            if A[ka-1] == B[kb-1]:
                dp[ka][kb] = dp[ka-1][kb-1] + 1
            else:
                dp[ka][kb] = max(dp[ka-1][kb], dp[ka][kb-1])

    return dp[Na][Nb]

if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
최백준
백준온라인
예제 출력 1
2
예제 입력 2
스타트링크
스트라토캐스터
예제 출력 2
2
예제 입력 3
선데이코딩
딩코이데선
예제 출력 3
1
예제 입력 4
가나다라가나다라
가다나가다라
예제 출력 4
5

--------
run=(python3 a15482.py)

echo '최백준\n백준온라인' | $run
# 2
echo '스타트링크\n스트라토캐스터' | $run
# 2
echo '선데이코딩\n딩코이데선' | $run
# 1
echo '가나다라가나다라\n가다나가다라' | $run
# 5






'''