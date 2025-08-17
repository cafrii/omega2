
import sys

def get_input():
    input = sys.stdin.readline
    return input().rstrip()

def solve_fast(digitstr:str):
    '''
    '''
    length = len(digitstr)
    dlist = [ s for s in digitstr ]
    history_set = set()

    def search(left:int, right:int, hist:str):
        '''
        left, right: 현재 채워져 있는 숫자 그룹의 왼쪽/오른쪽 경계.
            slice 노테이션을 따른다.
        '''
        if right - left >= length:
            if hist in history_set: return # duplicate!
            history_set.add(hist)
            return
        if left > 0: # 왼쪽 채우기
            search(left-1, right, hist + ',' + ''.join(dlist[left-1:right]))
        if right < length: # 오른쪽 채우기
            search(left, right+1, hist + ',' + ''.join(dlist[left:right+1]))
        return

    for i,d in enumerate(dlist):
        search(i, i+1, d)
    return len(history_set)

if __name__ == '__main__':
    print(solve_fast(get_input()))

