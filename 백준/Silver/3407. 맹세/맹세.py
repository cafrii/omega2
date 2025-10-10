
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
