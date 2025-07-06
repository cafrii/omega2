
import sys
input = sys.stdin.readline

def solve(A:str, B:str)->str:
    '''
    '''
    ha,hb = [0]*26,[0]*26  # alphabet histogram of string a,b

    for a in A:
        id = ord(a)-ord('a')
        ha[id] += 1
    for b in B:
        id = ord(b)-ord('a')
        hb[id] += 1

    # find common of both
    hc = [ min(ha[k], hb[k]) for k in range(26) ]

    # generate
    result = []
    for i in range(26):
        if not hc[i]: continue
        result.extend([chr(ord('a') + i)]*hc[i])

    return ''.join(result)


while True:
    try:
        A,B = input(),input()
    except EOFError:
        break
    # for readline, it returns empty string at EOF.
    if A == "" or B == "":
        break
    A,B = A.strip(),B.strip()
    print(solve(A, B))
