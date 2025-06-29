'''
좀 더 최적화 된 방법

내 코드의 용어를 기준으로..
1. D 자체를 관리하지 않고 L 만 관리하고 있다. 아래 코드에서 dp 가 L의 역할 수행.
   L 메모리를 미리 할당하지 않고, append 로 증가시키는 방법 사용.
2. L 에 A[k]만 저장하는게 아니라 k 인덱스도 같이 저장한다. (idxs 라는 별도의 리스트에..)
3. 나중에 복원을 쉽게 추적하기 위해 from_idx[] 도 같이 관리.

내 코드에 비해 시간을 좀 더 단축시킬 수 있는 이유는 바로 3번 때문.

'''

import sys
import bisect
input = sys.stdin.readline

def log(fmt, *args): print(fmt % args, file=sys.stderr)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = []
    idxs = []
    from_idx = [-1] * n

    for i, num in enumerate(arr):
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
            idxs.append(i)
        else:
            dp[idx] = num
            idxs[idx] = i
        if idx != 0:
            from_idx[i] = idxs[idx - 1]
        log('arr  : %s', arr[:i+1]) # 3 1 4 1 5 9 2 6 5
        log('dp   : %s', dp)    # 1 4 5 9
        log('idxs : %s', idxs)  # 1 2 4 5
        log('from :  %s', ', '.join(str(e) if e>=0 else '_' for e in from_idx[:i+1]))
          # . 1 . . . . . . .


    print(len(dp))

    last_idx = idxs[-1]
    result = []
    while last_idx != -1:
        result.append(arr[last_idx])
        last_idx = from_idx[last_idx]
    result.reverse()
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()

'''
arr  : 3 1 4 1 5 9 2 6 5
dp   : 1 4 5 9
idxs : 1 2 4 5
from : . 1 . . . . . . .


'''
