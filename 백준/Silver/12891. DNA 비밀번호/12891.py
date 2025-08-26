'''
12891번
DNA 비밀번호 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	34584	12927	9349	35.838%

문제
평소에 문자열을 가지고 노는 것을 좋아하는 민호는 DNA 문자열을 알게 되었다.
DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열을 말한다.
예를 들어 “ACKA”는 DNA 문자열이 아니지만 “ACCA”는 DNA 문자열이다.
이런 신비한 문자열에 완전히 매료된 민호는 임의의 DNA 문자열을 만들고 만들어진 DNA 문자열의 부분문자열을 비밀번호로 사용하기로 마음먹었다.

하지만 민호는 이러한 방법에는 큰 문제가 있다는 것을 발견했다.
임의의 DNA 문자열의 부분문자열을 뽑았을 때 “AAAA”와 같이 보안에 취약한 비밀번호가 만들어 질 수 있기 때문이다.
그래서 민호는 부분문자열에서 등장하는 문자의 개수가 특정 개수 이상이여야 비밀번호로 사용할 수 있다는 규칙을 만들었다.

임의의 DNA문자열이 “AAACCTGCCAA” 이고 민호가 뽑을 부분문자열의 길이를 4라고 하자.
그리고 부분문자열에 ‘A’ 는 1개 이상, ‘C’는 1개 이상, ‘G’는 1개 이상,
‘T’는 0개 이상이 등장해야 비밀번호로 사용할 수 있다고 하자.
이때 “ACCT” 는 ‘G’ 가 1 개 이상 등장해야 한다는 조건을 만족하지 못해 비밀번호로 사용하지 못한다.
하지만 “GCCA” 은 모든 조건을 만족하기 때문에 비밀번호로 사용할 수 있다.

민호가 만든 임의의 DNA 문자열과 비밀번호로 사용할 부분분자열의 길이,
그리고 {‘A’, ‘C’, ‘G’, ‘T’} 가 각각 몇번 이상 등장해야 비밀번호로 사용할 수 있는지 순서대로 주어졌을 때
민호가 만들 수 있는 비밀번호의 종류의 수를 구하는 프로그램을 작성하자.
단 부분문자열이 등장하는 위치가 다르다면 부분문자열이 같다고 하더라도 다른 문자열로 취급한다.

입력
첫 번째 줄에 민호가 임의로 만든 DNA 문자열 길이 |S|와 비밀번호로 사용할 부분문자열의 길이 |P| 가 주어진다.
(1 ≤ |P| ≤ |S| ≤ 1,000,000)

두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.

세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다.
각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.

출력
첫 번째 줄에 민호가 만들 수 있는 비밀번호의 종류의 수를 출력해라.

------

7:41~8:20

'''


import sys
from collections import defaultdict


def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    S,P = map(int, input().split())
    rstr = input().rstrip() # random string
    mc = list(map(int, input().split())) # min. count
    # assert len(mc) == 4, "wrong mc"
    return rstr,P,mc

def solve(rstr:str, P:int, mc:list[int])->int:
    '''
    '''
    # log('%s', rstr)
    # log('P:%d, %s', P, mc)

    N = len(rstr)
    s = 0 # start position of substr

    count = 0 # valid string count
    usecnt = defaultdict(int)

    def is_valid()->bool:
        return usecnt['A']>=mc[0] and usecnt['C']>=mc[1] and \
            usecnt['G']>=mc[2] and usecnt['T']>=mc[3]

    # initial pooling
    for k in range(s,s+P): # s ~ s+P-1
        usecnt[rstr[k]] += 1
    if is_valid():
        count += 1

    for s in range(1, N-P+1):
        # remove rstr[s-1] and add rstr[s+P]
        usecnt[rstr[s-1]] -= 1
        usecnt[rstr[s+P-1]] += 1
        if is_valid():
            count += 1

    return count


if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)


'''
예제 입력 1
9 8
CCTGGATTG
2 0 1 1
예제 출력 1
0
예제 입력 2
4 2
GATA
1 0 0 1
예제 출력 2
2

----

run=(python3 12891.py)

echo '9 8\nCCTGGATTG\n2 0 1 1' | $run
# 0

echo '4 2\nGATA\n1 0 0 1' | $run
# 2

echo '4 3\nGATA\n1 0 0 1' | $run
# 2



(python3 <<EOF
from random import randint
# S,P = 10,8
S,P = 100,10
# S,P = 1_000_000,100_000
print(S, P)
print(''.join(['ACGT'[randint(0,3)] for s in range(S)]))
mc = [randint(0,max(1,P//5)) for k in range(4)]
print(' '.join(map(str, mc)))
EOF
) | time $run

# 900001
$run  0.27s user 0.01s system 48% cpu 0.575 total


'''
