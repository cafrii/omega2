'''
17255번
N으로 만들기 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	1883	944	724	49.691%

문제
준하는 노트에 수를 적다가 수가 만들어지는 방식을 깨달았다.

처음에 어떤 숫자 하나를 적고 만들어진 수의 왼쪽이나 오른쪽에 숫자를 계속 붙이면 어떤 수 N이든 만들 수 있다는 것이다.

다시 말해 어떤 수 N을 만들기 위해서는, 처음에 어떤 숫자를 하나 적고 아래의 두 가지 행동을 반복한다.

수의 왼쪽에 숫자를 하나 적는다.
수의 오른쪽에 숫자를 하나 적는다.

준하는 어떤 수 N을 만드는 방법의 수가 몇 가지인지 궁금해졌다. 이를 알아내는 프로그램을 작성해주자.
숫자를 적는 과정에서 나온 수가 순서대로 모두 같다면 같은 방법이다.

단, 숫자를 적는 과정에서 수는 0으로 시작할 수 있다.

입력
음이 아닌 정수 N이 주어진다. (0 ≤ N ≤ 10,000,000)

출력
N을 만드는 방법의 수를 출력한다.
----

2:45~

일단 각 경우의 수 별로 모두 탐색해 보는 방법을 시도.
이때의 문제는 중복을 어떻게 감지할 것인지 이다.

자릿수는 최대 8 자리. (대부분 7자리임.)
단순 8자리 숫자의 순열은 8! = 40320. 즉, 별로 크지 않은 수 이다.

간편한 방법: 숫자를 리스트로 만든 후 set()에서 관리. in 연산자 사용.

----

문제가 모호한 부분이 있어서 시행 착오가 있음.

17255x.py - 초기 잘못된 구현. 중도 포기.
17255.py - 제대로 풀었으나 pass 못하고 fail.
    문제의 조건에 의심.
    게시판에서 납득이 안되는 반례 발견.
    다시 잘 읽어본 결과, 중복으로 허용하는 조건에 모호한 부분이 있음.
17255c.py
    17255.py 에서 코드를 일부 수정한 후 pass.
17255d.py
    17255c.py 에서 약간의 속도 개선


----
## 알고리즘

용어는 다들 dfs 라는 용어로 풀고 있는데, 그래프 구조라고 굳이 봐야 할 이유는 없어 보이고.
백트래킹 이라고 볼 수도 있는데 가지치기 라고 볼 만한 부분도 딱히 없음.
어찌 보면 주어진 상황에서 모든 가능한 경우를 시도하는 brute-force 방식이라고도 볼 수 있음.

----
## 성능 비교

stack (history) 대신 그냥 매번 만들어진 history를 재귀호출 인자로 전달하는 방법이
아주 약간 더 빠른 것으로 보임.

또한, 최초 입력 받은 숫자를 굳이 숫자로 관리할 필요도 없음. 그냥 문자열이라고 봐도 무방.
-> 17255d.py 참고

알고리즘을 바꿔서 시도한 버전은 17255e.py 참고


97561179 cafrii  17255  맞았습니다!!  32412KB  36ms  Python 3   757B  <- 17255e
97552062 cafrii  17255  맞았습니다!!  32412KB  36ms  Python 3   981B  <- 17255d
97550995 cafrii  17255  맞았습니다!!  32412KB  36ms  Python 3  1576B  <- 17255c


'''


import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    N = int(input().rstrip())
    return N


def solve2_fail(N:int):
    '''
    solve() 최초 버전에서, dlist, stack 모두 숫자 대신 문자로 저장 관리.
    하지만 여전히 fail

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
        # nonlocal count
        ###log("(%d) [%d:%d] %s", right-left, left, right, dlist[left:right])

        if right - left >= length:
            history = ''.join(stack)
            # log("final %s, stack %s", digitstr, history)
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
            stack.append(dlist[left-1])
            populate(left-1, right)
            stack.pop()
        if right < length: # 오른쪽 채우기
            ###log("    right fill %s", dlist[right])
            stack.append(dlist[right])
            populate(left, right+1)
            stack.pop()
        return

    populate(0, 0)
    return len(history_set)


if __name__ == '__main__':
    inp = get_input()
    print(solve2_fail(inp))




'''

예제 입력 1
521
예제 출력 1
4
521을 만드는 방법은 다음과 같이 4가지이다.

1 → 21 → 521
2 → 21 → 521
2 → 52 → 521
5 → 52 → 521


예제 입력 2
9111
예제 출력 2
4

9111을 만드는 방법은 다음과 같이 4가지이다.

1 → 11 → 111 → 9111
1 → 11 → 911 → 9111
1 → 91 → 911 → 9111
9 → 91 → 911 → 9111


----

run=(python3 17255.py)

echo '123' | $run
# -> 4

echo '9111' | $run
# -> 4

echo '21112' | $run
# -> 4??
# 이게 8 이 나와야 한다고?


'''

