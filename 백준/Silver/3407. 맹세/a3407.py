'''
3407번
맹세 성공 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	1484	364	288	26.841%

문제
위대한 화학자 김선영은 그를 바라보며 굳은 맹세를 했다.
"난 오늘부터 원소 기호로 이루어진 단어만을 말할 것이다."
선영이는 "I Am CLaRa"를 말할 수 있다.
I 는 아이오딘, Am은 아메리슘, C는 탄소, La는 란타넘, Ra는 라듐이다.
또, 선영이는 "InTeRnAtIONAl"도 말할 수 있다.
하지만, "collegiate", "programming", "contest"는 원소 기호로 이루어진 단어가 아니기 때문에 말할 수 없다.

단어가 주어졌을 때, 선영이가 말할 수 있는 단어 인지 (원소 기호가 연결된 단어) 아닌지를 구하는 프로그램을 작성하시오.
(대소문자는 가리지 않는다)
다음은 이 문제에서 사용하는 원소 주기율표이다.
..

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
다음 T개의 줄에는 알파벳 소문자로만 된 단어가 하나 주어진다.
단어의 길이는 50,000을 넘지 않으며 양수이다.

출력
입력으로 주어진 단어가 선영이가 발음할 수 있는 단어라면 YES를, 아니라면 NO를 출력한다.

---
dp 로 간단하게 처리. 해싱을 이용한 문자열 빠른 조회


알고리즘 분류에 그래프 관련 언급이 되어 있음?
그래프 탐색은 어떤 방법을 말하는 것인가?

제출 완료

'''


log = (lambda fmt, *args: print(fmt % args, file=sys.stderr)) \
    if __import__('os').getenv('DBG') else (lambda *args, **kwargs: None)


def get_input():
    import sys
    input = sys.stdin.readline
    T = int(input().rstrip())
    A = [ input().rstrip() for _ in range(T) ]
    return A,

def solve(A:list[str])->list[str]:
    '''
    Returns:
        list of 'YES' or 'NO'
    '''

    names = ['H','He','Li','Be','B','C','N','O','F','Ne',
             'Na','Mg','Al','Si','P','S','Cl','Ar',
             'K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr',
             'Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe',
             'Cs','Ba','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn',
             'Fr','Ra','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Fl','Lv',
             'La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu',
             'Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr',
    ]
    names2 = [ e.lower() for e in names ]

    # convert list to dict for fast access
    namedic = {}
    for n in names2:
        namedic[n] = 1

    def check(s:str)->str:
        sz = len(s)  # 최소 길이는 1 (문제 조건: 양수)
        s = s.lower()

        dp = [0] * (sz+1)
        # dp[k]는 문자열 s의 첫 k개가 원소이름으로만 구성 되었는지 여부. yes 이면 1
        # dp[1]이 첫번째 문자열 상태 저장
        dp[0] = 1
        dp[1] = 1 if s[0] in namedic else 0

        for k in range(2, sz+1):  # k: 2 ~ sz
            # 경우의 수는 두가지: 단글자 또는 두글자
            if dp[k-1] and s[k-1] in namedic: # 단글자
                dp[k] = 1
            elif dp[k-2] and s[k-2:k] in namedic: # 두글자
                dp[k] = 1

            if dp[k-1]==0 and dp[k]==0:
                return 'NO'

        return 'YES' if dp[sz] else 'NO'

    return [ check(s) for s in A ]


if __name__ == '__main__':
    print('\n'.join(solve(*get_input())))


'''
예제 입력 1
4
international
collegiate
programming
contest
예제 출력 1
YES
NO
NO
NO

----
run=(python3 a3407.py)

echo '4\ninternational\ncollegiate\nprogramming\ncontest' | $run
# YES
# NO
# NO
# NO

echo '2\nalcheznu\nsIvvEurNarkKozR' | $run
# YES
# YES


'''














