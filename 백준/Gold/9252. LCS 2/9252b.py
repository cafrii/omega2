'''
    풀다가 포기한 버전!
'''

import sys
def log(fmt, *args): print(fmt % args, file=sys.stderr)

A1 = input().strip()
A2 = input().strip()

def find_lcs(depth, idx1, idx2) -> str:
    if idx1 >= len(A1) or idx2 >= len(A2):
        return ''
    indent = ' ' * depth
    #log('%s(%d,%d) ???? %s, %s', indent, idx1, idx2, A1[idx1:], A2[idx2:])

    lcs_list = []
    for k1 in range(idx1, len(A1)):
        for k2 in range(idx2, len(A2)):
            if A1[k1] != A2[k2]: continue

            # #log('%s(%d,%d) found %s', indent, k1, k2, A1[k1])
            lcs = find_lcs(depth+1, k1+1, k2+1)
            if lcs:
                lcs_list.append(A1[k1] + lcs)
            else:
                lcs_list.append(A1[k1])

    if lcs_list:
        # indent = ' ' * depth
        #log('%s(%d,%d) lcs list: #%d, %s', indent, idx1, idx2, len(lcs_list), lcs_list)
        lcs_list.sort(key = lambda s: len(s), reverse = True)
        #log("%s(%d,%d) lcs: '%s'", indent, idx1, idx2, lcs_list[0])
        return lcs_list[0]
    else:
        #log('%s(%d,%d) no lcs', indent, idx1, idx2)
        return ''


ans = find_lcs(0, 0, 0)
print(len(ans))
if len(ans) > 0:
    print(ans)


'''
echo 'ACAYKP\nCAPCAK' | python3 9252.py


echo 'A\nB' | python3 9252.py
echo 'A\nA' | python3 9252.py
echo 'A\nAB' | python3 9252.py
echo 'AB\nKAB' | python3 9252.py

echo 'ACA\nCAP' | python3 9252.py


ASDGEGRDTJDJSERGHRTF
SGHRESGSFGSERGSDFGESRGSDF
-> 10
SGEGRDSRGF

ASDGEGRDTJDJSERGHRTFSGHRESGSFGSERG
SDFGSAFAWFSFSGRFWAFWERGEFAGERFSGFF



ASDGEGRDTJDJSERGHRTFSGHRESGSFGSERGSDFGESRGSDFGESRGSWGFATWERTERGERGEGRQWERQWERQWEFWFQWFAGAEWFADSFAWEFASDFSERGAF
SDFGSAFAWFSFSGRFWAFWERGEFAGERFSGFFSERFSFSERFSDFWEFASDFGSAFAWFSFSGRFWAFWERGEFAGERFSGFFSERFSFSERFSDFWEFASDFAW



'''