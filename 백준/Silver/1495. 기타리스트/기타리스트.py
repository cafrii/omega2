
import sys
input = sys.stdin.readline

N,S,M = map(int, input().split())

# S: 시작 볼륨
# M: 최대 볼륨. 볼륨 허용 값의 범위는 0~M

delta = list(map(int, input().split()))
assert len(delta) == N

def solve():
    vol =  set()
    vol.add(S)

    for d in delta:
        if not vol: break
        nextvol = set()
        for v in vol:
            if v+d <= M: nextvol.add(v+d)
            if v-d >= 0: nextvol.add(v-d)
        vol = nextvol

    return max(vol) if vol else -1

print(solve())
