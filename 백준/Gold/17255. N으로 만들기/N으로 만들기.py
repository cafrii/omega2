import sys

def get_input():
    input = sys.stdin.readline
    return input().rstrip()

def solve_opt(digitstr:str):
    '''
    solve_fast 에서 개선. 완성된 숫자에서 거꾸로 역추적.
    sliced index 위치 관리가 불필요하여 더 간편함.
    '''
    history_set = set()

    def back(dstr:str, hist:str):
        # dstr 라는 숫자가 완성되는 경우를 역추적.
        hist = dstr + hist
        if len(dstr) == 1:
            history_set.add(hist)
        else:
            back(dstr[1:], hist) # 왼쪽 숫자 잘라내기
            back(dstr[:-1], hist) # 오른쪽 숫자 잘라내기
        return

    back(digitstr, '')
    return len(history_set)

if __name__ == '__main__':
    print(solve_opt(get_input()))
