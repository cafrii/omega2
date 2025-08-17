'''

17255c.py 에서 좀 더 개선된 버전.
외부 stack 에서 push/pop 하는 대신, history 를 계속 만들어 가며 재귀 호출 인자로 전달해 줌.
호출 인자 자체가 stack 역할을 하기 때문에, 하는 일은 거의 같지만 코드가 단순해 짐.
(명시적인 push, pop 코드가 필요 없어지기 때문)

'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    return input().rstrip()


def solve_fast(digitstr:str):
    '''
    solve3 에서 좀 더 속도를 개선한 버전..
    '''
    length = len(digitstr)
    dlist = [ s for s in digitstr ]
    history_set = set()

    def search(left:int, right:int, hist:str):
        '''
        left, right: 현재 채워져 있는 숫자 그룹의 왼쪽/오른쪽 경계.
            slice 노테이션을 따른다.
        '''
        ###log("(%d) [%d:%d] %s", right-left, left, right, dlist[left:right])

        if right - left >= length:
            # log("final %s, hist %s", digitstr, hist)
            if hist in history_set: return # duplicate!
            history_set.add(hist)
            log("     ====> %d, seq %s", len(history_set), hist)
            return
        if left > 0: # 왼쪽 채우기
            ###log("    left fill %s", dlist[left-1])
            search(left-1, right, hist + ''.join(dlist[left-1:right]))
        if right < length: # 오른쪽 채우기
            ###log("    right fill %s", dlist[right])
            search(left, right+1, hist + ''.join(dlist[left:right+1]))
        return

    for i,d in enumerate(dlist):
        search(i, i+1, d)

    return len(history_set)


if __name__ == '__main__':
    print(solve_fast(get_input()))




'''

run=(python3 17255.py)

echo '123' | $run
# -> 4

echo '9111' | $run
# -> 4

echo '21112' | $run
#  ====> 1, seq 2,21,211,2111,21112
#  ====> 2, seq 1,21,211,2111,21112
#  ====> 3, seq 1,11,211,2111,21112
#  ====> 4, seq 1,11,111,2111,21112
#  ====> 5, seq 1,11,111,1112,21112
#  ====> 6, seq 1,11,112,1112,21112
#  ====> 7, seq 1,12,112,1112,21112
#  ====> 8, seq 2,12,112,1112,21112
# -> 8


'''

