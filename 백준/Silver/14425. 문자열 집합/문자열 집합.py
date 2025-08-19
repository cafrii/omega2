
import sys

def solve():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    S = set()
    for _ in range(N):
        S.add(input().rstrip())
    matched = 0
    for _ in range(M):
        m = input().rstrip()
        if m in S: matched += 1
    return matched

if __name__ == '__main__':
    print(solve())
