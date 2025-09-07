'''
1, 2, 3 더하기 4

사실상 brute force 풀이 이므로,
단지 slow 만 문제가 되는 게 아니고 메모리도 문제가 될 것임!

'''



import sys

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def get_input():
    input = sys.stdin.readline
    C = int(input().rstrip())
    Ns = []
    for _ in range(C):
        Ns.append(int(input().rstrip()))
    return Ns,


def solve0(Ns:list[int])->list[str]:
    '''
        N: 1 ~ 10_000
        set 를 이용하려는데, 리스트가 non-hashable 이라서 넣을 수 없음.
        그래서 별도로 문자열 화 해서 사용. 오버헤드가 클 것임.
    '''

    max_n = max(Ns)
    alloc_n = max(max_n, 4)

    dx:list[set[str]] = [ set() for j in range(alloc_n+1) ]

    dx[0].update([ '000000000000000' ]) # [ [0,0,0] ]
    dx[1].update([ '000010000000000' ]) # [ [1,0,0] ]
    dx[2].update([ '000020000000000', '000000000100000' ]) # [ [2,0,0], [0,1,0] ]
    dx[3].update([ '000030000000000', '000010000100000', '000000000000001' ]) # [ [3,0,0], [1,1,0], [1,1,0], [0,0,1] ]

    for k in range(4, max_n+1):
        for h in dx[k-1]:
            a,b,c = int(h[:5]),int(h[5:10]),int(h[10:])
            dx[k].add( f'{a+1:05}{b:05}{c:05}' )
        for h in dx[k-2]:
            a,b,c = int(h[:5]),int(h[5:10]),int(h[10:])
            dx[k].add( f'{a:05}{b+1:05}{c:05}' )
        for h in dx[k-3]:
            a,b,c = int(h[:5]),int(h[5:10]),int(h[10:])
            dx[k].add( f'{a:05}{b:05}{c+1:05}' )

        # dx[k].update([ [a+1,b,c] for a,b,c in dx[k-1] ])
        # dx[k].update([ [a,b+1,c] for a,b,c in dx[k-2] ])
        # dx[k].update([ [a,b,c+1] for a,b,c in dx[k-3] ])

        # log("%d: #%d, %s", k, len(dx[k]), dx[k])
        log("%d: #%d", k, len(dx[k]))

    ans = []
    for n in Ns:
        ans.append(str(len(dx[n])))
    return ans


def solve(Ns:list[int])->list[str]:
    '''
    set 대신 dict 를 사용. key 생성에는 비용이 들지만 값은 있는 그대로 추출 가능하긴 한데..
    그럼에도 불구하고 느림.
    이 방법이 아닌 뭔가 새로운 방법이 있을 듯..
    '''

    max_n = max(Ns)
    alloc_n = max(max_n, 4)

    def hash(v:list)->str:
        return '/'.join(map(str, v))
    # def add_one(d:dict, v:list):
    #     d[hash(v)] = v
    def addx(d:dict, *args): # vs:list[list])
        for v in args: d[hash(v)] = v

    dx:list[dict[str,list]] = [ {} for j in range(alloc_n+1) ]

    addx(dx[0], [0,0,0])
    addx(dx[1], [1,0,0])
    addx(dx[2], [2,0,0], [0,1,0])
    addx(dx[3], [3,0,0], [1,1,0], [0,0,1])

    # for k in range(3):
    #     log("%d: #%d, %s", k, len(dx[k]), dx[k])

    for k in range(4, max_n+1):
        for a,b,c in dx[k-1].values():
            addx(dx[k], [a+1,b,c])
        for a,b,c in dx[k-2].values():
            addx(dx[k], [a,b+1,c])
        for a,b,c in dx[k-3].values():
            addx(dx[k], [a,b,c+1])

        # log("%d: #%d, %s", k, len(dx[k]), dx[k])
        log("%d: #%d, %s", k, len(dx[k]), dx[k].values())
        # log("%d: #%d", k, len(dx[k]))

    ans = []
    for n in Ns:
        ans.append(str(len(dx[n])))
    return ans


if __name__ == '__main__':
    ans = solve(*get_input())
    print('\n'.join(ans))


'''
예제 입력 1
3
4
7
10
예제 출력 1
4
8
14
----

run=(python3 15989.py)

echo '3\n4\n7\n10' | $run
# 4 8 14

echo '1\n3' | $run
# 3

echo '1\n10' | $run
# 14

echo '1\n100' | $run
# 884

echo '1\n300' | time $run
# 7651
# -- solve1
# $run  1.33s user 0.13s system 53% cpu 2.709 total
# -- solve2
# $run  1.06s user 0.03s system 98% cpu 1.111 total

echo '1\n500' | time $run
# 21084

echo '1\n700' | time $run
# 41184
#  $run  21.69s user 0.40s system 99% cpu 22.240 total
# 사실, 이미 300 만 넘어가도 시간 초과 됨.


'''


