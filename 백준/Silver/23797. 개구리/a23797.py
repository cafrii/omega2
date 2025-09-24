'''
23797번
개구리, 실버1

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	512 MB	1432	489	386	34.190%

문제
개구리의 울음소리는 K와 P가 번갈아서 나온다.
예를 들어, KPKP... 또는 PKPKPKPK... 는 개구리의 울음소리지만, KKPP는 아니다.
여러 개구리가 같이 울고있다. 다만, 개구리들이 우는 타이밍은 제멋대로라서 울음소리의 간격이 일정하지 않을 수 있다.
K와 P로 이루어진 문자열 S가 주어질 때, S에는 최소 몇 마리의 개구리가 울고있을까?

입력
첫째 줄에 S가 주어진다. 1≤|S|≤10^6

출력
가능한 개구리의 최소 마릿수를 출력한다.

'''

import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    S = input().rstrip()
    return S,

def solve0(S:str):
    # 각 개구리들의 마지막 울음소리
    frogs:list[str] = []

    for s in S:
        if s == 'K':
            if not frogs: frogs.append('K')
            else:
                # P 개구리가 있다면 그것을 선택. 없으면 새로 추가.
                if 'P' in frogs:
                    i = frogs.index('P')
                    frogs[i] = 'K'
                else:
                    frogs.append('K')
        elif s == 'P':
            if not frogs: frogs.append('P')
            else:
                if 'K' in frogs:
                    frogs[frogs.index('K')] = 'P'
                else:
                    frogs.append('P')
    return len(frogs)


def solve(S:str)->int:
    '''
    '''
    ftype = ['K', 'P']
    frogs = [ 0, 0 ]
    # frogs[0]: 마지막으로 ftype[0] (K)를 울었던 개구리의 수
    # frogs[1]:   ,,    ftype[1] (P)  ,,
    for s in S:
        k = ftype.index(s)  # 0 or 1
        # 현재 울음소리의 반대 소리를 마지막으로 울었던 개구리를 위치 조정.
        # 예: frogs[0] 에서 frogs[1] 로 이동.
        # 만약 반대 소리의 개구리가 없다면 개구리 한 마리가 새로 추가됨.
        if frogs[1-k] > 0:
            frogs[1-k] -= 1
        frogs[k] += 1
    return sum(frogs)



if __name__ == '__main__':
    print(solve(*get_input()))


'''
예제 입력 1
KKPKPPKKKP
예제 출력 1
3

---
run=(python3 a23797.py)

echo KKPKPPKKKP | $run
# 3

echo KKKPKKKK | $run
# 6

echo K | $run
# 1

'''