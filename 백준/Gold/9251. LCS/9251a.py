'''
풀다가 중단한 것
'''

import sys
def log(fmt, *args): print(fmt % args, file=sys.stderr)

from dataclasses import dataclass
import copy

A = input().strip()
B = input().strip()

MAX = 1000

@dataclass
class Lcs:
    len: int = 0
    tail: list[tuple[str,str]] = []
    # tail_a: str = ''
    # tail_b: str = ''


lcs = [ [ Lcs() for c in range(MAX+1) ] for r in range(MAX+1) ]
# LCS[j][k] 는 [ lcslen, tail_of_a, tail_of_b ]
#    A 의 첫 j개 부분문자열 A[:j]과 B 의 첫 k개 부분문자열 B[:k]의 lcs 관련 정보
#    lcslen:   lcs 문자열 길이. lcs 자체를 저장하진 않는다.
#    tail_of_a:  A[:j] 에서 lcs 문자열 뒷부분
#    tail_of_b:  B[:k]  ,,
#
# 앞에서부터 채운 후, 최종 정답은 lcslen[len(A)][len(B)][0] 에서 얻는다.


def solve():
    # A 는 고정하고 B 를 하나씩 늘려가면서 계산해 보자.
    ans = [ 0 ]
    # ans[k] 는 A[:] 와 B[:k] 의 lcs 길이.

    for j in range(1, len(A)+1):
        for k in range(1, len(B)+1):

            # lcslen[j][k] 는 이전 데이터를 이용하여 구해야 한다.
            # if A[j] == B[k]:
            #     lcs[j][k].len = lcs[j-1][k-1].len + 1
            #     continue
            lcs_jka, lcs_jkb = None, None

            # lcs[j][k-1] 로부터 B에서 글자 하나 추가. 새로 늘어난 글자는 B[k]
            longest_ta = ''
            new_lcs_len = lcs[j][k-1].len
            for ta,tb in lcs[j][k-1].tail:
                if idx := ta.find(B[k]) < 0: continue
                new_lcs_len = lcs[j][k-1].len + 1
                new_ta = ta[idx+1:]
                if len(new_ta) > len(longest_ta):
                    longest_ta = new_ta
            if new_lcs_len
            lcs_jkb = Lcs(new_lcs_len, [
                        longest_ta, ''
                    ])


            if idx := lcs[j][k-1].tail_a.find(B[k]) >= 0:
                lcs_jkb = Lcs(lcs[j][k-1].len + 1,
                                lcs[j][k-1].tail_a[idx+1:],
                                '')  # lcs[j][k-1].tail_b 에는 B[k]가 존재하지 않는다.
            else: # 이전과 동일한 경우.
                lcs_jkb = Lcs(lcs[j][k-1].len,
                              lcs[j][k-1].tail_a,
                              lcs[j][k-1].tail_b + B[k])
                # lcs_jkb = copy.deepcopy(lcs[j][k-1])

            # lcs[j-1][k] 로부터 B에서 글자 하나 추가. 새로 늘어난 글자는 A[k]
            if idx := lcs[j-1][k].tail_b.find(A[k]) >= 0:
                lcs_jka = Lcs(lcs[j-1][k].len + 1,
                                '',
                                lcs[j-1][k].tail_b[idx+1:])
            else: # 이전과 동일
                lcs_jka = Lcs(lcs[j-1][k].len,
                              lcs[j-1][k].tail_a + A[k],
                              lcs[j-1][k].tail_b)

            # 둘 다 존재할 경우,
            if lcs_jka.len > lcs_jkb.len:
                lcs[j][k] = lcs_jka
            elif lcs_jka.len < lcs_jkb.len:
                lcs[j][k] = lcs_jkb
            else: # lcs 길이가 같다면 tail 이 긴 쪽을 선택해야 함!
                if len(lcs_jka.tail_a) >= len(lcs_jkb.tail_)
            if lcs_jka and lcs_jkb:
                lcs_jk = lcs_jka if lcs_jka.len >= lcs_jkb.len else lcs_jkb
            elif lcs_jka:
                lcs_jk = lcs_jka
            elif lcs_jkb:
                lcs_jk = lcs_jkb
            elif ...
            # 포기.. 이렇게 복잡할 리가 없음.




