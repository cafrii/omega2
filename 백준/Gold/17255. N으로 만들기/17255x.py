'''

초기, 잘못된 구현.. 완성되지 않은 채로 중단.

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N

from collections import deque

def solve_wrong(N:int):
    '''
    '''
    # 자릿수 확인.
    digitstr = str(N)
    dlist = [ int(s) for s in digitstr ]
    length = len(dlist)
    dset = set(dlist) # digit set

    # dque = deque()
    array = [0] * length
    stack = [] # used_digit stack
    numset = set()

    def populate(step:int, left:int, right:int):
        '''
        step: 채우기 단계. 채워져 있는 숫자의 개수
        left, right: 현재 채워져 있는 숫자 그룹의 왼쪽/오른쪽 경계.
            slice 노테이션을 따른다.
        '''
        log("step %d, [%d:%d] %s", step, left, right, array[left:right])
        if right - left >= length:
            num = int(''.join(map(str, array)))
            seq = int(''.join(map(str, stack)))
            log("final %d, stack %d", num, seq)
            if num != N:
                log("not match!")
            elif seq in numset:
                log("dup!")
            else:
                numset.add(seq)
                log("     ====> %d, seq %d", num, seq)
            return

        if step == 0:
            # 아무 자리도 상관 없음.
            for i,d in enumerate(dlist):
                array[i] = d
                stack.append(d)
                populate(1, i, i+1)
                stack.pop()
            return
        if left > 0: # 왼쪽 채우기
            for x in dset - set(array[left:right]):
                array[left-1] = x
                log("   left fill %d..", x)
                stack.append(x)
                populate(step+1, left-1, right)
                stack.pop()

        if right < length: # 오른쪽 채우기
            for x in dset - set(array[left:right]):
                log("   right fill %d..", x)
                array[right] = x
                stack.append(x)
                populate(step+1, left, right+1)
                stack.pop()
        return

    populate(0, 0, 0)
    return




if __name__ == '__main__':
    inp = get_input()
    r = solve_wrong(inp)
    print(r)


'''

run=(python3 17255.py)

echo '123' | $run

echo '9111' | $run

예제 출력 2
4
'''

