
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    tt = list(map(int, input().split())) # those who know truth: [num, ...]
    # assert tt[0] == len(tt)-1, "wrong a format"
    del tt[0]
    parties = []
    for _ in range(M):
        gg = list(map(int, input().split()))
        # assert gg[0] == len(gg)-1, "wrong gg format"
        parties.append(gg[1:])
    return N,tt,parties

def solve(N:int, tt:list[int], parties:list[list[int]])->int:
    '''
        tt: 진실을 아는 사람 목록
    '''
    roots = list(range(N+1))

    def find_root(a:int)->int:
        # 요소 a 가 속한 집합의 대표값을 리턴
        if a == roots[a]: return a
        roots[a] = find_root(roots[a])
        return roots[a]

    ra = 0 # 번호 0은 사용되지 않으므로, 진실 그룹의 초기 대표자로 지정.
    for b in tt:
        rb = find_root(b)
        if ra == rb: continue
        roots[rb] = roots[b] = ra

    for guests in parties:
        # 파티에 참석한 게스트들은 모두 한 그룹에 소속되게 됨.
        if len(guests) <= 1: continue
        a,ra = guests[0],find_root(guests[0])
        for b in guests[1:]:
            rb = find_root(b)
            if ra == rb: continue
            if rb == 0: roots[ra] = roots[a] = 0
            else: roots[rb] = roots[b] = ra

    return [ find_root(g[0])>0 for g in parties ].count(True)

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
