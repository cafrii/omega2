
import sys

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

def solve3(N:int):
    '''
    '''
    digitstr = str(N)
    length = len(digitstr)
    dlist = [ s for s in digitstr ]
    stack = [] # history
    history_set = set()

    def populate(left:int, right:int):
        '''
        left, right: 현재 채워져 있는 숫자 그룹의 왼쪽/오른쪽 경계.
            slice 노테이션을 따른다.
        '''
        if right - left >= length:
            history = ','.join(stack)
            if history in history_set: return # duplicate!
            history_set.add(history)
            return
        if left == right: # 시작. 모든 자리에서 시작 가능.
            for i,d in enumerate(dlist):
                stack.append(d)
                populate(i, i+1)
                stack.pop()
            return
        if left > 0: # 왼쪽 채우기
            # 주의: 채워져 가는 경로도 모두 중복 체크에 포함되도록 채점되는 것으로 보임.
            # 새로 채워지는 숫자 만 기록하지 않고 채워진 후의 전체 숫자를 history에 추가.
            stack.append(''.join(dlist[left-1:right]))
            populate(left-1, right)
            stack.pop()
        if right < length: # 오른쪽 채우기
            stack.append(''.join(dlist[left:right+1]))
            populate(left, right+1)
            stack.pop()
        return

    populate(0, 0)
    return len(history_set)

if __name__ == '__main__':
    inp = get_input()
    print(solve3(inp))

