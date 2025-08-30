import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    M,N = map(int, input().split())

    d2s = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    A = []
    for d in range(M,N+1):
        if d < 10:
            s = d2s[d]
        elif d <= 99:
            s = f'{d2s[d//10]} {d2s[d%10]}'
        else:
            s = '?'
        A.append((s, d))

    A.sort()

    BL = []
    while A:
        BL.append(A[:10])
        del A[:10]
    for b in BL:
        print(' '.join( str(d) for _,d in b ))
