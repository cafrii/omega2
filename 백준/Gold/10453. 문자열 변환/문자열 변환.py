
import sys

def get_input():
    input = sys.stdin.readline
    T = int(input().rstrip())
    def get_it():
        for _ in range(T):
            a,b = input().split()
            yield a,b
    return get_it(),

def solve(s1:str, s2:str)->int:
    '''
    Returns:
        number of flips required to convert from string s1 to s2.
    '''
    N = len(s1)
    assert s1[0]=='a'==s2[0], "bad string head"
    assert s1[-1]=='b'==s2[-1], "bad string tail"

    # convert ab string to nested depth list
    d1,d2 = [1],[1]
    for i in range(1,N):
        # nested level calculation
        if s1[i]=='a': d1.append(d1[-1]+1)
        elif s1[i]=='b': d1.append(d1[-1]-1)
        else: assert False, "wrong string s1"

        if s2[i]=='a': d2.append(d2[-1]+1)
        elif s2[i]=='b': d2.append(d2[-1]-1)
        else: assert False, "wrong string s2"

    # 요소의 모든 값이 >=0 이면 good string.
    assert sum((1 for k in d1 if k<0), 0)==0, "d1 is bad"
    assert sum((1 for k in d2 if k<0), 0)==0, "d2 is bad"

    assert d1[-1]==d2[-1]==0, "badly nested"

    # ?ab -> ?ba: de-nesting
    #   ex: 343 -> 323,  net absdiff: -2
    # ?ba -> ?ab: en-nesting
    #   ex: 212 -> 232,  net absdiff: +2

    diff = 0
    for k1,k2 in zip(d1,d2):
        diff += abs(k1-k2)
    assert diff%2 == 0, "diff should be even"
    return diff // 2

if __name__ == '__main__':
    it, = get_input()
    for a,b in it:
        assert len(a)==len(b)
        print(solve(a,b))
