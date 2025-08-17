'''

제출 후 pass 된 버전.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

def solve3_pass(N:int):
    '''
    제출 후 pass 된 버전.
    '''
    digitstr = str(N)
    length = len(digitstr)
    dlist = [ s for s in digitstr ]
    stack:list[str] = [] # history
    history_set = set()

    def populate(left:int, right:int):
        '''
        left, right: 현재 채워져 있는 숫자 그룹의 왼쪽/오른쪽 경계.
            slice 노테이션을 따른다.
        '''
        ###log("(%d) [%d:%d] %s", right-left, left, right, dlist[left:right])

        if right - left >= length:
            # history = ''.join(stack)
            # log("final %s, stack %s", digitstr, history)
            history = ','.join(stack)
            if history in history_set: return # duplicate!
            history_set.add(history)
            log("     ====> %d, seq %s", len(history_set), history)
            return

        if left == right: # 시작. 모든 자리에서 시작 가능.
            for i,d in enumerate(dlist):
                stack.append(d)
                populate(i, i+1)
                stack.pop()
            return
        if left > 0: # 왼쪽 채우기
            ###log("    left fill %s", dlist[left-1])
            stack.append(''.join(dlist[left-1:right]))
            populate(left-1, right)
            stack.pop()
        if right < length: # 오른쪽 채우기
            ###log("    right fill %s", dlist[right])
            stack.append(''.join(dlist[left:right+1]))
            populate(left, right+1)
            stack.pop()
        return

    populate(0, 0)
    return len(history_set)



if __name__ == '__main__':
    inp = get_input()
    print(solve3_pass(inp))




'''

run=(python3 17255.py)

echo '123' | $run
# -> 4

echo '9111' | $run
# -> 4

echo '21112' | $run
# -> 4
# -> 8 이 나와야 이 문제 출제자 의도에 맞음.


'''

