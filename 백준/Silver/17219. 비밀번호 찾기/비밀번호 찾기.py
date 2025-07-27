
import sys

def get_input():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    memo = {}
    for _ in range(N):
        url,pswd = input().split()
        memo[url] = pswd
    def gen_urls():
        for _ in range(M):
            url = input().rstrip()
            yield url
        return
    return memo,gen_urls()

def solve(memo, g):
    for url in g:
        yield memo[url]
    return

if __name__ == '__main__':
    inp = get_input()
    for a in solve(*inp):
        print(a)
