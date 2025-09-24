import sys

def get_input():
    input = sys.stdin.readline
    S = input().rstrip()
    return S,

def solve(S:str):
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
