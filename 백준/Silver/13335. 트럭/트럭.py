
import sys
from collections import deque

def get_input():
    input = sys.stdin.readline
    N,W,L = map(int, input().split())
    A = list(map(int, input().split()))
    #assert len(A) == N, "wrong A"
    return A,W,L

def solve(A:list[int], len_br:int, max_load:int):
    '''
        A: list, weight of each truck
        len_br: length of bridge
        max_load: max load of bridge
    '''
    trucks = deque(A)
    bridge = deque([0]*len_br) # pre-fill

    max_t = len_br * len(A)
    t = 0
    for t in range(1, max_t+100): # 100 is safe margin
        bridge.popleft()
        if trucks and sum(bridge) + trucks[0] <= max_load:
            bridge.append(trucks[0])
            trucks.popleft()
        else:
            bridge.append(0)
        if len(trucks) == 0 and sum(bridge) == 0:
            break
    return t

if __name__ == '__main__':
    inp = get_input()
    r = solve(*inp)
    print(r)
