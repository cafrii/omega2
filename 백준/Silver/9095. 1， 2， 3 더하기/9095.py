

import sys
input = sys.stdin.readline

def solve(N) -> list[int]:
    ans = [0] * (N+1) # 0 ~ N
    # ans[:4] = [1,1,2,4]
    ans[0] = 1
    # ans[0] is for special purpose, which means i(index) itself.

    for i in range(1,N+1):
        ans[i] = (0
            + (ans[i-1] if i-1>=0 else 0)
            + (ans[i-2] if i-2>=0 else 0)
            + (ans[i-3] if i-3>=0 else 0)
        )
        # print(f'ans[{i}] = {ans[i]}')
    return ans

T = int(input().strip())
Ns = []
for _ in range(T):
    Ns.append(int(input().strip())) # N: 1~11
ans = solve(max(Ns))
for N in Ns:
    print(ans[N])



'''
echo '3\n4\n7\n10' | python3 9095.py

'''


'''
*** 0

*** 1
1

*** 2
2
1+1

*** 3
3
1+2
2+1
1+1+1

*** 4
1+3
2+2
1+1+2
3+1
1+2+1
2+1+1
1+1+1+1



'''